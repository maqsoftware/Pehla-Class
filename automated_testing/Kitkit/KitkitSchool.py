import os
import cv2
from time import sleep
from appium import webdriver
from pathlib import Path
import numpy as np
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import sys



class testingOperation:  
    # base template device resolution width and height based on portrait mode (Pixel C Tablet)
    base_w = 2560
    base_h = 1440
    base_dpi_w = 532.983
    base_dpi_h = 537.882
    dpi_w = 0.0
    dpi_h = 0.0
    isTablet = False

    def __init__(self,udId,port,file,id):
        self.count = id # result counter used for screen and text results
        # Required capabilities to setup connection between script, Appium server and device
        self.udid = udId
        self.platformName = 'Android'
        self.deviceName = 'Device'
        self.appPackage = 'com.maq.pehlaschool'
        self.appActivity = 'org.cocos2dx.cpp.pehlalauncher.MainActivity'
        self.url = 'http://localhost:'+port+'/wd/hub'

        # Different files paths used in testing
        self.base = os.path.dirname(os.path.realpath(file))
        self.output = os.path.join(self.base,'results',udId)+r"\outputs"
        self.template = self.base+r"\images\templates"
        self.test = os.path.join(self.base,'results',udId)+r"\tests"

        # Extracts device properties
        # DPI
        os.system("adb -s "+udId+" shell dumpsys display > devices"+udId+".txt")
        file = open("devices"+udId+".txt",'r')
        self.dpiLine = []
        for line in file:
            if 'dpi' in line:
                self.dpiLine = line.split('}],')
                break
        for line in self.dpiLine:
            if 'dpi' in line:
                self.dpiLine = (line.split(', '))
                break
        for line in self.dpiLine:
            if 'dpi' in line:
                self.dpiLine = (line.split(' x '))
                break
        self.dpi_h = float(self.dpiLine[0])
        self.dpiLine = self.dpiLine[1].split(' ')
        self.dpi_w = float(self.dpiLine[0])
        file.close()
        os.system("del devices"+udId+".txt")

        # Tablet or Mobile
        os.system("adb -s "+udId+" shell getprop ro.build.characteristics > devices"+udId+".txt")
        file = open("devices"+udId+".txt",'r')
        for line in file:
            if 'tablet' in line:
                self.isTablet = True
                print("Tablet Device")
        if not self.isTablet:
                print("Mobile Device")
        file.close()
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
            print("Pass")
            
        except NoSuchElementException:
            driver.save_screenshot(self.output+r"\output_t"+str(self.count)+r".png")
            print("Fail")
        self.count+=1

    # wait OBB extraction
    def wait_for_extraction(self,driver):
        val = self.check_exists1(self.appPackage+':id/p',driver)
        while self.check_exists1(self.appPackage+':id/p',driver):
            print('Waiting extraction')
            sleep(30)
        return val

    #allow permission
    def allow_permission(self,driver):
        sleep(2)
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
                return False
        
        self.count+=1
        sleep(2)
        return True

    # check tutorial is there or not in a game
    def check_tutorials(self,driver):
        result = self.checkElementByImage(driver,self.template+r"\back.png")
        return not result
    
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
            threshold = 0.6

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
            return [(points[0][0],points[0][1])],True
        except IndexError:
            driver.save_screenshot(self.output+r"\output_t"+str(self.count)+r".png")
            print("Fail")
            self.count+=1
            return [(-1,-1)],False

    # check an element on the screen. Return type is boolean
    def checkElementByImage(self,driver, template):
        driver.save_screenshot(self.test+r"\currentScreen.png")
        
        temp = cv2.imread(template)
        screen = cv2.imread(self.test+r"\currentScreen.png")

        a,sw,sh = screen.shape[::-1]
        a,w, h = temp.shape[::-1]
        # scales the reference template according to current device's resolution
        h = int(h * sh/self.base_h)
        w = int(w  *sw/self.base_w)
        # check if the current device have same resolution as the reference device and sets threshold  
        if float(sh/self.base_h) == float(sw/self.base_w) and  float(sh/self.base_h) == 1.0:
            threshold = 0.8
        else:
            threshold = 0.6

        temp = cv2.resize(temp, (w,h))
        res = cv2.matchTemplate(screen,temp,cv2.TM_CCOEFF_NORMED)  # @UndefinedVariable
        loc = np.where( res >= threshold )
        try:
            temp = loc[0][0]
            return True
        except IndexError:
            return False

    # press back button of the device and save the screen
    def backButton(self,driver):
        driver.save_screenshot(self.output+r"\output_t"+str(self.count)+r".png")
        self.count+=1
        print("Pass")
        sleep(1)
        driver.back()

    # clicks back button of tool section games 
    def toolsCocosBackButton(self,driver):
        driver.save_screenshot(self.output+r"\output_t"+str(self.count)+r".png")
        self.count+=1
        print("Pass")
        driver.find_element_by_id(self.appPackage+':id/v_back').click()
        sleep(1)

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

    def main(self):
        toolSection=[1,1,2,2,3,1,0,0]
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        # connects to luncher application
        driver=self.connect('true')
		
        # allow permission
        self.allow_permission(driver)
        sleep(2)
        driver.save_screenshot(self.test+r"\mainscreen.png")
        # check screen loaded
        sleep(2)
        driver.save_screenshot(self.output+r"\output_t"+str(self.count)+r".png")
        self.count+=1
        self.check_exists(self.appPackage+':id/launcher_title_button',driver)
        self.check_exists(self.appPackage+':id/button_todoschool',driver)
        self.check_exists(self.appPackage+':id/button_library',driver)
        self.check_exists(self.appPackage+':id/button_tool',driver)
        self.check_exists(self.appPackage+':id/imageView_coin',driver)
        itr = 1
        # Launcher Main Screen
        for itr in range(3):
            points = self.find_matches(driver,os.path.join(testingOperationObject.template,'')+str(itr+1)+'.png')
            
        self.click_elements(points,driver)
        sleep(2)
        # Tools Section
        for itr in range(8):
            points = self.find_matches(driver,os.path.join(self.template,'toolSection','')+str(itr+1)+'.png')
            self.click_elements(points,driver)
            sleep(1)
            
            for itr2 in range(toolSection[itr]):
                points = self.find_matches(driver,os.path.join(self.template,'toolSection',str(itr+1),'')+str(itr2+1)+'.png')
                self.click_elements(points,driver)
                sleep(1)
            if itr < 5:
                self.toolsCocosBackButton(driver)

if __name__ == "__main__":
    testingOperationObject = testingOperation(sys.argv[1],sys.argv[2],__file__,1).main()
	
