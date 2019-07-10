:: This script generate a python to install APK and copy OBB to all the connected devices in parallel


echo # multiprocessing automated script > setDevices.py
(
echo import multiprocess
echo from multiprocess import Process
echo import os
echo #
) >> setDevices.py
setlocal enableDelayedExpansion
set /A c =0
for /f %%a in (%1/resources.txt) do (
set R[!c!]=%%a
set /A c+=1
)
set /A c =0
for /f "skip=2 delims=!" %%a in (deviceId.txt)  do (
set /A c+=1
set D1[!c!]=%%a
)

for /L %%a in (1,1,%c%)  do (


:: generates funtions for all the devices.
call echo !D1[%%a]!
echo def run!D1[%%a]!^(^)^: >> setDevices.py
echo     import os >> setDevices.py

:: Extract the only file names present in a directory
cd apk/%1
for /r %%f in (*) do (
cd ..
cd ..
echo     os.system^(r'adb -s !D1[%%a]! push  %cd%/apk/%1/%%~nxf /data/local/tmp/'^) >> setDevices.py
echo     os.system^(r'adb -s !D1[%%a]! shell "cd /data/local && chmod 777 tmp && cd tmp && chmod 777 %%~nxf && pm install -r /data/local/tmp/%%~nxf && exit"'^) >> setDevices.py 
cd apk/%1
)
cd ..
cd ..

:: Extract the only folder names present in a directory
cd obb/%1
for /d %%D in (*) do (
cd ..
cd ..
echo     os.system^(r'adb -s !D1[%%a]! push %%~fD/ /storage/emulated/0/Android/obb'^) >> setDevices.py
cd obb/%1
)
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
python testAppium.py %c%

