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


if __name__ == "__main__":
    # mainappMenu = [[6, 10, 28, 29, 33, 29, 31, 31, 31, 31, 26], [6, 17, 18, 29, 22, 29, 29, 29, 29, 29, 29]]
    mainappMenu = [[6, 0, 0, 29, 33, 29, 31, 31, 31, 31, 26], [6, 17, 18, 29, 22, 29, 29, 29, 29, 29, 29]]
    gamesNumber = [[[3, 3, 3, 3, 3, 6], 
					 [5, 5, 5, 5, 5, 5, 5, 5, 1, 8], 
					 [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 8], 
					 [4, 4, 4, 4, 5, 4, 4, 4, 5, 4, 4, 4, 5, 4, 5, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 14], 
					 [5, 4, 5, 4, 5, 4, 5, 1, 4, 5, 4, 5, 5, 5, 5, 1, 4, 4, 4, 4, 4, 5, 4, 1, 5, 4, 4, 5, 4, 5, 4, 1, 14],
					 [5, 4, 5, 4, 5, 4, 1, 5, 4, 5, 4, 5, 4, 1, 4, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 1],
					 [4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 4, 1],
					 [4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 4, 1],
					 [4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 4, 1],
					 [4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 4, 1]],
					[[3, 4, 4, 3, 4],
					 [5, 4, 5, 4, 4, 4, 5, 4, 5, 4, 5, 5, 5, 4, 5, 1],
					 [5, 4, 5, 5, 5, 4, 5, 4, 5, 5, 4, 5, 5, 5, 5, 5, 1],
					 [5, 5, 5, 6, 5, 6, 1, 6, 6, 5, 5, 5, 6, 1, 6, 6, 5, 5, 6, 5, 1, 5, 5, 6, 5, 5, 5, 1],
					 [5, 5, 5, 5, 5, 4, 1, 5, 5, 5, 5, 5, 4, 1, 5, 5, 5, 5, 5, 5, 1],
					 [5, 5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5, 5, 1, 5, 4, 5, 5, 5, 5, 1],
					 [5, 5, 6, 5, 5, 5, 1, 5, 6, 5, 6, 5, 5, 1, 5, 5, 5, 5, 5, 6, 1, 5, 5, 4, 5, 5, 5, 1],
					 [5, 5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5, 5, 1],
					 [5, 5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5, 5, 1],
					 [5, 5, 5, 5, 5, 4, 1, 5, 5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5, 5, 1]]]

    noreset = 'true'
    testingOperationObject = KitkitSchool.testingOperation(sys.argv[1],sys.argv[2],__file__,30)
    driver = testingOperationObject.connect(noreset)
    sleep(2)
    
    result = testingOperationObject.allow_permission(driver)

    if result or noreset == 'true':
        points,result = testingOperationObject.find_matches(driver,os.path.join(testingOperationObject.template,'')+'1.png')
        testingOperationObject.click_elements(points,driver)
        
        if result or noreset == 'true':
            sleep(8)
            result =testingOperationObject.allow_permission(driver)
            sleep(2)
            if result or noreset == 'true':
                result =testingOperationObject.wait_for_extraction(driver)
                if result or noreset == 'true':
                    print("Extraction done")
                    sleep(30)
                    mainappPath = os.path.join(testingOperationObject.template,'mainapp','')
                    for menu in range(2):
                        sleep(2)
                        points,result = testingOperationObject.find_matches(driver,mainappPath+str(menu+1)+'.png')
                        testingOperationObject.click_elements(points,driver)
                        sleep(4)
                        if result:
                            sectionNumberPath = os.path.join(mainappPath,str(menu+1),'')	
                            for section in range(11):
                                if section == 0:
                                    sleep(5)
                                sleep(2)
                                points,result = testingOperationObject.find_matches(driver,sectionNumberPath+str(section+1)+'.png')
                                testingOperationObject.click_elements(points,driver)
                                if result:
                                    subSectionPath = os.path.join(sectionNumberPath,str(menu+1)+'_'+str(section+1),'')
                                    for subSection in range(mainappMenu[menu][section]):
                                    # subSection = mainappMenu[menu][section] -1
                                        sleep(2)
                                        points,result = testingOperationObject.find_matches(driver,subSectionPath+str(subSection+1)+'.png')
                                        testingOperationObject.click_elements(points,driver)
                                        if result:
                                            gamePath = os.path.join(subSectionPath,str(menu+1)+'_'+str(section+1)+'_'+str(subSection+1),'') 
                                            if not testingOperationObject.isTablet or subSection < mainappMenu[menu][section] -1:
                                                for game in range(gamesNumber[menu][section][subSection]):

                                                    sleep(2)
                                                    points,result = testingOperationObject.find_matches(driver,gamePath+str(game+1)+'.png')
                                                    testingOperationObject.click_elements(points,driver)
                                                    sleep(6)
                                                    if testingOperationObject.check_tutorials(driver) and subSection < mainappMenu[menu][section] -1:
                                                        sleep(16)
                                                    else:
                                                        sleep(2)
                                                    if result:
                                                        # check if it was video module or not
                                                        if testingOperationObject.checkElementByImage(driver,testingOperationObject.template+r"\tick.png"):
                                                            points,result = testingOperationObject.find_matches(driver,testingOperationObject.template+r"\tick.png")
                                                            testingOperationObject.click_elements(points,driver)
                                                            if not result:
                                                                driver.back()
                                                            sleep(1)
                                                        elif subSection == mainappMenu[menu][section] -1 and game%2 == 1:
                                                            points,result = testingOperationObject.find_matches(driver,gamePath+'close.png')
                                                            testingOperationObject.click_elements(points,driver)
                                                            if not result:
                                                                driver.back()
                                                        elif subSection == mainappMenu[menu][section] -1 and game%2 == 0:
                                                            continue
                                                        else :
                                                            points,result = testingOperationObject.find_matches(driver,testingOperationObject.template+r'\back.png')
                                                            testingOperationObject.click_elements(points,driver)
                                                            if not result:
                                                                driver.back()
                                                            sleep(1)
                                            sleep(2)
                                            if subSection == mainappMenu[menu][section] -1:
                                                points,result = testingOperationObject.find_matches(driver,gamePath+'down.png')
                                                testingOperationObject.click_elements(points,driver)
                                                if not result:
                                                    driver.back()
                                            else:    
                                                points,result = testingOperationObject.find_matches(driver,testingOperationObject.template+r'\back.png')
                                                testingOperationObject.click_elements(points,driver)
                                                if not result:
                                                    driver.back()
                                    points,result = testingOperationObject.find_matches(driver,testingOperationObject.template+r'\back.png')
                                    testingOperationObject.click_elements(points,driver)
                                    if not result:
                                        driver.back()
                            points,result = testingOperationObject.find_matches(driver,testingOperationObject.template+r'\back.png')
                            testingOperationObject.click_elements(points,driver)
                            if not result:
                                driver.back()
    sleep(2)        
    driver.close_app()

					


    
    
    # C:\Users\MAQUser\Desktop\scripts\Screen shots\cropedObject\mainapp
    # os.path.join(testingOperationObject.template,'mainScreen','')