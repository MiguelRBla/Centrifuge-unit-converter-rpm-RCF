#This is a program to convert rpm to centrifugal relative force and viceversa
print("WELCOME TO THE UNIT CONVERTER FOR LAB CENTRIFUGAL MACHINES")

import math

#variables

k=1.12e-5 #constant
g=918 #cm*s^2


#program starts here
while True:
    unit=input("To what do you want to convert? [rpm/FCR]: ").lower() #defines coversion direction
    
    if unit=="rpm" or unit=="RPM":
        r=float(input("What is your machine's radius (cm): ")) #asks for centrifuge radius
        fcr=float(input("How many G do you want to convert to rpm: ")) #asks for the number we want to convert
        rpm=math.sqrt(fcr/(k*r)) #conversion equation
        print(fcr,"G are",round(rpm,3),"rpm.") #gives the result
    elif unit=="FCR" or unit=="fcr":
        r=float(input("What is your machine's radius (cm): ")) #defines cetrifuge radius
        rpm=float(input("How many rpm do you want to convert to G: ")) #asks for the number we want to convert
        fcr=k*r*(rpm**2) #conversion equation
        print(rpm,"rpm are",round(fcr,3),"G.") #gives the result
    else:
        print("Error. Please answer rpm or FCR") #gives an error when incorrect input
        continue

    #covert again or exit program
    cont=input("Do you want to continue converting? [y/n]: ").lower()

    if cont=="n":
        print("Thanks for using the program. Until the next time!")
        print("Created by MiguelRBla for the FUNDAE Python essentials 1 course.")
        break

    print("------------------------------------")
