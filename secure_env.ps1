# Remove sensitive data from .env file
(Get-Content .env) | ForEach-Object { $_ -replace 'DATABASE_URL=.*', 'DATABASE_URL=<REDACTED>' `
                                    -replace 'SECRET_KEY=.*', 'SECRET_KEY=<REDACTED>' `
                                    -replace 'MAIL_USERNAME=.*', 'MAIL_USERNAME=<REDACTED>' `
                                    -replace 'MAIL_PASSWORD=.*', 'MAIL_PASSWORD=<REDACTED>' } | Set-Content .env

# Add .env to the staging area
git add .env
