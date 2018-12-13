#!/usr/bin/env python3
import csv

#myfile = open('zfile.csv', 'r')
#print(myfile.read())
#myfile.close()

#This will automatically close the csv_file
#More likely to run into this code than actually use it at this level
with open('superheros.txt') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=",")
  line_count = 0
  for row in csv_reader:
     if line_count == 0:
        print("Column names are {}".format(",".join(row)))
        line_count = line_count + 1
     else:
        print("\t{} a.k.a. {} has this power:".format(row[0], row[1], row[2]))
        line_count += 1

  print('Processed {} lines'.format(line_count))
