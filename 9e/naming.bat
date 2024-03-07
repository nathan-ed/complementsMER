@echo off
setlocal EnableDelayedExpansion

:: Define json dictionary file
set "json_dict=dictionary.json"

:: Initialize the json dictionary
echo { > %json_dict%

:: Iterate over all .tex files in the current directory
for %%F in (*.tex) do (
    :: Get the file name and the first two letters
    set "old_name=%%~nF"
    set "new_name=!old_name:~0,2!"
    
    :: Write the file name and the first two letters to the json dictionary
    echo    "!old_name!": "!new_name!-", >> %json_dict%
)

:: Close the json dictionary
echo } >> %json_dict%

:: Replace the trailing comma with a space
powershell -Command "(Get-Content %json_dict%) -replace ',\\s*}', ' }' | Set-Content %json_dict%"
