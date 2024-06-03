import random
characters= ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789#$%*&")
while 1:
    password_length=int (input(" enter lenghth would like in your password "))
    password_count=int (input("how many passwords would you like to generate "))
    for x in range (0,password_count):
        password= ""
        for x in range (0,password_length):
            password_char=random.choice(characters)
            password  = password+password_char
            
        print ("here is your password :",password)
        
        