import random
import secrets

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

def gnerate_password(lenght=12):
    password = ""
    for i in range(lenght):
        password += random.choice(alphabet)
    return password

if __name__ == "__main__":
    password = gnerate_password(12)
    print(password)