@echo off

REM Remove sensitive data from .env file
powershell -Command "& {(Get-Content .env) -replace 'DATABASE_URL=.*','DATABASE_URL=<REDACTED>' | Set-Content .env}"
powershell -Command "& {(Get-Content .env) -replace 'SECRET_KEY=.*','SECRET_KEY=<REDACTED>' | Set-Content .env}"
powershell -Command "& {(Get-Content .env) -replace 'MAIL_USERNAME=.*','MAIL_USERNAME=<REDACTED>' | Set-Content .env}"
powershell -Command "& {(Get-Content .env) -replace 'MAIL_PASSWORD=.*','MAIL_PASSWORD=<REDACTED>' | Set-Content .env}"

REM Add .env to the staging area
git add .env
