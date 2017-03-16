@echo off
title Toontown HD - Localhost Client

:main
"Panda3d-1.10.0/python/ppython.exe" -m toontown.toonbase.ToontownStart
pause
goto main
