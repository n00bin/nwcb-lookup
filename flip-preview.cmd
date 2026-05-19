@echo off
REM Double-click launcher for scripts\flip-preview.py
REM Reads PREVIEW_ACTIVE in js\preview-config.js, asks before flipping,
REM then commits + pushes so GitHub Pages redeploys.

cd /d "%~dp0"

where python >nul 2>nul
if errorlevel 1 (
    echo.
    echo ERROR: 'python' is not on PATH.
    echo Install Python from https://www.python.org/ and check
    echo "Add Python to PATH" during install, then try again.
    echo.
    pause
    exit /b 1
)

python "scripts\flip-preview.py"
set EXITCODE=%errorlevel%

echo.
echo Press any key to close this window.
pause >nul
exit /b %EXITCODE%
