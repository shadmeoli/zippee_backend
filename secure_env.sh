#!/bin/bash

# Create pre-commit hook script
cat > pre-commit <<EOF
#!/bin/bash

# Remove sensitive data from .env file
sed -i 's/DATABASE_URL=.*/DATABASE_URL=<REDACTED>/' .env
sed -i 's/SECRET_KEY=.*/SECRET_KEY=<REDACTED>/' .env
sed -i 's/MAIL_USERNAME=.*/MAIL_USERNAME=<REDACTED>/' .env
sed -i 's/MAIL_PASSWORD=.*/MAIL_PASSWORD=<REDACTED>/' .env

# Add .env to the staging area
git add .env
EOF

# Copy pre-commit hook script to .git/hooks directory
cp pre-commit .git/hooks/pre-commit

# Make pre-commit hook script executable
chmod +x .git/hooks/pre-commit

# Clean up
rm pre-commit
