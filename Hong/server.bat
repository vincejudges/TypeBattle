@echo off
start cmd /k "python TBServer.py"
timeout /T 2
start cmd /k "python TBDisplayServer.py display"