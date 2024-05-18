# PRODIGY_CS_03
A simple tool that assesses the strength of a password.

## Task
Build a tool that assesses the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. Provide feedback to users on the password's strength.

## Running the program
First, download the list of compromised passwords [here](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)

Place rockyou.txt inside the project's folder

Checking password
```
python password_checker.py -p <password>
```

Examples
```
python password_checker.py -p securepassword

Your password is compromised
```

```
python password_checker.py -p brb69420

Moderate password
```

```
python password_checker.py -p aVerySecurePassword54

Very strong password
```