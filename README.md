# Updates

I created **a one time run** script that hides your credentials
With this update you don't have to update your .env file not will not need to ignore it in the .gitignore file.

> linux shell script to automate the process and a windows based script for the same

## To excute

> linux

simply run

```bash
./secure_env.sh

or

bash secure_env.sh
```

With this you don't have to change up the credentials on the .env file but it will write on top of it - placeholders.

> windows

##### with powershell

```ps1
move pre-commit.ps1 .git/hooks
```

This will move the powershell script to your local .git/hooks directory
then run

```ps1
powershell.exe -ExecutionPolicy Bypass -File ".git/hooks/pre-commit.ps1"
```

This will run the script on each commit

##### With cmd

```cmd
move path\to\file\secure_env.bat .git\hooks\pre-commit.bat
```

This will move the bat script to the .git/hooks directory

---

> NOTE: I have not tested he script on windows machine I am linux.
