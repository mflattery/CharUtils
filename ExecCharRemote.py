# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 14:03:56 2019

@author: mflattery
"""
import paramiko
import sys
def ExecCharRemote(nproc,chardir=r'/mnt/nfs/home/mflattery/work/VGamma/HeatShield/CHAR2D/CHAR'):
    
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('fleetwood-linux', username='mflattery', password='toyon101')
    cmd='cd {} ; mpirun -np {} char CharWork.inp'.format(chardir,nproc)
    stdin, stdout, stderr = client.exec_command(cmd)
 
    errline=[]
    stdline=[]
    for line in stdout:
        stdline.append( line.strip('\n'))
    for line in stderr:
        errline.append( line.strip('\n'))
        
    if errline:        

        for line in errline:
            print( line.strip('\n'))
        sys.exit('Char Crash')
        client.close()        
    client.close()
    

