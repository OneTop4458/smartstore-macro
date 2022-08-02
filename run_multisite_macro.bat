@ECHO off
SET APP=SMARTSTORE-MACRO.exe
rem MASK on site
FOR /F "delims=" %%i in (SITE.txt) DO (
echo %%i
start cmd /c %APP% --target %%i
)

GOTO :EOF
