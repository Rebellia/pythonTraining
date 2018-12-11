#!/usr/bin/env python3

import shutil
import os


os.chdir('/home/student/pythonTraining/lab9_moving')

shutil.move('object2.obj', 'lab9_storage')

newName = input("What is the new name for the first object? ")

shutil.move('lab9_storage/object1.obj', 'lab9_storage/' + newName)
