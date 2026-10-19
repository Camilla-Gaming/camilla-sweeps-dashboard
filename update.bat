@echo off
echo Syncing Camilla Sweeps VIP Dashboard to GitHub Pages...
git add .
git commit -m "Updated real player database"
git push origin main
echo.
echo ✅ Dashboard updated live on GitHub Pages!
pause
