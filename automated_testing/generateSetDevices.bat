echo # multiprocessing automated script > setDevices.py
(
echo import multiprocess
echo from multiprocess import Process
echo import os
echo #
) >> setDevices.py
setlocal enableDelayedExpansion
set /A c =0
for /f "skip=2 delims=!" %%a in (deviceId.txt)  do (
set /A c+=1
set D1[!c!]=%%a
)
for /L %%a in (1,1,%c%)  do (
call echo !D1[%%a]!
echo def run!D1[%%a]!^(^)^: >> setDevices.py
echo     import os >> setDevices.py
echo     os.system^(r'adb -s !D1[%%a]! push C:\Users\MAQUser\Documents\GitHub\GLEXP-Team-onebillion-Hindi\app\build\outputs\apk\enGB_community_\debug\app-enGB_community_-debug.apk /data/local/tmp/'^) >> setDevices.py
echo     os.system^(r'adb -s !D1[%%a]! shell "cd /data/local && chmod 777 tmp && cd tmp && chmod 777 app-enGB_community_-debug.apk && pm install -r /data/local/tmp/app-enGB_community_-debug.apk && exit"'^) >> setDevices.py
echo     os.system^(r'adb -s !D1[%%a]! push %cd%\obb\com.maq.xprize.onecourse.hindi /storage/emulated/0/Android/obb'^) >> setDevices.py
)

echo if __name__ ^=^= "__main__"^: >> setDevices.py
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
