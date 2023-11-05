#!/usr/bin/env python
# coding: utf-8

# In[ ]:


attempt_count = 0
username = 'admin'
actual_password = 'test123$'
while True:
    
    try:
        user_name = input("Enter Your Name Please: ")
        password = input("Enter Your Password Here: ")
        attempt_count = attempt_count + 1

        if user_name == username and password == actual_password and attempt_count < 4:
            print("Log in Succesfull!")
            break
        elif attempt_count >= 4:
            print("Number Of Attempts are Exceeded! Please Contact Customer Care to Unblock Your Account.")
        else:
            print("Log in Failed! Please Try Again.")

    except:
        print("Something Went Wrong!")
    


# In[ ]:


attempt_count = 0
username = 'admin'  # stored username in system
otp = 5565 # stored password in system
while True:
  try:
    attempt_count = attempt_count+1
    user_name = input('Enter your yourname please: ') # username which user will supply at run time for validation and authentication
    password = int(input('Enter your password: '))  # password which user will supply at run time for validation and authentication
    if user_name == username and password == otp and attempt_count <4:
      print('Login successful')
      break
    elif attempt_count >=4:
      print('Number of attempts exceeded, Please contact customer care to unblock account')
      break
    else:
      print('login failed because of wrong credentials')

  except:
    if attempt_count >=4:
      print('Number of attempts exceeded, Please contact customer care to unblock account')
      break
    else:
      print('Something went wrong')

