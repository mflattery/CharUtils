# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 18:43:29 2019

@author: mflattery
"""
from subprocess import Popen, PIPE

def ExecATAC():
        p = Popen('atac_8p1_win.exe ATAC.inp',stdout=PIPE,stderr=PIPE)
        out, err=p.communicate()

        for line in err.split(b'\r\n'):
            print(line)
        for line in out.split(b'\r\n'):
            print(line)