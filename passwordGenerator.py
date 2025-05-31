import random
import string 
import os
alphabet = string.ascii_letters
digits = "0123456789"
symbols = "!@#$%&"

def create_password(strings = True, numbers = True, characters = True):
    password = ""
    length = 12
    while len(password) != length:
        if len(password) != length:
            temp = random.choice(alphabet)
            temp2 = random.choice(digits)
            temp3 = random.choice(symbols)
            password  += temp
            password += temp2 
            password += temp3
            continue 
        else:
            break 
        
    return str(password)
newPassword = create_password()

def save_password():
    directory = os.path.expanduser('~\\Documents')
    file_path = os.path.join(directory, 'password.txt')
    
    with open(file_path, 'w') as file:
        file.write(newPassword)
    print("file created with your new password in Documents folder called password.txt")
save_password()