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
echo     import os >> automatedMultiprocessing.py
echo     os.system^(r'%cd%\testingScripts\waitExtraction.py !A1[%%a]! ^> %cd%\testingScripts\results\!D1[%%a]!\!D1[%%a]!.txt'^) >> automatedMultiprocessing.py
)

echo if __name__ ^=^= "__main__"^: >> automatedMultiprocessing.py
for /f "skip=1 delims= " %%a in (output.txt)  do (
(echo     p%%a ^= multiprocess.Process^(target^=run%%a^) 
 )>> automatedMultiprocessing.py
)
echo ## Start proccesses >> automatedMultiprocessing.py
for /f "skip=1 delims= " %%a in (output.txt)  do (
(echo     p%%a.start^(^) 
 )>> automatedMultiprocessing.py
)
echo ## Wait all proccesses >> automatedMultiprocessing.py
for /f "skip=1 delims= " %%a in (output.txt)  do (
(echo     p%%a.join^(^) 
 )>> automatedMultiprocessing.py
)
call folder.bat
python automatedMultiprocessing.py
cd Report
python reportGeneration.py
echo Done

