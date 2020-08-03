echo off
:: %variable% is variable's value
:: /A is used to define integer type variable
:: /L is used to define Long integer type
:: by default variables are of string type
:: %i i is integer is the i th argument to the script 
call devices.bat

echo kitkit onebillion
:: user input for application name to test 
SET /P _inputname= Please enter Application name:

IF "%_inputname%"=="kitkit" GOTO :start_kikit_main
IF "%_inputname%"=="onebillion" GOTO :start_onebillion

echo not a valid input
pause
GOTO :end

:: NOTE: arguments are used in corresponding scripts to do the application specific testing

:: Kitkit school testing
:start_kikit_main
echo Starting Kitkit School Main App testing
call generateSetDevices.bat Kitkit
python setDevices.py 
call combined.bat
call generateScript.bat Kitkit

:: starts library and tools section testing 
echo Starting Kitkit School Library App and Tools section testing 
call generateSetDevices.bat KitkitLibrary
python setDevices.py
call combined.bat
call generateScript.bat KitkitLibrary
GOTO :end
 
:: onebillion testing 
:start_onebillion
echo Starting onebillion App testing
call generateSetDevices.bat onebillion
python setDevices.py
call combined.bat
call generateScript.bat onebillion
:end

