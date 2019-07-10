echo off
call devices.bat

echo kitkit onebillion
SET /P _inputname= Please enter Application name:

IF "%_inputname%"=="kitkit" GOTO :start_kikit_main
IF "%_inputname%"=="onebillion" GOTO :start_onebillion

echo not a valid input
pause
GOTO :end

:start_kikit_main
echo Starting Kitkit School Main App testing

call generateSetDevices.bat Kitkit
python setDevices.py 
call combined.bat
call generateScript.bat Kitkit
echo Starting Kitkit School Library App testing

call generateSetDevices.bat KitkitLibrary
python setDevices.py
call combined.bat
call generateScript.bat KitkitLibrary
GOTO :end

:start_onebillion
echo Starting onebillion App testing
pause
call generateSetDevices.bat onebillion
python setDevices.py
call combined.bat
call generateScript.bat onebillion
:end

