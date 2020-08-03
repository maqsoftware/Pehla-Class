import onebillion
import cv2 
import numpy as np 
import os
import sys
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException


if __name__ == "__main__":
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    # create an object of onebillion class passing device id,port,current file,intial test case number 
    testingOpernationInstance = onebillion.testingOperation(arg1,arg2,__file__,10)
    
    driver = testingOpernationInstance.connect('true')
    sleep(8)

    driver.save_screenshot(testingOpernationInstance.test+r"\main_games_scr.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_active_treasure.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(12)


    ################# Bird Game #######################################
    driver.save_screenshot(testingOpernationInstance.test+r"\play_ground.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_playground_bird.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(8)

    driver.save_screenshot(testingOpernationInstance.test+r"\playground_birdgame.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\play_ground_bird_scr.png")
    sleep(2)

    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\play_ground_bird_scr_1.png")
    sleep(8)

    driver.save_screenshot(testingOpernationInstance.test+r"\playground_birdgame.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_playground_birdgame_audio.png")
    sleep(8)

    driver.save_screenshot(testingOpernationInstance.test+r"\playground_birdgame.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_playground_birdgame_bird.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(5)

    driver.save_screenshot(testingOpernationInstance.test+r"\playground_birdgame.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_playground_birdgame_back.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(5)

    driver.save_screenshot(testingOpernationInstance.test+r"\playground.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_playground_back.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(10)

    driver.save_screenshot(testingOpernationInstance.test+r"\main_games_scr.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_active_treasure.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(10)
    

        ################## Draw Game #######################################
    driver.save_screenshot(testingOpernationInstance.test+r"\playground.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_playground_draw.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(8)
   
    driver.save_screenshot(testingOpernationInstance.test+r"\playground_drawgame.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_playground_drawgame_theme.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(8)
    
    driver.save_screenshot(testingOpernationInstance.test+r"\playground_drawgame.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\play_ground_draw_scr.png")
    sleep(8)

    driver.save_screenshot(testingOpernationInstance.test+r"\playground_drawgame.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_playground_drawgame_savechang.png")
    # testingOpernationInstance.click_elements(points,driver)
    sleep(8)
 
    driver.save_screenshot(testingOpernationInstance.test+r"\playground_drawgame.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_playground_birdgame_back.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(8)

    ################## video Game #######################################
    driver.save_screenshot(testingOpernationInstance.test+r"\playground.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_playground_video.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(8)
    
    driver.save_screenshot(testingOpernationInstance.test+r"\playground_videogame.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_playground_video_monkey.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(8)

    driver.save_screenshot(testingOpernationInstance.test+r"\playground_videogame.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\play_ground_video_scr.png")
    sleep(8)

    driver.save_screenshot(testingOpernationInstance.test+r"\playground_videogame_monk.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_playground_videogame_back.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(8)



     ##################  Story Section #######################################
    driver.save_screenshot(testingOpernationInstance.test+r"\playground.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_playground_story.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(8)

    driver.save_screenshot(testingOpernationInstance.test+r"\playground_story_section.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\play_ground_story_scr_1.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(8)

    driver.save_screenshot(testingOpernationInstance.test+r"\playground_story.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_playground_videogame_back.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(8)

    driver.save_screenshot(testingOpernationInstance.test+r"\playground_story_section.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_playground_videogame_back.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(8)

     ##################  Number Game #######################################
    sleep(10)

    driver.save_screenshot(testingOpernationInstance.test+r"\playground.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\pixeltab_playground_number.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(8)
    
    driver.save_screenshot(testingOpernationInstance.test+r"\playground_numbergame.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\play_ground_number_scr.png")
    sleep(8)

    driver.save_screenshot(testingOpernationInstance.test+r"\playground_number_game.png")
    points = testingOpernationInstance.find_matches(driver, testingOpernationInstance.template+r"\game_sound_blue.png")
    # testingOpernationInstance.click_elements(points,driver)
    sleep(8)

    testingOpernationInstance.exit_application(driver)
    sleep(10)
    print("Done Testing Play Ground")
    os.system("adb -s "+testingOpernationInstance.udid+" uninstall "+testingOpernationInstance.appPackage)
    
    
   
    





















 
   