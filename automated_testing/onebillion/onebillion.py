import cv2 
import numpy as np 
import os
import sys
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

# global variables
class testingOperation:  
    # base template device resolution width and height based on portrait mode
    base_w = 2560
    base_h = 1800
    isTablet = False
    def __init__(self,udId,port,file,id):
        self.count = id # result counter used for screen and text results
        # Required capabilities to setup connection between script, Appium server and device
        self.udid = udId
        self.platformName = 'Android'
        self.deviceName = 'Device'
        self.appPackage = 'com.maq.xprize.onecourse.hindi'
        self.appActivity = 'com.maq.xprize.onecourse.hindi.mainui.DownloadExpansionFile'
        self.url = 'http://localhost:'+port+'/wd/hub'

        # Different files paths used in testing
        self.base = os.path.dirname(os.path.realpath(file))
        self.output = os.path.join(self.base,'results',udId)+r"\outputs"
        self.template = self.base+r"\images\templates"
        self.test = os.path.join(self.base,'results',udId)+r"\tests"

        # Extracts device properties
        os.system("adb -s "+udId+" shell getprop ro.build.characteristics > devices"+udId+".txt")
        file = open("devices"+udId+".txt",'r')
        for line in file:
            if 'tablet' in line:
                self.isTablet = True
                print("Tablet Device")
        if not self.isTablet:
                print("Mobile Device")
        file.close()
        # delete created file after use 
        os.system("del devices"+udId+".txt")

    # click element if exists
    def click_elements(self,points,driver):
        if points[0][0] != -1 :
            TouchAction(driver).tap(None, points[0][0] , points[0][1], 0.5).perform()

    # checks if element exists or not using its id. return type boolean
    def check_exists1(self,id,driver):
        sleep(2)
        try:
            driver.find_element_by_id(id)
            return True    
        except NoSuchElementException:
            return False
    
    # checks if element exists or not using its id, print result and save screen
    def check_exists(self,id,driver):
        sleep(2)
        try:
            driver.find_element_by_id(id)
            driver.save_screenshot(self.output+r"\output_t"+str(self.count)+r".png")
            print("Pass")
            
        except NoSuchElementException:
            driver.save_screenshot(self.output+r"\output_t"+str(self.count)+r".png")
            print("Fail")
        self.count+=1

    #wait OBB extraction
    def wait_for_extraction(self,driver):
        while self.check_exists1(self.appPackage+':id/progressBar',driver):
            sleep(30)
            print('Waiting extraction')

    #allow permission
    def allow_permission(self,driver):
        sleep(2)
        for x in range(3):  # iter according to the number of permission needs to be allowed
            # based on different types of devices, text may differ.
            try:
                driver.save_screenshot(self.output+r"\output_t"+str(self.count)+r".png")    
                driver.find_element_by_android_uiautomator('text("ALLOW")').click()
                print("Pass")
            except NoSuchElementException:
                try:
                    driver.save_screenshot(self.output+r"\output_t"+str(self.count)+r".png")
                    driver.find_element_by_android_uiautomator('text("Allow")').click()
                    print("Pass")
                except NoSuchElementException:
                    driver.save_screenshot(self.output+r"\output_t"+str(self.count)+r".png")
                    print("Fail")

            self.count+=1
            sleep(2)
        sleep(2)

    # matches template on current screen
    def find_matches(self, driver, template):
        driver.save_screenshot(self.test+r"\currenScreen.png")
        temp = cv2.imread(template)
        screen = cv2.imread(self.test+r"\currenScreen.png")

        a,sw,sh = screen.shape[::-1]
        a,w, h = temp.shape[::-1]
        # scales the reference template according to current device's resolution
        h = int(h * sh/self.base_h)
        w = int(w * sw/self.base_w)
        # check if the current device have same resolution as the reference device and sets threshold  
        if float(sh/self.base_h) == float(sw/self.base_w) and  float(sh/self.base_h) == 1.0:
            threshold = 0.8
        else:
            threshold = 0.5

        temp = cv2.resize(temp, (w,h))
        res = cv2.matchTemplate(screen,temp,cv2.TM_CCOEFF_NORMED)  # 
        loc = np.where( res >= threshold )
        
        # handles the case when no object is been detected
        try:
            temp = loc[0][0]
            points = []

            for pt in zip(*loc[::-1]):
                # Center of matched frame
                points.append(((pt[0]+w/2), pt[1]+h/2))
            print( "Pass")
            # Draws a rectangle around the matched region.
            cv2.rectangle(screen, (int(points[0][0] - w/2), int(points[0][1] - w/2)), (int(points[0][0] + w/2), int(points[0][1] + h/2)), (255,0,0), 8)
            # Draws center point of element where click will happen.
            cv2.line(screen,(int(points[0][0]), int(points[0][1])), (int(points[0][0]), int(points[0][1])),(0,0,225),10)
            # write the result back to the system      
            cv2.imwrite(self.output+r"\output_t"+str(self.count)+r".png",screen)
            self.count+=1
            return [(points[0][0],points[0][1])]
        except IndexError:
            driver.save_screenshot(self.output+r"\output_t"+str(self.count)+r".png")
            print("Fail")
            self.count+=1
            return [(-1,-1)]

    # connects the appium server and the device. As a result this function returns the instance of the connected device 
    def connect(self,noReset):
        desired_caps={}
        desired_caps['udid'] = self.udid
        desired_caps['platformName'] = self.platformName
        desired_caps['deviceName']=self.deviceName
        desired_caps['appPackage'] = self.appPackage
        desired_caps['appActivity'] = self.appActivity
        desired_caps['noReset'] = noReset
        # initiate application on server 
        driver = webdriver.Remote(self.url, desired_caps)
        return driver
    
    # uses double tap back functionality to close the application
    def exit_application(self,driver):
        driver.back()
        sleep(1)
        driver.back()
        sleep(2)

    def main(self):
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        driver=self.connect('false')
        print("Extraction")
        # allow permission
        self.allow_permission(driver)
        sleep(2)
        driver.save_screenshot(self.test+r"\loading.png")
        # check the loaded screen
        sleep(2)
        self.check_exists(self.appPackage+':id/progressBar',driver)
        self.check_exists(self.appPackage+':id/oneTimeExtractionEnglish',driver)
        self.check_exists(self.appPackage+':id/oneTimeExtractionHindi',driver)
        self.check_exists(self.appPackage+':id/percentText',driver)
        self.check_exists(self.appPackage+':id/splashScreenBackground',driver)

        # wait extracting 
        self.wait_for_extraction(driver)     
        sleep(2)

        
        points = self.find_matches(driver, self.template+r"\pixeltab_ready.png")
        self.click_elements(points,driver)

        sleep(2)    
        print("Done Extraction")
        self.exit_application(driver)

        os.system(r"python "+self.base+ r"\gameSection.py "+arg1+" "+arg2)
            
if __name__ == "__main__":
    testingOperationObject = testingOperation(sys.argv[1],sys.argv[2],__file__,1).main()

    