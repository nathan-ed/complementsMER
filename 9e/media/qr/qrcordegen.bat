@echo off
for /F "tokens=1,2" %%A in (qr-codes.txt) do (
    set "url=%%A"
    set "word2=%%B"
    setlocal enabledelayedexpansion
    
    set "folder=!word2!"
    set "folder=!folder:/=_!"
    
    if not exist "img\!folder!\" (
        mkdir "img\!folder!\"
    )
    
    for %%F in ("!url:/=" "!") do (
        set "word3=%%~nxF"
        set "word3=!word3:~0,-1!"
    )
    if not exist "img\!folder!\!word3!\" (
        mkdir "img\!folder!\!word3!\"
    )
    set "word4=!url:~-1!"
    
    qrencode.exe -t EPS -o "img\!folder!\!word3!\!word3!_!word4!.eps" "!url!"
    endlocal
)