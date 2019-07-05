Local Automated Testing System files
-startTesting.bat file is the starting point of testing.
-devices.bat extract the information of all the devices connnected to ADB.
-generateSetDevices.bat generates a python script which parallelly copy and installs APK on the connected devices and copy OBB.
-testAppium.py initailizes appium sever instances for all the connected devices.
-combined.bat allocates appium server instances to their repective devices.
-generateScript.bat generates a python script which will parallelly run the test cases on the connected devices using appium server.
-folder.bat creates folders for the connected devices so that testing results can be stored.