#number of occuranes set by the user
from tkinter.tix import CheckList


num = int(input())

# create a dictionary 
dic = {}

for i in range(num):
    # take input from the user for the dictionary
    user_input = input().split()
    #assign the divided input to dictionary as key and value
    dic[user_input[0]] = [user_input[1]]

while True:
    try:
        check_input = input()
        if check_input in dic:
            print(check_input "=" dic[input])

        else:
            print("Not Found")

    except EOFError:
        break
