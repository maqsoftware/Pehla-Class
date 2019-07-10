import os
import cv2
from time import sleep
from appium import webdriver
import appium.webdriver.extensions
from pathlib import Path
import numpy as np
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import sys
import KitkitSchool

# screen have same element size but screen apperarence depend on screen's physical size
if __name__ == "__main__":
    noreset = 'true'
    testingOperationObject = KitkitSchool.testingOperation(sys.argv[1],sys.argv[2],__file__,30)
    driver = testingOperationObject.connect(noreset)
    sleep(2)
    result = testingOperationObject.allow_permission(driver)

    if result or noreset == 'true':
        points,result = testingOperationObject.find_matches(driver,os.path.join(testingOperationObject.template,'')+'2.png')
        testingOperationObject.click_elements(points,driver)        
        if result or noreset == 'true':
            sleep(8)
            result =testingOperationObject.allow_permission(driver)
            sleep(2)
            result =testingOperationObject.wait_for_extraction(driver)
            sleep(8)
            # if result or noreset == 'true':
            #     points,result = testingOperationObject.library_find_matches(driver,os.path.join(testingOperationObject.template,'librarySection','')+'1.png')
            #     testingOperationObject.click_elements(points,driver)
            #     if result or noreset == 'true':
            #         for x in range(9): 
            #             sleep(2)
            #             points,result = testingOperationObject.library_find_matches(driver,os.path.join(testingOperationObject.template,r'librarySection\videoSection','')+str(x+1)+'.png')
            #             testingOperationObject.click_elements(points,driver)
            #             sleep(6)
            #             if result :
            #                 testingOperationObject.backButton(driver)
            #             print("scrolling")
            #             sleep(2)
            #             testingOperationObject.swipeScreen(driver,1000,800,70,800)   
            #         for x in range(6):
            #             sleep(2)
            #             print("scrolling")
            #             testingOperationObject.swipeScreen(driver,800,1130,800,100)
            #             points,result = testingOperationObject.library_find_matches(driver,os.path.join(testingOperationObject.template,r'librarySection\videoSection','')+str(x+10)+'.png')
            #             testingOperationObject.click_elements(points,driver)
            #             sleep(6)
            #             if result :
            #                 points,result = testingOperationObject.library_find_matches(driver,os.path.join(testingOperationObject.template,r'librarySection','')+'back.png')
            #                 testingOperationObject.click_elements(points,driver)
            #                 if not result:
            #                     driver.back()

            #         # press back arrow
            #         sleep(2)
            #         points,result = testingOperationObject.library_find_matches(driver,os.path.join(testingOperationObject.template,r'librarySection','')+'back.png')
            #         testingOperationObject.click_elements(points,driver)
            #         sleep(2)
            #         if not result:
            #             driver.back()
        points,result = testingOperationObject.library_find_matches(driver,os.path.join(testingOperationObject.template,'librarySection','')+'2.png')
        testingOperationObject.click_elements(points,driver)


        if result:
            for x in range(20):
                sleep(2) 
                points,result = testingOperationObject.library_find_matches(driver,os.path.join(testingOperationObject.template,r'librarySection\storySection','')+str(x+1)+'.png')
                testingOperationObject.click_elements(points,driver)
                sleep(6)
                if result:
                    points,result = testingOperationObject.library_find_matches(driver,os.path.join(testingOperationObject.template,r'librarySection\storySection','')+'back.png')
                    testingOperationObject.click_elements(points,driver)
                    if not result:
                        driver.back()
                print("scrolling right")
                sleep(3)
                testingOperationObject.swipeScreen(driver,600,800,100,800)
            for x in range(6):
                sleep(3)
                print("scrolling down")
                testingOperationObject.swipeScreen(driver,800,1060,800,240)
                points,result = testingOperationObject.library_find_matches(driver,os.path.join(testingOperationObject.template,r'librarySection\storySection','')+str(x+21)+'.png')
                testingOperationObject.click_elements(points,driver)
                sleep(6)
                if result:
                    points,result = testingOperationObject.library_find_matches(driver,os.path.join(testingOperationObject.template,r'librarySection\storySection','')+'back.png')
                    testingOperationObject.click_elements(points,driver)
                    if not result:
                        driver.back()
            # exit library
            points,result = testingOperationObject.library_find_matches(driver,os.path.join(testingOperationObject.template,r'librarySection','')+'back.png')
            testingOperationObject.click_elements(points,driver)
            if not result:
                driver.back()
            points,result = testingOperationObject.library_find_matches(driver,os.path.join(testingOperationObject.template,r'librarySection','')+'back.png')
            testingOperationObject.click_elements(points,driver)
            if not result:
                driver.back()
    sleep(2)
    driver.close_app()


