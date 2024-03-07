@echo off
for %%f in (*.ipe) do (
    if "%%~xf"==".ipe" ipetoipe -pdf %%f
)
