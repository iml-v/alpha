##########################################################
# CST8333 2018 Final Project                             #
#                                                        #
# Created by Arish Kakadiya                              #
# Student number: 040894137                              #
# November 26 ,2018                                      #
#                                                        #
##########################################################


import csv
import pandas as pd # import statements

# I have choosed Pandas, because it's much faster, has an excellent and extremely rich API, a source code looks much cleaner and better, etc.


import CommodityPerform


df = pd.read_csv("32100054.csv", sep = ",")

class DataReader(): # Created a class to read csv file and place into list


    def __init__(self, fname):  # DatabaseReader constructor
        self.fname = fname;

    def rowList(self):
        with open(self.fname, newline='') as csvfile:
            reader = csv.reader(csvfile)
            dlist = list(reader)
        return dlist

def showData(dlist): # function to show all the rows from dataset
    for row in dlist:
        print(row[2]) # prints all the rows in console

def showNumRows(dlist): # function to count the total number of rows.
    return len(dlist) - 1

def showRow(dlist, row): # function to show specfic row that user wants.
    print(dlist[row])

def showCommodiytOnUOM():
    print(df[df["UOM_ID"] == 205])



def showOnCommodityName():# To select rows whose column value equals a scalar, some_value, use ==:

    commodity_name = input("Enter Commodity Name for which you want to search same commodity values :\n")# Variable assignment

    print(df.loc[df['Commodity'] == commodity_name])# print all rows in which this specific commodity exist

    print("Total Count of data having ", commodity_name, "Commodity name is : ")
    print(df.loc[df.Commodity == commodity_name, 'Commodity'].count())  # find total count



def show_on_UOM(): # To select rows whose column value equals a scalar, some_value, use ==:

    uom_name = input("Enter UOM Name which you want to search") # Variable assignment

    print((df.loc[df['UOM'] == uom_name]))# print all rows in which this specific UOM exist

    print("Total Count of data having ",uom_name,"UOM is : ")

    print(df.loc[df.UOM == uom_name, 'UOM'].count())  # find total count





def total_ref_date():
    ref_date = input("Enter Ref date for which you want to search")  # Variable assignment
    print("Total Count of  Ref Year ", ref_date, " is : ")

    # print([df.REF_DATE == ref_date, 'REF_DATE'].count())  # find total count

def show_on_Food_categories():
    food_categories = input("Enter Food categories Name which you want to search")
    print((df.loc[df['Food categories'] == food_categories]))  # print all rows in which this specific Food categories exist


def main():
    data = DataReader('32100054.csv') # reads the .csv file

    dList = data.rowList()    # Function for Showing the data
    # showData(dList)

    showCommodiytOnUOM()   # Function for Showing all rows Commodity based on UOM

    showOnCommodityName()  #Function for Showing all rows having specific commodity name
    total_ref_date()
    show_on_Food_categories() #function for showing all rows having specific food category


    show_on_UOM()

# this block of code allows running this program from the command line,
# taken from Python's official PyUnit documentation.
# Python Software Foundation. (2015). 26.4.1. Basic example. [Webpage].
# Retrieved from https://docs.python.org/3/library/unittest.html#basic-example.

if __name__ == "__main__":
    # executes if run as main program.
    main()
