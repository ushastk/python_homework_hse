import secrets
import string
import random

def generate_alphanum_crypt_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    crypt_rand_string = ''.join(secrets.choice(letters_and_digits) for i in range(length)) + "\n"
    return crypt_rand_string

n = random.randint(1, 100)
with open("lines.txt", "w", encoding="UTF-8") as file_out:
    for i in range(n):
        length = random.randint(1, 100)
        file_out.write(generate_alphanum_crypt_string(length))

random_line = random.randint(1, n)
with open("lines.txt", "r", encoding="UTF-8") as file_in:
    i = 0
    for line in file_in:
        if i == random_line:
            print(line.rstrip())
        i += 1


