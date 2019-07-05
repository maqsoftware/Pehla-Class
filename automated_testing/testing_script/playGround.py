import waitExtraction
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
    testingOpernationInstance = waitExtraction.testingOperation(arg1,arg2,__file__,10)
    
    driver = testingOpernationInstance.connect('true')
    sleep(8)
    driver.save_screenshot(testingOpernationInstance.test+r"\main_games_scr.png")
    points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\main_games_scr.png",testingOpernationInstance.template+r"\pixeltab_active_treasure.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(12)
    # driver.save_screenshot(testingOpernationInstance.output+r"\outputs\play_ground_ss.png")


    ################# Bird Game #######################################
    driver.save_screenshot(testingOpernationInstance.test+r"\play_ground.png")
    points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\play_ground.png",testingOpernationInstance.template+r"\pixeltab_playground_bird.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(8)
    # driver.save_screenshot(testingOpernationInstance.output+r"\outputs\playground_birdgame_ss.png")

    sleep(8)
    driver.save_screenshot(testingOpernationInstance.test+r"\playground_birdgame.png")
    points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground_birdgame.png",testingOpernationInstance.template+r"\play_ground_bird_scr.png")
    # testingOpernationInstance.click_elements(points,driver)
    sleep(2)
    points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground_birdgame.png",testingOpernationInstance.template+r"\play_ground_bird_scr_1.png")
    sleep(8)
    driver.save_screenshot(testingOpernationInstance.test+r"\playground_birdgame.png")
    points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground_birdgame.png",testingOpernationInstance.template+r"\pixeltab_playground_birdgame_audio.png")
    # testingOpernationInstance.click_elements(points,driver)
    
    sleep(8)
    driver.save_screenshot(testingOpernationInstance.test+r"\playground_birdgame.png")
    points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground_birdgame.png",testingOpernationInstance.template+r"\pixeltab_playground_birdgame_bird.png")
    testingOpernationInstance.click_elements(points,driver)
    # driver.save_screenshot(testingOpernationInstance.output+r"\outputs\playground_birdfly_ss.png")
    sleep(5)
    driver.save_screenshot(testingOpernationInstance.test+r"\playground_birdgame.png")
    points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground_birdgame.png",testingOpernationInstance.template+r"\pixeltab_playground_birdgame_back.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(5)
    driver.save_screenshot(testingOpernationInstance.test+r"\playground.png")
    points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground.png",testingOpernationInstance.template+r"\pixeltab_playground_back.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(10)
    # driver.save_screenshot(testingOpernationInstance.output+r"\main_games_ss.png")

    driver.save_screenshot(testingOpernationInstance.test+r"\main_games_scr.png")
    points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\main_games_scr.png",testingOpernationInstance.template+r"\pixeltab_active_treasure.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(10)
    # driver.save_screenshot(testingOpernationInstance.output+r"\play_ground_ss1.png")
    
        ################## Draw Game #######################################
    driver.save_screenshot(testingOpernationInstance.test+r"\playground.png")
    points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground.png",testingOpernationInstance.template+r"\pixeltab_playground_draw.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(8)
    # driver.save_screenshot(testingOpernationInstance.output+r"\drawgame_ss.png")
    
    
    driver.save_screenshot(testingOpernationInstance.test+r"\playground_drawgame.png")
    points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground_drawgame.png",testingOpernationInstance.template+r"\pixeltab_playground_drawgame_theme.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(8)
    # driver.save_screenshot(testingOpernationInstance.output+r"\drawgame_theme2_ss.png")

    sleep(8)
    driver.save_screenshot(testingOpernationInstance.test+r"\playground_drawgame.png")
    points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground_drawgame.png",testingOpernationInstance.template+r"\play_ground_draw_scr.png")


    driver.save_screenshot(testingOpernationInstance.test+r"\playground_drawgame.png")
    points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground_drawgame.png",testingOpernationInstance.template+r"\pixeltab_playground_drawgame_savechang.png")
    # testingOpernationInstance.click_elements(points,driver)
    sleep(8)
    # driver.save_screenshot(testingOpernationInstance.output+r"\drawgame_save_ss.png")
    
    
    # driver.save_screenshot(testingOpernationInstance.test+r"\playground.png")
    # points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground.png",testingOpernationInstance.template+r"\pixeltab_playground_draw.png")
    # testingOpernationInstance.click_elements(points,driver)
    # sleep(8)
    # driver.save_screenshot(testingOpernationInstance.output+r"\drawgame_ss.png")

    driver.save_screenshot(testingOpernationInstance.test+r"\playground_drawgame.png")
    points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground_drawgame.png",testingOpernationInstance.template+r"\pixeltab_playground_birdgame_back.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(8)
    # driver.save_screenshot(testingOpernationInstance.output+r"\play_ground_ss.png")

    ################## video Game #######################################
    driver.save_screenshot(testingOpernationInstance.test+r"\playground.png")
    points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground.png",testingOpernationInstance.template+r"\pixeltab_playground_video.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(8)
    # driver.save_screenshot(testingOpernationInstance.output+r"\videogame_ss.png")
    

    driver.save_screenshot(testingOpernationInstance.test+r"\playground_videogame.png")
    points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground_videogame.png",testingOpernationInstance.template+r"\pixeltab_playground_video_monkey.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(8)
    # driver.save_screenshot(testingOpernationInstance.output+r"\videogame_monkey_ss.png")

    sleep(8)
    driver.save_screenshot(testingOpernationInstance.test+r"\playground_videogame.png")
    points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground_videogame.png",testingOpernationInstance.template+r"\play_ground_video_scr.png")

    driver.save_screenshot(testingOpernationInstance.test+r"\playground_videogame_monk.png")
    points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground_videogame_monk.png",testingOpernationInstance.template+r"\pixeltab_playground_videogame_back.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(8)
    # driver.save_screenshot(testingOpernationInstance.output+r"\play_ground_ss.png")

    # ################  Video Recording #######################################
    # driver.save_screenshot(testingOpernationInstance.test+r"\playground.png")
    # points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground.png",testingOpernationInstance.template+r"\pixeltab_playground_camera.png")
    # testingOpernationInstance.click_elements(points,driver)
    # sleep(8)
    # # driver.save_screenshot(testingOpernationInstance.output+r"\videorecording_ss.png")
    
    # driver.save_screenshot(testingOpernationInstance.test+r"\playground_camerasection.png")
    # points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground_camerasection.png",testingOpernationInstance.template+r"\pixeltab_playground_camera_rotate.png")
    # # testingOpernationInstance.click_elements(points,driver)
    # sleep(8)
    # # driver.save_screenshot(testingOpernationInstance.output+r"\videorecording_rot_ss.png")

    
    # driver.save_screenshot(testingOpernationInstance.test+r"\playground_camerasection.png")
    # points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground_camerasection.png",testingOpernationInstance.template+r"\pixeltab_playground_camera_record.png")
    # testingOpernationInstance.click_elements(points,driver)
    # sleep(4)
    # # driver.save_screenshot(testingOpernationInstance.output+r"\videorecording_record_ss.png")
    # sleep(8)
    # # driver.save_screenshot(testingOpernationInstance.output+r"\play_ground_record_ss.png")

    # driver.save_screenshot(testingOpernationInstance.test+r"\playground.png")
    # points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground.png",testingOpernationInstance.template+r"\pixeltab_playground_camera.png")
    # testingOpernationInstance.click_elements(points,driver)
    # sleep(8)
    # # driver.save_screenshot(testingOpernationInstance.output+r"\videorecording_ss.png")

    # driver.save_screenshot(testingOpernationInstance.test+r"\playground_camerasection.png")
    # points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground_camerasection.png",testingOpernationInstance.template+r"\pixeltab_playground_camera_back.png")
    # testingOpernationInstance.click_elements(points,driver)
    # sleep(8)
    # # driver.save_screenshot(testingOpernationInstance.output+r"\play_ground_ss.png")



     ##################  Story Section #######################################
    driver.save_screenshot(testingOpernationInstance.test+r"\playground.png")
    points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground.png",testingOpernationInstance.template+r"\pixeltab_playground_story.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(8)
    # driver.save_screenshot(testingOpernationInstance.output+r"\story_section_ss.png")

    driver.save_screenshot(testingOpernationInstance.test+r"\playground_story_section.png")
    points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground_story_section.png",testingOpernationInstance.template+r"\play_ground_story_scr_1.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(8)

    driver.save_screenshot(testingOpernationInstance.test+r"\playground_story.png")
    points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground_story.png",testingOpernationInstance.template+r"\pixeltab_playground_videogame_back.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(8)

    driver.save_screenshot(testingOpernationInstance.test+r"\playground_story_section.png")
    points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground_story_section.png",testingOpernationInstance.template+r"\pixeltab_playground_videogame_back.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(8)
    # driver.save_screenshot(testingOpernationInstance.output+r"\play_ground_record_ss.png")

     ##################  Number Game #######################################
    sleep(10)
    driver.save_screenshot(testingOpernationInstance.test+r"\playground.png")
    points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground.png",testingOpernationInstance.template+r"\pixeltab_playground_number.png")
    testingOpernationInstance.click_elements(points,driver)
    sleep(8)
    # driver.save_screenshot(testingOpernationInstance.output+r"\number_game_ss.png")
    
    sleep(8)
    driver.save_screenshot(testingOpernationInstance.test+r"\playground_numbergame.png")
    points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground_numbergame.png",testingOpernationInstance.template+r"\play_ground_number_scr.png")

    driver.save_screenshot(testingOpernationInstance.test+r"\playground_number_game.png")
    points = testingOpernationInstance.find_matches(driver,testingOpernationInstance.test+r"\playground_number_game.png",testingOpernationInstance.template+r"\game_sound_blue.png")
    # testingOpernationInstance.click_elements(points,driver)
    sleep(8)
    # driver.save_screenshot(testingOpernationInstance.output+r"\number_game_ss.png")
    driver.close_app()
    print("Done Testing Play Ground")
    
    
   
    





















 
   