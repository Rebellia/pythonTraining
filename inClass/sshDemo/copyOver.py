#!/usr/bin/env python3
import paramiko
import os

t = paramiko.Transport("10.10.2.3", 22) #22 is the standard ssh port

#Move past the fact that you're not in the authorized hosts list
#This wasn't working in class for some reason
#t.set_missing_host_key(paramiko.AutoAddPolicy())

t.connect(username='bender', password='alta3')

sftp = paramiko.SFTPClient.from_transport(t)

# os.listdir() #iterate on a directory of contents
# os.path.isdir) #return true/false if an item is a dir
# sftp.put() #moves something to the connected target

#Iterate through a target directory
for item in os.listdir("home/student/files2copy"):
    #Is the item we're iterating on a fild or a folder?
    if not os.path.isdir("/home/student/files2copy/"+x):
        #if a file move to bender box
        sftp.put("/home/student/files2copy/"+item, "/newDir/"+item)

sftp.close() #close the ftp session

t.close() #close the ssh
