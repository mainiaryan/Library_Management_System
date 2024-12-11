print("----------Welcome to Skill Circle Library Management System----------\n")
# dictionary/library
books={1:'''Book's Title: Atomic Habits (101)
Author: James Clear
Price: 1099
Launch: October 16, 2018
Description: A practical guide to building good habits and breaking bad ones through small, incremental changes'''
,2:'''Book's Title : The Power of Habit (102)
Author : Charles Duhigg
Price : 999
Launch : February 2012
Description : A science-based exploration of how habits are formed and broken, with practical strategies for transforming your life'''
,3:'''Book's Title : Better Than Before (103)
Author : Gretchen Rubin
Price : 999
Launch : January 2015
Description : A personalized approach to habit formation, helping you identify your unique personality type and tailor your strategies accordingly'''
,4:'''Book's Title : Elastic Habits (104)
Author : Stephen Guise
Price : 315
Launch : August 2022
Description : A guide to creating flexible and adaptable habits that can withstand life's challenges, focusing on having multiple options and gradually increasing difficulty'''
,5:'''Book's Title : 168 Hours (105)
Author : Laura Vanderkam'
Price : 1099
Launch': August 2010
Description : A guide to time management, helping you identify how you spend your time and offering strategies to maximize your 168 hours each week'''
}
# menu
for i in range(1,6):
    print(f'Press {i} for Book {100+i}\'s Information')
# function
try:
    def lms(x):
        print(books[x])
        y=int(input('''\n>>>>> Do you want to Continue?\nPress 1 to Continue & 2 to Exit:'''))
        if y==1:
            lms(int(input('\n>>>>> Enter Number to get Book Information:')))
        elif y==2:
            print('\n-------Thanks for Visiting Skill Circle Library Management System-------')
        else:
            print('\nPlease Enter the Correct Number')
    lms(int(input('\n>>>>> Enter Number to get Book Information:')))
except:
    print('\nPlease Enter the Correct Number')
# for dictionary's key error & string's value error
