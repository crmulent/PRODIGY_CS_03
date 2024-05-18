import re
import argparse


def is_pwned(password):
    with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as f:
        for i in f:
            i = i.strip()
            if i == password:
                return True 
    return False


def check_strength(password):
    length = len(password)
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    numbers = any(char.isdigit() for char in password)
    special_chars = bool(re.match('[\\W_]', password))

    if length < 8:
        print("Password is too short")
        return 1

    score = length * 4
    if uppercase:
        score += 10
    if lowercase:
        score += 10
    if numbers:
        score += 10
    if special_chars:
        score += 10

    if is_pwned(password):
        print("Your password is compromised")
    elif score < 40:
        print("Weak password")
    elif score < 70:
        print("Moderate password")
    elif score < 100:
        print("Strong password")
    else:
        print("Very strong password")


def main():
    parser = argparse.ArgumentParser(
        description='Assess password\'s complexity.',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('-p', type=str, metavar='password', help='password to assess')
    password = parser.parse_args().p

    if not password:
        print('usage: password_checker.py [-h] [-p password]')
        return 1
    check_strength(password)


if __name__ == '__main__':
    main()
