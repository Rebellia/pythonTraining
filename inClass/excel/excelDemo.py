#!/usr/bin/env python3
"""Excel spreadsheet maker...now with functions!"""

import pyexcel

#request data from user
def get_ip_data():
    input_ip = input("\nWhat is the IP address? ")
    input_vendor = input("What is the vendor assoc. with this IP? ")

    #place data from user into organized structure (dict)
    d = {"IP": input_ip, "vendor": input_vendor}
    return d


## Main function (This is our runtime code)
def main():
    mylistdict = []
    print("Welcome to the *.xls maker")


    while(True):
       mylistdict.append(get_ip_data())
       keepgoing = input("Would you like to add another entry? Press 'q' to quit: ")
       
       if keepgoing.lower() == 'q':
          break
    
    #place single dict in a list, this list will be our excel sheet

    ##code to create excel file

    #ask user what xls file should be named -- we'll add the .xls extension
    filename = input("\nWhat would you like to name the file? Don't include the .xls ")
    filename = filename + ".xls"

    #save xls to local older
    pyexcel.save_as(records=mylistdict, dest_file_name=filename)

if __name__ == "__main__":
   main()
