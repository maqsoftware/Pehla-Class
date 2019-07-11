Local Automated Testing System

This system parallelly tests application on the connected devices.The script present here for Kitkit School Application and onebillion Application uses image recognition technic to test GUI.    

- startTesting.bat file is the starting point of testing.
- devices.bat extract the information of all the devices connnected to ADB.
- generateSetDevices.bat generates a python script which parallelly copy and installs APK on the connected devices and copy OBB.
- testAppium.py initailizes appium sever instances for all the connected devices.
- combined.bat allocates appium server instances to their repective devices.
- generateScript.bat generates a python script which will parallelly run the test cases on the connected devices using appium server.
- folder.bat creates folders for the connected devices so that testing results can be stored.
- sendReport.bat it uploads report on google drive and sends it to the defined mail from email.txt.
- email.txt it contains all the emails to which we want to send reports.

