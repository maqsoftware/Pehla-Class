echo off
echo combined output > output.txt
set /A i=0
setlocal enableDelayedExpansion
for /F "skip=2 delims=!" %%a in (deviceId.txt) do (
    set /A i+=1
    set A1[!i!]=%%a
)
set /A i=0
for /F "delims=!" %%a in (activePorts.txt) do (
    set /A i+=1
    set A2[!i!]=%%a
)
for /L %%a in (1,1,%i%) do (
call echo !A1[%%a]! !A2[%%a]!# >> output.txt
)

call generateScript.bat
