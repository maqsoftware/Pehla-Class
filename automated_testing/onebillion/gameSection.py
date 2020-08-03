import onebillion
import cv2 
import numpy as np 
import os
import time 
import sys
from time import sleep
from appium import webdriver
from pathlib import Path
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException



    
if __name__ == "__main__":  
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    # create an object of onebillion class passing device id,port,current file,intial test case number 
    testingOpernationInstance = onebillion.testingOperation(arg1,arg2,__file__,34)

    driver =testingOpernationInstance.connect('true')

    sleep(6)
    
    
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_game1.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(6)

    driver.save_screenshot(testingOpernationInstance.test+r"\game1.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game_sound_white.png")
    # testingOpernationInstance.click_elements(points,driver)

    sleep(2)
    driver.save_screenshot(testingOpernationInstance.test+r"\game1.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game1_scr.png")

    sleep(2)
    print("Done Testing 1")
    
    # exit application
    testingOpernationInstance.exit_application(driver)
    sleep(2)
    # connect to applicationdriv
    driver = testingOpernationInstance.connect('true')

    driver.save_screenshot(testingOpernationInstance.test+r"\main_games_scr.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_game2.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(6)

    driver.save_screenshot(testingOpernationInstance.test+r"\game2.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game_sound_blue.png")
    # testingOpernationInstance.click_elements(points,driver)
    sleep(2)

    driver.save_screenshot(testingOpernationInstance.test+r"\game2.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game2_scr.png")
    sleep(2)

    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game2_scr_2.png")
    sleep(2)
    
    print("Done Testing 2")

    # exit application
    testingOpernationInstance.exit_application(driver)
    sleep(2)
    # connect to application
    driver = testingOpernationInstance.connect('true')  
    sleep(6)

    driver.save_screenshot(testingOpernationInstance.test+r"\main_games_scr.png")
    sleep(2)

    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_game3.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(6)
    
    driver.save_screenshot(testingOpernationInstance.test+r"\game3.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game_sound_white.png")
    # testingOpernationInstance.click_elements(points,driver)
    sleep(2)

    driver.save_screenshot(testingOpernationInstance.test+r"\game3.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game3_scr.png")
    sleep(2)

    print("Done Testing 3")

    # exit application
    testingOpernationInstance.exit_application(driver)
    sleep(2)
    # connect to application
    driver = testingOpernationInstance.connect('true')  
    sleep(6)

    driver.save_screenshot(testingOpernationInstance.test+r"\main_games_scr.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_game4.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(6)
    
    driver.save_screenshot(testingOpernationInstance.test+r"\game4.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game_sound_white.png")
    # testingOpernationInstance.click_elements(points,driver)
    sleep(2)

    driver.save_screenshot(testingOpernationInstance.test+r"\game4.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game4_scr.png")
    sleep(2)
    print("Done Testing 4")

    # exit application
    testingOpernationInstance.exit_application(driver)
    sleep(2)
    # connect to application
    driver = testingOpernationInstance.connect('true') 
    sleep(6)

    driver.save_screenshot(testingOpernationInstance.test+r"\main_games_scr.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_game5.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(6)

    driver.save_screenshot(testingOpernationInstance.test+r"\game5.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game_sound_white.png")
    # testingOpernationInstance.click_elements(points,driver)
    sleep(4)

    driver.save_screenshot(testingOpernationInstance.test+r"\game5.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game5_scr.png")
    sleep(4)

    print("Done Testing 5")

    # exit application
    testingOpernationInstance.exit_application(driver)
    sleep(2)
    # connect to application
    driver = testingOpernationInstance.connect('true')
    sleep(6)

    driver.save_screenshot(testingOpernationInstance.test+r"\main_games_scr.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_game6.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(6)

    

    driver.save_screenshot(testingOpernationInstance.test+r"\game6.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game_sound_white.png")
    # testingOpernationInstance.click_elements(points,driver)
    sleep(2)

    driver.save_screenshot(testingOpernationInstance.test+r"\game6.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game6_scr.png")
    sleep(2)

    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game6_scr_1.png")
    sleep(2)
    
    print("Done Testing 6")

    # exit application
    testingOpernationInstance.exit_application(driver)
    sleep(2)
    # connect to application
    driver = testingOpernationInstance.connect('true')
    sleep(6)

    driver.save_screenshot(testingOpernationInstance.test+r"\main_games_scr.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_game7.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(6)
    
    driver.save_screenshot(testingOpernationInstance.test+r"\game7.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game_sound_white.png")
    # testingOpernationInstance.click_elements(points,driver)
    sleep(4)

    driver.save_screenshot(testingOpernationInstance.test+r"\game7.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game7_scr.png")
    sleep(4)
    print("Done Testing 7")

    # exit application
    testingOpernationInstance.exit_application(driver)
    sleep(2)
    # connect to application
    driver = testingOpernationInstance.connect('true')
    sleep(6)

    driver.save_screenshot(testingOpernationInstance.test+r"\main_games_scr.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_game8.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(6)

    driver.save_screenshot(testingOpernationInstance.test+r"\game8.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game_sound_white.png")
    # testingOpernationInstance.click_elements(points,driver)
    sleep(2)

    driver.save_screenshot(testingOpernationInstance.test+r"\game8.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game8_scr.png")
    sleep(2)

    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game8_scr_1.png")
    sleep(2)

    print("Done Testing 8")

    # exit application
    testingOpernationInstance.exit_application(driver)
    sleep(2)
    # connect to application
    driver = testingOpernationInstance.connect('true')
    sleep(6)

    driver.save_screenshot(testingOpernationInstance.test+r"\main_games_scr.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_game9.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(6)

    driver.save_screenshot(testingOpernationInstance.test+r"\game9.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game_sound_white.png")
    sleep(2)

    driver.save_screenshot(testingOpernationInstance.test+r"\game9.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game9_scr.png")
    sleep(2)

    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game9_scr_1.png")
    sleep(2)

    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game9_scr_2.png")
    sleep(2)

    print("Done Testing 9")

    # exit application
    testingOpernationInstance.exit_application(driver)
    sleep(2)
    # connect to application
    driver = testingOpernationInstance.connect('true')
    sleep(6)

    driver.save_screenshot(testingOpernationInstance.test+r"\main_games_scr.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_game10.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(6)

    driver.save_screenshot(testingOpernationInstance.test+r"\game10.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game_sound_white.png")
    sleep(2)

    driver.save_screenshot(testingOpernationInstance.test+r"\game10.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game10_scr.png")
    sleep(2)

    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game10_scr_1.png")
    sleep(2)

    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game10_scr_2.png")
    sleep(2)

    print("Done Testing 10")

    # exit application
    testingOpernationInstance.exit_application(driver)
    sleep(2)
    # connect to application
    driver = testingOpernationInstance.connect('true')
    sleep(6)

    driver.save_screenshot(testingOpernationInstance.test+r"\main_games_scr.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_game11.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(6)
   
    driver.save_screenshot(testingOpernationInstance.test+r"\game11.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game_sound_white.png")
    # testingOpernationInstance.click_elements(points,driver)
    sleep(2)

    driver.save_screenshot(testingOpernationInstance.test+r"\game11.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game11_scr.png")
    sleep(2)

    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game11_scr_1.png")
    sleep(2)

    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game11_scr_2.png")
    sleep(2)

    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game11_scr_3.png")
    sleep(2)

    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game11_scr_4.png")
    sleep(2)

    print("Done Testing 11")

    # exit application
    testingOpernationInstance.exit_application(driver)
    sleep(2)
    # connect to application
    driver = testingOpernationInstance.connect('true')
    sleep(6)

    driver.save_screenshot(testingOpernationInstance.test+r"\main_games_scr.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_game12.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(6)

    driver.save_screenshot(testingOpernationInstance.test+r"\game12.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game_sound_white.png")
    # testingOpernationInstance.click_elements(points,driver)
    sleep(2)

    driver.save_screenshot(testingOpernationInstance.test+r"\game12.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game12_scr.png")
    sleep(2)

    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game12_scr_1.png")
    sleep(2)

    print("Done Testing 12")

    # exit application
    testingOpernationInstance.exit_application(driver)
    sleep(2)
    # connect to application
    driver = testingOpernationInstance.connect('true')
    sleep(6)

    driver.save_screenshot(testingOpernationInstance.test+r"\main_games_scr.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_game13.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(11)

    driver.save_screenshot(testingOpernationInstance.test+r"\game13.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game_sound_white.png")
    # testingOpernationInstance.click_elements(points,driver)
    sleep(2)

    driver.save_screenshot(testingOpernationInstance.test+r"\game13.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game13_scr.png")
    sleep(2)

    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game13_scr_2.png")
    sleep(2)

    print("Done Testing 13")

    # exit application
    testingOpernationInstance.exit_application(driver)
    sleep(2)
    # connect to application
    driver = testingOpernationInstance.connect('true')
    sleep(6)

    driver.save_screenshot(testingOpernationInstance.test+r"\main_games_scr.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_game14.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(6)

    driver.save_screenshot(testingOpernationInstance.test+r"\game14.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game14_sound.png")
    # testingOpernationInstance.click_elements(points,driver)
    sleep(2)

    driver.save_screenshot(testingOpernationInstance.test+r"\game14.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game14_scr.png")
    sleep(2)

    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game14_scr_1.png")
    sleep(2)

    print("Done Testing 14")

    # exit application
    testingOpernationInstance.exit_application(driver)
    sleep(2)
    # connect to application
    driver = testingOpernationInstance.connect('true')
    sleep(6)

    driver.save_screenshot(testingOpernationInstance.test+r"\main_games_scr.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_game15.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(6)
   
    driver.save_screenshot(testingOpernationInstance.test+r"\game15.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game_sound_white.png")
    # testingOpernationInstance.click_elements(points,driver)
    sleep(2)

    driver.save_screenshot(testingOpernationInstance.test+r"\game15.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game15_scr.png")
    sleep(2)

    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game15_scr_1.png")
    sleep(2)
    
    print("Done Testing 15")
    print("Done Testing Game Section")

    # exit application
    testingOpernationInstance.exit_application(driver)
    sleep(2)
    # connect to application
    os.system(r"python "+testingOpernationInstance.base+ r"\playGround.py "+arg1+" "+arg2)
 