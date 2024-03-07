@echo off
setlocal enabledelayedexpansion

REM Define json dictionary file
set "json_dict=dict.json"

REM Create output folder if it doesn't exist
if not exist output mkdir output

REM Get all the keys from the json dictionary using PowerShell
for /f "delims=" %%A in ('powershell -Command "Get-Content -Path ./%json_dict% -Raw | ConvertFrom-Json | Get-Member -MemberType NoteProperty | Select-Object -ExpandProperty Name"') do (
    set "filename=%%A"
    
    REM Check if the filename starts with 'NO'
   REM if /I "!filename:~0,5!"=="NO-30" (
        REM Check if the .tex file exists
        if exist "!filename!.tex" (
            REM Compile the tex file
            pdflatex --shell-escape "!filename!.tex"
            
            REM Find the corresponding new name in the json dictionary using PowerShell
            for /f "delims=" %%B in ('powershell -Command "Get-Content -Path ./%json_dict% -Raw | ConvertFrom-Json | Select-Object -ExpandProperty !filename!"') do (
                set "new_name=%%B"
            )

            REM If there is a corresponding new name
            if not "!new_name!"=="null" (
                REM Rename the pdf and move it to the output folder
                move "!filename!.pdf" "output/!new_name!.pdf"
            ) else (
                REM If no new name in the json, just move the file
                move "!filename!.pdf" output/
            )

            REM Remove the generated files except for the .pdf
            del "!filename!.aux" "!filename!.log" "!filename!.out" "!filename!.toc"
        )
   REM )
)

endlocal