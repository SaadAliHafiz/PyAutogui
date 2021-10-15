import random
from typing import List
import pyautogui


chars= "abcdefghijklmnopqrstuvwxyz0123456789"
char_list = list(chars)

password=pyautogui.password("Enter a password : ")
guess_password = ""

while guess_password!=password:
    guess_password=random.choices(char_list,k=len(password))

    print("<=========================="+ str(guess_password)+ "========>")

    if guess_password==list(password):
        print("your password is : "+ "".join(guess_password))
        break