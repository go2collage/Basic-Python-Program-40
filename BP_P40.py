# Python function that accepts a string

# also calculate number of upper and lower case letter of String

def string_cal(str1):
    d = {"Upper_Case": 0, "Lower_Case": 0}
    for i in str1:
        if i.isupper():                 # isupper() function
            d["Upper_Case"] += 1
        elif i.islower():               # islower() function
            d["Lower_Case"] += 1
        else:
            pass
    print("Number of Upper Case letters: ", d["Upper_Case"])
    print("Number of Lower Case letters: ", d["Lower_Case"])
    

str1 = input("Enter String that contains Upper & Lower case Letters: ")

print("The String is: ", str1)

string_cal(str1)

# Thanks for Watching