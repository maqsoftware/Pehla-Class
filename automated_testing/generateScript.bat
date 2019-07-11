:: This script generate a python script to runb test cases on all the connected devices in parallel
:: import section of the python script 
echo # multiprocessing automated script > automatedMultiprocessing.py
(
echo import multiprocess
echo from multiprocess import Process
echo import os
echo #
) >> automatedMultiprocessing.py

set /A c =0
setlocal enableDelayedExpansion
for /f "skip=1 delims=#" %%a in (output.txt)  do (
set /A c+=1
set A1[!c!]=%%a
)

set /A c =0
for /f "skip=1 delims= " %%a in (output.txt)  do (
set /A c+=1
set D1[!c!]=%%a
)



for /L %%a in (1,1,%c%)  do (
call echo !D1[%%a]!
echo def run!D1[%%a]!^(^)^: >> automatedMultiprocessing.py
:: Error was there if this import statement was on their in python script
echo     import os >> automatedMultiprocessing.py
:: Calls respective testing scripts as per user requirement
echo     os.system^(r'%cd%\%1\%1.py !A1[%%a]! ^> %cd%\%1\results\!D1[%%a]!\!D1[%%a]!.txt'^) >> automatedMultiprocessing.py

)

echo # Main section >> setDevices.py
echo if __name__ ^=^= "__main__"^: >> automatedMultiprocessing.py
:: define all the proccesses
for /f "skip=1 delims= " %%a in (output.txt)  do (
(echo     p%%a ^= multiprocess.Process^(target^=run%%a^) 
 )>> automatedMultiprocessing.py
)
:: Start all the processes
echo ## Start proccesses >> automatedMultiprocessing.py
for /f "skip=1 delims= " %%a in (output.txt)  do (
(echo     p%%a.start^(^) 
 )>> automatedMultiprocessing.py
)
:: wait all the processes to end
echo ## Wait all proccesses >> automatedMultiprocessing.py
for /f "skip=1 delims= " %%a in (output.txt)  do (
(echo     p%%a.join^(^) 
 )>> automatedMultiprocessing.py
)
:: create foldersand files in result section for the devices 
call folder.bat %1
:: run generated script to start testing parallelly 
python automatedMultiprocessing.py
cd Report
:: run python script to generate report
python reportGeneration.py %1
echo Done

