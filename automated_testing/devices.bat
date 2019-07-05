adb devices -l > devices.txt
echo device! >deviceId.txt
for /f %%a in (devices.txt) do (
echo %%a! >> deviceId.txt

)

set /a cnt=0
for /f "skip=2 delims=!" %%a in (deviceId.txt) do (
set /a cnt+=1
)
call generateSetDevices.bat
python setDevices.py
python testAppium.py %cnt%
call combined.bat
