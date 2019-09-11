#!/usr/bin/env python3

# Date = 11 Sept 2019
# Version = i
# OriginalAuthor = Oliver Bonham-Carter

# Description: A basic calculator: This program asks the users to enter two numbers.
# Then the user will enter a mathematical operator to be applied to the numbers for
# the calculation.

def getResponse(prmpt, task ="string"):
# Handles the user input aspect for the program
# prmpt: the string of the question to ask the user
# task: if the parameter for this is "float" then return a float, otherwise
# return a string


    response_str = input(prmpt)
    if task == "float":
        try:
            return float(response_str) # variable is now of type float (has decimal in value)
        except ValueError: # the user has entered an alphabetic character
            print("\t Please enter numbers only. Exiting...")
            exit()
    else:
        return response_str
#end of getResponse()

def main(): # driver function
    print("  -------------------------------------------------")
    print("  |   This is a program to compute the addition,  |")
    print("  | subtraction, multiplication, division and     |")
    print("  | modulus of two user-entered numbers.          |")
    print("  -------------------------------------------------")
    prmpt = "\t Enter the first number in your equation : "
    num1_flt = getResponse(prmpt,"float") # specify a float to return
    print("\t\t + Your response is :",num1_flt)

    prmpt = "\t Enter the second number in your equation : "
    num2_flt = getResponse(prmpt,"float") # specify a float to return
    print("\t\t + Your response is :",num2_flt)

    prmpt = "\t Select an operator (+, -, *, / or %) : "
    op_str = getResponse(prmpt) # since no second option is added, we return a string.
    print("\t\t +Your response is :",op_str)

    print("\t The result of <<",num1_flt, op_str,num2_flt,">> is :",driveCalc(num1_flt, num2_flt, op_str)) # call function to perform the calculation
    print("")
#end of main()


#################### TODO (below) ####################

def driveCalc(num1_flt, num2_flt, op_str): # function to decide which function will perform what type of operation.
    print("\t\n The driveCalc() function to determine which function is to be called to perform a type of operation.")
    print("\t  First value: ",num1_flt)
    print("\t Second value: ",num2_flt)
    print("\t     Operator: ",op_str) # use this variable to
# end of driveCalc()

def add(): # function to add values and return value
    print("\t add()")
# end of add()

def subtract(): #function to substract the first inputted value from the second one.
    print("\t substract()")
# end of subtract()

def multiply(): #function to multiply the inputted values.
    print("\t multiply()")
#end of multiply()

def divide(): #function to divide the first inputted value (numerator) by the second one (denominator).
    print("\t divide()")
# end of divide()

def modulus(): # function to return the modulus result; the remainder.
    print("\t modulus()")
#end of modulus()
main() # begin the program
