@ECHO OFF ::這是BATCH檔所使用的指令，如不需要可刪除 
echo 123 if %errorlevel% NEQ 0 (ECHO 成功)ELSE (ECHO 失敗)
pause