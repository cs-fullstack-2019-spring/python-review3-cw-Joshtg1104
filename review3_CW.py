def main():
    # problem1()
    # problem2()
    problem3()


# ### Problem 1:
# Given a number n, return ```True``` if n is in the range 1..10, inclusive.
# Unless outside_mode is ```True```, in which case return True if the number is less or equal to 1,
# or greater or equal to 10. Print the result returned from your function.
# BONUS: Get the number and outside_mode flag from User input instead of hardcoding it
# ```def in1to10(n, outside_mode):```
# Examples of Expected Output:
# ```in1to10(5, False)``` → True
# ```in1to10(11, False)``` → False
# ```in1to10(11, True)``` → True

# def problem1():
#     Kevin should no longer skip in class work, it usually goes over similar problems which helps with understanding
#    the graded work.
#
# def in1to10(n, outside_mode):
#     outside_mode = n > 10 or n < 1
#     n = int(input("Enter a number"))
#     if n >= 1 and n <= 10:
#         print("True")
#     if outside_mode = False:
#         return("False")
#     if n > 10 or n < 1:
#         return("False")
#     if outside_mode = True:



# ### Problem 2:
# ##### We will keep having (some variation) of this problem until EVERYONE gets it right without help
# Create a function that has a loop that quits with the equal sign. If the user doesn't enter the equal sign,
# ask them to input another string.
# Once the user enters the equal sign to quit,
# print all the strings that were entered as one line with each word separated by a comma and space.
# Example of Expected Output:
# ```You, Entered, These, Words, Today```

def problem2():

    entry =input("Say something. Press = to Exit.")
    array = []
    while(entry != '='):
        entry = input("Say something else. Press = to Exit.")
        if entry == '=':
            print(array)

        else:
            array.append(entry)
            continue

# ### Problem 3:
# Given a non-negative number "num", return ```True``` if num is within ```2``` of a *multiple of 10*.
# Print the result from your function.
# BONUS: Get the number from User input instead of hardcoding it
# ```def near_ten(num):```
# Examples of Expected Output:
# ```near_ten(12)``` → True
# ```near_ten(17)``` → False
# ```near_ten(19)``` → True

def problem3():
    num = 45

    if num % 10:
        num += 2
        num -= 2
        print("True")
    else:
        print("False")












if __name__ == '__main__':
    main()