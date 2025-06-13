import random
import string 
import os

alphabet = string.ascii_letters
digits = "0123456789"
symbols = "!@#$%&"

reason = input("what is this new password for?(keep it simple): ")

def create_password():
    password = ""
    length = 12
    while True:
        if len(password) != length:
            temp = random.choice(alphabet)
            temp2 = random.choice(digits)
            temp3 = random.choice(symbols)
            password  += temp
            password += temp2 
            password += temp3
            continue
        break
        
    return str(password)
newPassword = create_password()
def save_password():
    directory = os.path.expanduser('~\\Documents')
    file_path = os.path.join(directory, 'password.txt')
    if file_path == False:
        with open(file_path, 'w') as file:
            file.write(f'{reason}   password: {newPassword}\n')
        print("file created with your new password in Documents folder called password.txt")
    else:
        with open(file_path, 'a') as file:
            file.write(f'{reason}   password: {newPassword}\n')
        print("new password aded in your file at Documents folder called password.txt")
save_password()
