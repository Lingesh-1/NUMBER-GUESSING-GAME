#NUMBER GUESSING GAME
import random as r
# In video they created function for diffculity game
def guess(gnum,rannum):
    global attempt
    global isgameover
    if 2<=attempt:
        if gnum >rannum:
            print("TO HIGH!!!")
            print("Guess Again!")
            attempt =attempts()
            print(f"You have {attempt} attempts left!!!")
            isgameover=True
        elif gnum <rannum:
            # attempt-=1
            attempt =attempts()
            print("TO LOW!!!")
            print("Guess Again!")
            print(f"You have {attempt} attempts left!!!")
            isgameover=True
        else:
            isgameover= False
            print(f"\\nYOU GOT IT!THE ANSWER IS {rannum}.")
            print("""
            ╦ ╦╔═╗╦ ╦  ╦ ╦╔═╗╔╗╔
            ╚╦╝║ ║║ ║  ║║║║ ║║║║
             ╩ ╚═╝╚═╝  ╚╩╝╚═╝╝╚╝""")
    elif attempt==1:
        if gnum==rannum:
            print(f"\n\nYOU GOT IT!THE ANSWER IS {rannum}.")
            print("""
            ╦ ╦╔═╗╦ ╦  ╦ ╦╔═╗╔╗╔
            ╚╦╝║ ║║ ║  ║║║║ ║║║║
             ╩ ╚═╝╚═╝  ╚╩╝╚═╝╝╚╝""")
        else:
            print("""
            ╦ ╦╔═╗╦ ╦  ╦  ╔═╗╔═╗╔═╗
            ╚╦╝║ ║║ ║  ║  ║ ║╚═╗║╣ 
             ╩ ╚═╝╚═╝  ╩═╝╚═╝╚═╝╚═╝""")
        print(f"The Number is {rannum}")
        print("Better Luck Next Time.")
        isgameover= False



def attempts():
    global attempt
    return attempt-1

asscii=""""
╔╗║╦ ╦╔╦╗╔╗ ╔═╗╦═╗  ╔═╗╦ ╦╔═╗╔═╗╔═╗╦╔╗╔╔═╗  ╔═╗╔═╗╔╦╗╔═╗
║║║║ ║║║║╠╩╗║╣ ╠╦╝  ║ ╦║ ║║╣ ╚═╗╚═╗║║║║║ ╦  ║ ╦╠═╣║║║║╣ 
║╚╝╚═╝╩ ╩╚═╝╚═╝╩╚═  ╚═╝╚═╝╚═╝╚═╝╚═╝╩╝╚╝╚═╝  ╚═╝╩ ╩╩ ╩╚═╝
"""
print(asscii)
print("Welcome to the Number Guessing Game")
diff=['easy','hard']
numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
rannum=r.randint(0,len(numbers)-1)
difficulty= input("Chose a difficulty.type 'easy' or 'hard':").lower()
print("Guess The Number between 1to 100!!!")
if diff[0]==difficulty:
    attempt=10
elif diff[1]==difficulty:
    attempt=5
else:
    print("Enter a valid difficulty level")

print(f"You have {attempt} remaining to guess the number.")


isgameover=True#FLAG
while  isgameover:
    gunum=int(input("Make a guess:"))
    guess(gunum,rannum)


""""what is  white hole? who proposed white hole theory? 
how white holes are formed?
 how white hole is different from black hole? 
images of black hole and white hole"""




















# def game():
#     def guess(gnum,rannum):
#         global attempt
#         global isgameover
#         if 2<=attempt:
#             if gnum >rannum:
#                 print("TO HIGH!!!")
#                 print("Guess Again!")
#                 attempt =attempts()
#                 print(f"You have {attempt} attempts left!!!")
#                 isgameover=True
#             elif gnum <rannum:
#                 # attempt-=1
#                 attempt =attempts()
#                 print("TO LOW!!!")
#                 print(f"You have {attempt} attempts left!!!")
#                 isgameover=True
#             else:
#                 isgameover= False
#                 print("YOU WON!!!")
#         elif attempt==1:
#             print("YOU LOSE!!!")
#             print(f"The Number is:{rannum}")
#             print("Better Luck Next Time.")
#             isgameover= False
#     def attempts():
#         global attempt
#         return attempt-1
   


# game()

