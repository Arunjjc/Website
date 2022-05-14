import numpy as np
import pandas as pd
###################################Class Inheritance  Objects#######################################
class Salary:
    def __init__(self, firstname, lastname, wages):
        self.firstname = firstname
        self.lastname = lastname
        self.wages = wages
p1 = Salary("arun", "kumar", 3000)
print(p1.wages)

###################################Concntanete Tupils#######################################
tup1 = ("1", "Arun", "3")
tup2 = ("Adding Tups", "3")
print(tup2+tup1)

####################################Functions##################################################
def addfun():
    print(num1+num2)
num1 = 5
num2 = 8
addfun()

#######################################Numpy############################################
arr1 = np.zeros((3,3))
arr2 = np.ones((3,3))
print(arr1+arr2)

#########################################Pandas##########################################

dataframe1 = pd.DataFrame([[12, "Arun", 3.14],
                           [13, "Raj",9.7]])
dataframe2 = pd.read_csv(r"C:\Users\ARUNKUMAR\Desktop\Test.csv")
print(dataframe2.groupby("Sex").count())
print(dataframe1)
print(dataframe2.head(10))

#########################################List->dataframe##############################

Bike = ["TVS", "Bajaj", "HD", "Suzuki", "BMW"]
print(Bike[3])
Car = ["Honda", "Benz", "Maruthi", "Geely","KIA"]
print(Car[3])
dataframe3 = pd.DataFrame()
d = {"Bike":Bike, "Car":Car}
dataframe3 = pd.DataFrame(d)
print(dataframe3)
dataframejoin = pd.merge(dataframe3,dataframe3)
print(dataframejoin)

#############################Capitalize################################
name = "arun"
name1 = name.capitalize()
print(name1)

#########################list insert###############################
list = [1,2,3,4,5,6,7,8,9]
list.insert(15,10)
print(list)

#######################For comprehension#######################################

list=[i for i in range (1000)]
list2 = "Arun"
list1 = list2.split(",")
print(list1)

######################LAMBDA############################################

triple = lambda x: x*100
print(triple(93))

######################Factorial############################################

print("fun")
def fac(x):
    if x==1:
        return 1
    else:
       return (x * fac(x-1))

i=fac(3)
print(i)

