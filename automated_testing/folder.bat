:: this script creates folder and files for the results of testing
:: 'cd' is a variable use for current directory %cd% is its value
if not exist %cd%\testingScripts\results mkdir %cd%\testingScripts\results
set /A i=0

setlocal enableDelayedExpansion
:: folder to store device's results
for /F "skip=2 delims=!" %%a in (deviceId.txt) do (
if not exist %cd%\testingScripts\results\%%a mkdir %cd%\testingScripts\results\%%a
if not exist %cd%\testingScripts\results\%%a\outputs mkdir %cd%\testingScripts\results\%%a\outputs
if not exist %cd%\testingScripts\results\%%a\tests mkdir %cd%\testingScripts\results\%%a\tests
set A1[!i!]=%%a
set /A i+=1
) 

set /A i=0
for /F "skip=1 delims=!" %%a in (devices.txt) do (
set A2[!i!]=%%a
set /A i+=1
)

:: device details in run folder
set /A i-=1 
for /L  %%a in (0,1,%i%) do (
echo !A2[%%a]! > %cd%\testingScripts\results\!A1[%%a]!\deviceDetails.txt
)
