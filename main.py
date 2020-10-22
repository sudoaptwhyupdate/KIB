import os


#The idea for this progrsm comes from 'Automate the boring Stuff with Python" by Al Sweigart
#But however is coded by me
#onto the code


def kib():
    #Kib stands for 'keep idiot busy"
    clear = 'clear' #defining function for os.system()
    print("Want to know how to keep an idiot busy for hours")
    #Input doesnt actually do anything, it just creates a prompt for te idiot to type in
    input_kib = input()
    #Clear screen then end func
    os.system(clear)

#Takes function and then loops it 1000 times,
#This will create a loop where the idiot has to anter yes 999 times
for value in range(1, 999):
    kib()

#On the 1000th input it finally will say "Learn Python"
kib()
print("Learn Python!")