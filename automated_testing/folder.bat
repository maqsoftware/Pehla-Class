if not exist %cd%\%1\results mkdir %cd%\%1\results
set /A i=0
setlocal enableDelayedExpansion
for /F "skip=2 delims=!" %%a in (deviceId.txt) do (
if not exist %cd%\%1\results\%%a mkdir %cd%\%1\results\%%a
if not exist %cd%\%1\results\%%a\outputs mkdir %cd%\%1\results\%%a\outputs
if not exist %cd%\%1\results\%%a\tests mkdir %cd%\%1\results\%%a\tests
set A1[!i!]=%%a
set /A i+=1
) 
set /A i=0
for /F "skip=1 delims=!" %%a in (devices.txt) do (
set A2[!i!]=%%a
set /A i+=1
)
set /A i-=1 
for /L  %%a in (0,1,%i%) do (
echo !A2[%%a]! > %cd%\%1\results\!A1[%%a]!\deviceDetails.txt
)
