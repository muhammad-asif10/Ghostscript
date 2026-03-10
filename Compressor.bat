@echo off
setlocal enabledelayedexpansion

set "GS_OUTPUT_DIR=compressed_files"
if not exist "%GS_OUTPUT_DIR%" mkdir "%GS_OUTPUT_DIR%"

set /a count=0
for %%i in (*.pdf) do set /a count+=1

set /a current=0

for %%i in (*.pdf) do (
    set /a current+=1
    echo [!current!/!count!] Compressing %%i

    "C:\Program Files\gs\gs10.06.0\bin\gswin64c.exe" -sDEVICE=pdfwrite -dPDFSETTINGS=/screen -dNOPAUSE -dBATCH -dQUIET -sOutputFile="%GS_OUTPUT_DIR%\%%i" "%%i"
)

echo DONE. All !count! files compressed.
pause