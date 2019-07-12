:: This script generate a python script to install APK and copy OBB to all the connected devices in parallel
:: import section of the python script
echo # multiprocessing automated script > setDevices.py
(
echo import multiprocess
echo from multiprocess import Process
echo import os
echo #
) >> setDevices.py

setlocal enableDelayedExpansion
:: this command enables to used updated value of a variable use !variable! for current variable value  
:: %variable% gives as the stable value i.e variable in not being updated over and over again 


set /A c =0
:: %%variable are for loop controller varaible
for /f "skip=2 delims=!" %%a in (deviceId.txt)  do (
set /A c+=1
set D1[!c!]=%%a 
:: in this loop !c! is current value of c in for loop !c! = 1 and change with iters but %c% = 0
)
:: here %c% == !c!
set /A cnt=%c%
for /L %%a in (1,1,%c%)  do (


:: generates funtions for all the devices.

echo def run!D1[%%a]!^(^)^: >> setDevices.py
echo     import os >> setDevices.py

:: Extract the only file names present in a directory
cd apk/%1
:: here in apk/---- folder we extract file names 
for /r %%f in (*) do ( 
cd ..
cd ..
:: back to current directory to store
echo     os.system^(r'adb -s !D1[%%a]! push  %cd%/apk/%1/%%~nxf /data/local/tmp/'^) >> setDevices.py
echo     os.system^(r'adb -s !D1[%%a]! shell "cd /data/local && chmod 777 tmp && cd tmp && chmod 777 %%~nxf && pm install -r /data/local/tmp/%%~nxf && exit"'^) >> setDevices.py 
cd apk/%1
)
:: back to current directory to store
cd ..
cd ..

:: Extract the only folder names present in a directory
cd obb/%1
:: here in obb/---- folder we extract folder names 
for /d %%D in (*) do (
cd ..
cd ..
:: back to current directory to store
echo     os.system^(r'adb -s !D1[%%a]! push %%~fD/ /storage/emulated/0/Android/obb'^) >> setDevices.py
cd obb/%1
)
:: back to current directory to store
cd ..
cd ..
)

echo # Main section >> setDevices.py
echo if __name__ ^=^= "__main__"^: >> setDevices.py
:: define all the proccesses
for /f "skip=2 delims=!" %%a in (deviceId.txt)  do (
(echo     p%%a ^= multiprocess.Process^(target^=run%%a^) 
 )>> setDevices.py
)
echo ## Start proccesses >> setDevices.py
for /f "skip=2 delims=!" %%a in (deviceId.txt)  do (
(echo     p%%a.start^(^) 
 )>> setDevices.py
)
echo ## Wait all proccesses >> setDevices.py
for /f "skip=2 delims=!" %%a in (deviceId.txt)  do (
(echo     p%%a.join^(^) 
 )>> setDevices.py
)
:: start Appium server instances 
echo     count=%cnt% >> setDevices.py
echo     os.system^(^"python testAppium.py ^" + str(count)^) >> setDevices.py


