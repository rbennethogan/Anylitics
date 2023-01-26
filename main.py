#Anylitics


# Stages of Anylitics

##Create and write a CSV File
#file = open("myFirstCSVFile.csv", "w")
#file.write("1, 2, 3, 4, 5")
#file.close()

#file = open("myFirstCSVFile.csv", "r")
#dataIn = file.read()
#file.close()
#print(dataIn)

## The data we have entered and read is a string.
##We can't do a lot of anylitics on a string.
## We will change our strings to a list.

##Task1 create a list called my list.
##TASK2 set it equal to dataIn.split(",")
##TASK3 print the list

#myList = dataIn.split(",") ## splits the dataIn commas
#print(myList)
#myList = [int(item) for item in myList]
#print(myList)
## We have a list of numbers

################################################################
# Q1. Create a python programme that asks a user to enter 
##their name and stores the name in a text file called myName. 
##Then read in the text file. 
#file = open("myName.txt", "w")
#file.write(input("Enter your name: "))
#file.close()

#file = open("myName.txt", "r")
#dataIn = file.read()
#file.close()
#print(dataIn)

##Q2. Write a program that asks a user for a password.
##Check whether the password entered matches the password
###in the text file
##Display a message to say whether they entered it
##correctly or not.
##How to complete Q2
##Create and open a .txt file called password.txt
##write the password into the file
##Close the file 
##Open the file up to read
##Create a variable called dataIn to store the file info
##Close the file
##Print the variable

#file = open("password.txt", "w")
#file.write("password")
#file.close()

#file = open("password.txt", "r")
#dataIn = file.read()
#file.close()
#print(dataIn)

##Create a variable that asks the user to enter a password
#passwordCheck =(input("Enter the password: "))
##Create an if statement that compares the password the 
##User enters to the password stored in the text file.
##If they are equal the output should read "Success"
##or else the output should say "Access denied"
#if passwordCheck == input("Please enter your password: "):
 # print("Successful")
#else:
#  print("Access Denied")
  ###############################################################
# numbers = [1, -19, 4, 3, -5, 2]
#   ### Find total of non-erroneous data and the amount to find the average

# totalNED = 0
# countNED = 0

# for item in numbers: 
#   if item >= 0:
#       totalNED += item
#       countNED += 1

# averageNED = totalNED/countNED 
# print(averageNED)

# for counter in range(len(numbers)):
#   if numbers[counter] = averageNED
# print(numbers)
############################################################
#import csv

#numList = [1, 3, 5, 6, 7, 8, 4, 9, 12, 17]

#numList.sort(reverse = True)
#print(numList)

#file = open("List of Numbers.csv", "w")
#file.write(str(numList))
#file.close()

#file = open("List of Numbers.csv", "r")
#dataIn = file.read()
#file.close()
#print(dataIn)

#print("The largest number is:",numList[0])
#print("The smallest number is:",numList[-1])
################################################################

## 3 Visualisation


###Python has inbuilt statistical functions
# Use them to find max & min
#myList=[2, 1, 5, 3, 7, 6, -1, -3]
#print("Min value: ", min(myList))
#print("Max value: ", max(myList))


# #### Finding Averages
## use python functions

## 1. Mean

#import statistics

#myList = [1, 4, 4, 7, 9]
#mean = statistics.mean(myList)
#print("mean: ",mean)

## 2. Median - middle value
#median = statistics.median(myList)
#print("Median: ", median)

## 3. Mode - most common/frequent value
#mode = statistics.mode(myList)
#print("mode: ", mode)

####Plotting graphs
## import graphing library, want to shorten name to ply
import matplotlib.pyplot as ply

#myList = [1, 4, 4, 7, 9]
#ply.plot(myList)
#ply.show()

### Adding Labels
#ply.title("Numbers")
#ply.xlabel("List index")
#ply.ylabel("Numbers")
#ply.show()

#Data not connected
#ply.plot(myList, "rs")
#ply.show()

###Line graphs
#numbers = [1, 2, 4, 3, 5, 2]
#names = ["a", "b", "c", "d", "e", "f"]
#ply.plot(names, numbers) #(x-axis, y-axis)
#ply.title("Brothers & Sisters")
#ply.xlabel("Student")
#ply.ylabel("Amount of Siblings")
#ply.show()

# Q1. Create a list of 20 values
# - Create a plot
# - Add a y-axis label
# - Add a title
# - show plot

#myList = [1, 2, 4, 3, 1, 5, 7, 6, 8, 9, 1, 6, 10, 5, 7, 8, 11, 9, 10, 4]
#ply.plot(myList)
#ply.ylabel("List index")
#ply.title("Numbers")
#ply.show()


## create a bar chart
#numbers = [1, 2, 4, 3, 5, 2,]
#names = ["a", "b", "c", "d", "e", "f"]
#ply.bar(names, numbers)
#ply.title("Brothers & Sisters")
#ply.xlabel("Student")
#ply.ylabel("Amount of Siblings")
#ply.show()

##TASK 2 create a scatter plot
#numbers = [1, 2, 4, 3, 5, 2]
#names = ["a", "b", "c", "d", "e", "f"]
#ply.scatter(names, numbers)
#ply.title("Brothers & Sisters")
#ply.xlabel("Student")
#ply.ylabel("Amount of Siblings")
#ply.show()

# ## create a pie chart

#numbers = [1, 2, 4, 3, 5, 2]
#names = ["Aoife", "Ben", "Carl", "Danny", "Ella", "Fionn"]
#ply.pie(numbers, labels = names)
#ply.title("Brothers & Sisters")
#ply.show()


# Q2. Find out the top 10 shows on Netflix

#numbers = [5, 4, 4, 9, 5, 8, 6, 5, 10, 7]
#names = ["ST", "PLL", "FRDS", "KDS", "TBBT", "SL", "TWD", "YS", "DH", "IS"]
#ply.pie(numbers, labels = names)
#ply.title("Netflix shows")
#ply.show()

#numbers = [5, 4, 4, 9, 5, 8, 6, 5, 10, 7]
#names = ["ST", "PLL", "FRDS", "KDS", "TBBT", "SL", "TWD", "YS", "DH", "IS"]
#ply.bar(numbers,  names)
#ply.title("Netflix shows")
#ply.show()


# ## Two graphs on the same axis

numbers = [1, 2, 4, 3, 5, 2]
names = ["Aoife", "Ben", "Carl", "Danny", "Ella", "Fionn"]
ages = [17, 12, 15, 6, 89, 1]

#Create a line graph with names on x-axis and numbers on y-axis

ply.plot(names, numbers)
ply.plot(ages)
ply.legend(["Numbers of siblings", "Age"])
ply.title("Brothers & Sisisters")
ply.xlabel("Student")
ply.ylabel("Total")
ply.show()

# Q3. sport Prize money-M  Prize money-F
#Football         2.2       0.6
#Cricket          3.1       0.5
#Golf             1         0.5
#Tennis           1.5       1.5
#Make 3 lists: name of sport, average prize for men and women, difference in prize money between men and women.
# X-label - name of sport
# Y-axis - average for men and women, prize gap
#Use a legend - use ply.plot

# import matplotlib.pyplot as ply

# averagePrize = [1.4, 1.8, 0.75, 1.5]
# sport = ["Football", "Cricket", "Golf", "Tennis"]
# difference = [1.6, 2.6, 0.5, 0]

# ply.plot(sport, averagePrize)
# ply.plot(difference)
# ply.legend(["averagePrize", "difference"])
# ply.xlabel("Sport names")
# ply.ylabel("Prizegap")
# ply.show()
















































            





