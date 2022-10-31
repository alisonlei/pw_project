import random
import string
class Login:
    def __init__(self,site,user,pw):
        self.site=site
        self.user=user
        self.pw=pw
    def change_pw(self):
        self.pw=make_password()
    def show_account(self):
        print('Login:',self.site)
        print('Username:',self.user)
        print('Password:',self.pw)

def pw_length(): 
    again=True
    while  again: 
      try:
        length=int(input('Choose a password length between 8-50.'))
        if length<8 or length>50:
            print('The length must be between 8 and 50')
        else:
          again=False
      except:
        print('the length must be a integer')
      
    print('this is the password length:',length)
    return length
def special_char():
    answer=input('Do you want to include special characters in your password?\
        Enter Y/N')
    while answer!='Y' and answer!='y' and answer!='N' and answer!='n':
        print('you must type Y/N')
        answer=input('Do you want to include special characters in your password?\
        Enter Y/N')
    if answer=='y' or answer=='Y':
        return True
    else:
        return False
def make_password():
    length=pw_length()
    special=special_char()
    if special:
        characters=string.ascii_letters+string.digits+string.punctuation
    else:
        characters=string.ascii_letters+string.digits
    #let user have a preview of the password generated
    change='y'
    while change=='y':
     password=''  
     for n in range(length):
        password=password+random.choice(characters)
     print('your password is',password)
     change=input('do you want another password?Enter y/n')
    return password

def main():
    print('welcome to password generator')
    site=input('enter the site name')
    user=input('create a user')
    pw=make_password()
    
    a=Login(site,user,pw)
    a.show_account()
    
    change=input('do you want to change your password?Type Y/N' )
    while change=='y'or change=='Y':
      a.change_pw()
      a.show_account()
      #let the user make a new password,with choice of length and choice of
      #special characters 
      change=input('do you want to change your password?Type Y/N' )

main()
   
    

