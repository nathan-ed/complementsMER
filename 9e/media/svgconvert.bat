@echo off
for %%f in (*.svg) do (
    if "%%~xf"==".svg" inkscape %%f -o %%~nf.pdf
)
