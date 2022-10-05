import string
import random


# characters we wish to generate password from
chars = list(string.ascii_letters + string.digits + "!@#$%^&*()")

# function to generate password
def generate_password(pwd_length):
  random.shuffle(chars)

  pwd = list()

  # Creates a random password based on the pwd_length given
  for _ in range(pwd_length):
    pwd.append(random.choice(chars))

  random.shuffle(pwd)

  pwd = "".join(pwd)

  return pwd
