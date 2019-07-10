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
    # base template device resolution 
    base_w = 2560
    base_h = 1440
    base_dpi_w = 537.882
    base_dpi_h = 532.983
    dpi_w = 0.0
    dpi_h = 0.0
    def __init__(self,udId,port,file,id):
        self.count = id
        self.udid = udId
        self.platformName = 'Android'
        self.deviceName = 'Device'
        self.appPackage = 'com.maq.xprize.kitkitschool.hindi'
        self.appActivity = 'org.cocos2dx.cpp.kitkitlauncher.hindi.MainActivity'
        self.url = 'http://localhost:'+port+'/wd/hub'
        self.base = os.path.dirname(os.path.realpath(file))
        self.output = os.path.join(self.base,'results',udId)+r"\outputs"
        self.template = self.base+r"\images\templates"
        self.test = os.path.join(self.base,'results',udId)+r"\tests"
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
            print("Pass")
            
        except NoSuchElementException:
            print("Fail")
        self.count+=1

    #wait extracting 
    def wait_for_extraction(self,driver):
        val = self.check_exists1('com.maq.xprize.booktest:id/p',driver)
        while self.check_exists1('com.maq.xprize.booktest:id/p',driver):
            print('Waiting extraction')
            sleep(30)
        return val
    #allow permission
    def allow_permission(self,driver):
        sleep(2)
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

    #match template function
    def find_matches(self,driver, template):
        driver.save_screenshot(self.test+r"\currentScreen.png")
        threshold = 0.6
        temp = cv2.imread(template)
        screen = cv2.imread(self.test+r"\currentScreen.png")
        a,sw,sh = screen.shape[::-1]
        a,w, h = temp.shape[::-1]
        h = int(h * sh/self.base_h)
        w = int(w  *sw/self.base_w)
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
            return points,True
        except IndexError:
            driver.save_screenshot(self.output+r"\output_t"+str(self.count)+r".png")
            print("Fail")
            self.count+=1
            return [(-1,-1)],False

    
    #match template function
    def library_find_matches(self,driver, template):
        driver.save_screenshot(self.test+r"\currentScreen.png")
        threshold = 0.6
        temp = cv2.imread(template)
        screen = cv2.imread(self.test+r"\currentScreen.png")
        a,w, h = temp.shape[::-1]
        h = int(h * self.dpi_h/self.base_dpi_h)
        w = int(w  *self.dpi_w/self.base_dpi_w)
        if float(self.dpi_h/self.base_dpi_h) == float(self.dpi_w/self.base_dpi_w) and  float(self.dpi_h/self.base_dpi_h) == 1.0:
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
            return points,True
        except IndexError:
            driver.save_screenshot(self.output+r"\output_t"+str(self.count)+r".png")
            print("Fail")
            self.count+=1
            return [(-1,-1)],False

    def checkElementByImage(self,driver, template):
        driver.save_screenshot(self.test+r"\currentScreen.png")
        threshold = 0.69
        temp = cv2.imread(template)
        screen = cv2.imread(self.test+r"\currentScreen.png")
        a,sw,sh = screen.shape[::-1]
        a,w, h = temp.shape[::-1]
        h = int(h * sh/self.base_h)
        w = int(w  *sw/self.base_w)
        if float(sh/self.base_h) == float(sw/self.base_w) and  float(sh/self.base_h) == 1.0:
            threshold = 0.8
        temp = cv2.resize(temp, (w,h))
        res = cv2.matchTemplate(screen,temp,cv2.TM_CCOEFF_NORMED)  # @UndefinedVariable
        loc = np.where( res >= threshold )
        try:
            temp = loc[0][0]
            return True
        except IndexError:
            return False

    def backButton(self,driver):
        driver.save_screenshot(self.output+r"\output_t"+str(self.count)+r".png")
        self.count+=1
        print("Pass")
        sleep(1)
        driver.back()

    def libraryCocosBackButton(self,driver):
        driver.save_screenshot(self.output+r"\output_t"+str(self.count)+r".png")
        self.count+=1
        print("Pass")
        driver.find_element_by_id('com.maq.xprize.kitkitlibrary.english:id/v_back').click()
        sleep(1)

    def mainappCocosBackButton(self,driver):
        driver.save_screenshot(self.output+r"\output_t"+str(self.count)+r".png")
        self.count+=1
        print("Pass")
        driver.find_element_by_id('com.maq.xprize.kitkitschool.hindi:id/v_back').click()
        sleep(1)
        
    def clickById(self,driver,id):
        driver.save_screenshot(self.output+r"\output_t"+str(self.count)+r".png")
        self.count+=1
        print("Pass")
        driver.find_element_by_id(id).click()
        sleep(1)
    
    def swipeScreen(self,driver,x1,y1,x2,y2):
        screen = cv2.imread(self.test+r"\currentScreen.png")
        a,sw,sh = screen.shape[::-1]
        h = self.dpi_h/self.base_dpi_h
        w = self.dpi_w/self.base_dpi_w
        driver.swipe(int(x1*w), int(y1*h), int(x2*w), int(y2*h))
        sleep(2)

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
   
    def coinIcon(self,driver):
        points = self.find_matches(driver,self.template+r"\coin.png")
    def main(self):
        toolSection=[1,1,2,2,3,1,0,0]
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        driver=self.connect('true')
		# Kitkit launcher starts
        # allow permission
        self.allow_permission(driver)
        sleep(2)
        driver.save_screenshot(self.test+r"\mainscreen.png")
        # check screen loaded
        sleep(2)
        driver.save_screenshot(self.output+r"\output_t"+str(self.count)+r".png")
        self.count+=1
        self.check_exists('com.maq.xprize.kitkitschool.hindi:id/launcher_title_button',driver)
        self.check_exists('com.maq.xprize.kitkitschool.hindi:id/button_todoschool',driver)
        self.check_exists('com.maq.xprize.kitkitschool.hindi:id/button_library',driver)
        self.check_exists('com.maq.xprize.kitkitschool.hindi:id/button_tool',driver)
        self.check_exists('com.maq.xprize.kitkitschool.hindi:id/imageView_coin',driver)
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
                self.mainappCocosBackButton(driver)
if __name__ == "__main__":
    testingOperationObject = testingOperation(sys.argv[1],sys.argv[2],__file__,1).main()
	
