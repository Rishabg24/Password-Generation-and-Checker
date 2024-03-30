import string
import re
import random

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = '0123456789'
special = string.punctuation 

try:
    print('Welcome!')
    print('Would you like to Generate or Strengthen your password?')
    choice = input()

    if choice.lower() == 'generate':
        print('How many characters would you like it to be?')
        length = int(input())
  
        characters = lower + upper + num + special
        password = "".join(random.sample(characters, length))
  
        print('Your new password is : ', password)

    elif choice.lower() == 'strengthen':
        print('Enter your password:')
        password_input = input()
  
        if len(password_input) <= 20:
            print('Consider creating 20 character passwords for optimal strength.')
        
        if not re.search('[a-z]', password_input):
            print('You should consider adding some lower case letters to your password.')
        
        if not re.search('[A-Z]', password_input):
            print('You should consider adding some upper case letters to your password.')
        
        if not re.search('[0-9]', password_input):
            print('You should consider adding some numbers to your password.')
        
        if not any(c in special for c in password_input):
            print('You should consider adding some special characters to your password.')
        
        if (len(password_input) > 20 and 
            re.search('[a-z]', password_input) and 
            re.search('[A-Z]', password_input) and 
            re.search('[0-9]', password_input) and 
            any(c in special for c in password_input)):
            print('Your password is strong!')
    
    else:
        raise ValueError("Invalid choice. Please enter 'Generate' or 'Strengthen'.")
except ValueError as err:
    print(err)
