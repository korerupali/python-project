#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install countdown-timer')

def welcome():
    print("Welcome to Mumbai | The city of Masala Chai")
    user_name=input("Please enter your name here:")
    print("Hello",user_name.title())
    user_budget=int(input("enter your budget for chai:"))
    
    if user_budget>=500:
        print("You can visit taj Hotel!")
    elif user_budget>=250 and user_budget<500:
        print("you can visit Trisent!") 
    elif user_budget>=100 and user_budget<250: 
        print("you can visit Starbucks!") 
    elif user_budget>=20 and user_budget<100:
        print("you can visit Udipi Hotel!")
    elif user_budget>=5 and user_budget<20: 
        print("you can visit any tapri | The best chai in the world!")
    else:
        print("Go back Simon!")


def dice_game():
    #dice game
    print("Welcome to the dice game")
    #user greet
    user_name=input("Please enter your name here:")
    print("Hello",user_name.title())
     #ask user choice
    user_number=input("please enter the number 1,2,3,4,5 or 6:")
    #display user choice
    print("You choose:",user_number.lower())
    #Dice Toss
    import random
    dice_num=random.choice('123456')
    #dice result display
    print('dice result:',dice_num)
    if user_number.lower()==dice_num:
        print("You win!")
    else:
        print("You lose!")


def heads_tails():
    #Heads and Tails game
    #user name
    print("Welcome to heads and tails game!")
    #user choice
    user_choice=input('Please choose Heads and Tails')
    #ddisplay user choice
    print('You chose:',user_choice.lower())
    #coin toss
    import random
    if random.choice('ab')=='a':
        coin_toss=('Heads')
    else:
        coin_toss=('Tails')
    #display result
    print("coin Result:",coin_toss)
    if user_choice.lower()==coin_toss.lower():
        print('You win!')
    else:
        print('You Lose!')


def multiplication():
    #multiplication table game
    print("Welcome to the World of multiplication")
    user_input=int(input("enter a number here:"))
    for i in range(1,11):
        print(user_input,'x',i,'=',i*user_input)
    
    
def cube():   
    #cube game
    # user welcome
    print('welcome to the world cube')
    #take 1 number as input
    user_input=int(input('please enter a number here:'))
    #use for loop
    for i in range(1,user_input+1):
        print('cube of',i,'=',i**3)

def ct():  
    from countdown import countdown
    user_min=int(input('please enter minutes here:'))
    user_sec=int(input('please enter seconds here:'))
    countdown(mins=user_min,secs=user_sec)


def factorial():
    #factorial number
    print('Welcome to the world of Factorial!')
    user_input=int(input('Enter a number:'))
    result=1
    for i in range(1,user_input+1):
        result=result*i
    print('The factorial of ',user_input ,'is',result)


def fibonacci():   
    #fibonacci series
    print('Fibonacci number')
    user_input=int(input('enter a number here:'))
    n1=0
    n2=1
    for i in range(user_input):
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3



def password_gen():    
    #password generator
    #welcome user
    print('Welcome to the password generator')
    #take a number as input from user-for password char limit
    num=int(input('enter number of characters you want in your password:'))
    #use for loop to generate password
    import random
    password=''
    for i in range(num):
        password=password+(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789012345678901234567890!@#$%^*(&^%!##$%^&*()><#$%^&&*()&%$%$'))
    print(password)




#import lybrary
import tkinter as tk

#creating a window
window=tk.Tk()

#change title
window.title('PYTHON PROJECTS')

#window size
window.geometry('515x400')

#Label
tk.Label(window,text='PYTHON PROJECTS',font=('bold',20)).place(x=120,y=40)
tk.Label(window,text='Made by: Rupali Kore',font=('Helvetica',14)).place(x=165,y=105)

#button
tk.Button(window,text='Budget Game',width=18,height=2,command=welcome).place(x=30,y=180)
tk.Button(window,text='Dice Game',width=18,height=2,command=dice_game).place(x=190,y=180)
tk.Button(window,text='Heads Tails game',width=18,height=2,command=heads_tails).place(x=350,y=180)

tk.Button(window,text='multiplication',width=18,height=2,command=multiplication).place(x=30,y=250)
tk.Button(window,text='Cube',width=18,height=2,command=cube).place(x=190,y=250)
tk.Button(window,text='Countdown Timer',width=18,height=2,command=ct).place(x=350,y=250)

tk.Button(window,text='Factorial Number',width=18,height=2,command=factorial).place(x=30,y=320)
tk.Button(window,text='Fibonacci Number',width=18,height=2,command=fibonacci).place(x=190,y=320)
tk.Button(window,text='Password Generator',width=18,height=2,command=password_gen).place(x=350,y=320)


window.mainloop()


# In[ ]:




