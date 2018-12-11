#!/usr/bin/env python3

import shutil
import os

os.chdir('/home/student/pythonTraining')

shutil.copy('copy_files_folders/copyFiFo.txt','copy_files_folders/copyFiFo.txt.copy')

shutil.copytree('copy_files_folders','copy_files_folders_backup')
