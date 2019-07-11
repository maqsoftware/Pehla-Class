:: it uploads the report on google drive and send them to defined emails in email.txt
gdrive-windows-x64.exe upload %cd%\Report\testingReport%1.xlsm  > gdrivelist.txt
setlocal enableDelayedExpansion
set /A c=0
for /f "skip=1 tokens=2" %%a in (gdrivelist.txt)  do (
if !c! == 0 set ID=%%a
set /A c+=1
)

for /f "skip=1 delims= " %%a in (email.txt)  do (
gdrive-windows-x64.exe share %ID% --type user --email %%a
)

