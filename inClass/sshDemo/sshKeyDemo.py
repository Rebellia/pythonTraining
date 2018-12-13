#!/usr/bin/env python3

import paramiko
import os

#def commandissue(command_x:str) would force the input paramter to be a string
#This would only work in Python 3
def commandissue(command_x, myobj):
   ssh_stdin, ssh_stdout, ssh_stderr = myobj.exec_command(command_x)
   return ssh_stdout.read()

def main():
    sshsession = paramiko.SSHClient()

    #Strip private key out of key file
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")
    
    sshsession.set_mission_host_key_policy(paramiko.AutoAddPolicy())

    sshsession.connect(hostname="10.10.2.3", username="bender", pkey = mykey)

    cmds2issue = ["touch sshworked.txt", "touch otherfile.txt", "touch onemore.dat", "ls"]

    for x in cmds2issue:
        print(commandissue(x,sshsession).decode())
   
    sshsession.close()


main() 
