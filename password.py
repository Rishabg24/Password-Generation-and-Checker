
import string
import re
import random

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = '0123456789'
special = string.punctuation 

try:
    print('Welcome!')
    print('Would you like to generate or strengthen your passsword')
    choice = input()

    if choice == 'Generate':
      print('how many digits would you like it to be')
      length = int(input())
  
      string = lower + upper + num + special
      password = "".join(random.sample(string, length))
  
      print('Your new password is : ', password)

      pass

    elif choice == 'Strengthen':
       print('enter your password')
    password = input()
  
    if (len(password)) <= 20:
      print('Consider creating 20 character passwords for optimal strength. ')
    
    elif not re.search('[a-z]', password):
      print('You should consider adding some lower case letters in you password')
    
    elif not re.search('[A-Z]', password):
      print('You should consider adding some Upper case letters in your password')
    
    elif not re.search('[0-9]', password):
      print('You should consider adding some numbers to your password')

    elif not any(c in special for c in password):
      print('You should consider adding some special characters to your password')

    
    raise ValueError("Invalid choice. Please enter 'Generate' or 'Strengthen'.")
except ValueError as err:
    print(err)
