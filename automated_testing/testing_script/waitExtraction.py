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
    # base template device resolution 
    base_w = 2560
    base_h = 1800

    def __init__(self,udId,port,file,id):
        self.count = id
        self.udid = udId
        self.platformName = 'Android'
        self.deviceName = 'Device'
        self.appPackage = 'com.maq.xprize.onecourse.hindi'
        self.appActivity = 'com.maq.xprize.onecourse.hindi.mainui.DownloadExpansionFile'
        self.url = 'http://localhost:'+port+'/wd/hub'
        self.base = os.path.dirname(os.path.realpath(file))
        self.output = os.path.join(self.base,'results',udId)+r"\outputs"
        self.template = self.base+r"\images\templates"
        self.test = os.path.join(self.base,'results',udId)+r"\tests"

      #click element if exists
    def click_elements(self,points,driver):
        # sw,sh =driver.get_window_size()    and points[0][1] < sh and points[0][0] < sw:

        if points[0][0] != -1 :
            TouchAction(driver).tap(None, points[0][0] , points[0][1], 0.5).perform()
    def check_exists1(self,id,driver):
        sleep(2)
        try:
            driver.find_element_by_id(id)
            return True    
        except NoSuchElementException:
            return False
        
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

    #wait extracting 
    def wait_for_extraction(self,driver):
        while self.check_exists1('com.maq.xprize.onecourse.hindi:id/progressBar',driver):
            sleep(30)
            print('Waiting extraction')
    #allow permission
    def allow_permission(self,driver):
        sleep(2)
        for x in range(3):
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
    #match template function
    def find_matches(self,driver,screenshot, template):
        threshold = 0.5
        temp = cv2.imread(template)
        screen = cv2.imread(screenshot)
        a,sw,sh = screen.shape[::-1]
        a,w, h = temp.shape[::-1]
        h = int(h * sh/self.base_h)
        w = int(w * sw/self.base_w)
        if float(sh/self.base_h) == float(sw/self.base_w) and  float(sh/self.base_h) == 1.0:
            threshold = 0.8
        temp = cv2.resize(temp, (w,h))
        res = cv2.matchTemplate(screen,temp,cv2.TM_CCOEFF_NORMED)  # @UndefinedVariable
        loc = np.where( res >= threshold )
        try:
            temp = loc[0][0]
            points = []
            # Counts the matches themselves
            #and saves their centers to an array
            for pt in zip(*loc[::-1]):
                # Draw a rectangle around the matched region.
                cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (255,0,0), 2)
                # Center of matched frame
                points.append(((pt[0]+w/2), pt[1]+h/2))
            print( "Pass")
            cv2.line(screen,(int(points[0][0]),int(points[0][1])),(int(points[0][0]),int(points[0][1])),(0,0,225),10)
            cv2.imwrite(self.output+r"\output_t"+str(self.count)+r".png",screen)
            self.count+=1
            return points
        except IndexError:
            driver.save_screenshot(self.output+r"\output_t"+str(self.count)+r".png")
            print("Fail")
            self.count+=1
            return [(-1,-1)]

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
    def main(self):
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        driver=self.connect('false')
        print("Extraction")
        # allow permission
        self.allow_permission(driver)
        sleep(2)
        driver.save_screenshot(self.test+r"\loading.png")
        # check screen loaded
        sleep(2)
        self.check_exists('com.maq.xprize.onecourse.hindi:id/progressBar',driver)
        self.check_exists('com.maq.xprize.onecourse.hindi:id/oneTimeExtractionEnglish',driver)
        self.check_exists('com.maq.xprize.onecourse.hindi:id/oneTimeExtractionHindi',driver)
        self.check_exists('com.maq.xprize.onecourse.hindi:id/percentText',driver)
        self.check_exists('com.maq.xprize.onecourse.hindi:id/splashScreenBackground',driver)
        # wait extracting 
        self.wait_for_extraction(driver)     
        sleep(2)
        driver.save_screenshot(self.test+r"\loading.png")
        points = self.find_matches(driver,self.test+r"\loading.png",self.template+r"\pixeltab_ready.png")
        sleep(5)
        self.click_elements(points,driver)
        sleep(2)    
        print("Done Extraction")
        driver.close_app()
        os.system("python "+self.base+ "\gameSection.py "+arg1+" "+arg2)
if __name__ == "__main__":
    testingOperationObject = testingOperation(sys.argv[1],sys.argv[2],__file__,1).main()

    