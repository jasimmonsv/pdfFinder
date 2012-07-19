'''
Created on Jul 13, 2012

@author: J.A. Simmons V
Run this program in the root directory of a collection of PDF files and it will
move all pdf's into a new directory called ./PDF
'''

import os
import shutil

startPath = os.getcwd()
print "Finding PDFs..."
try:
    os.mkdir('./PDF')
    destFolder = os.getcwd()+'./PDF'
except OSError:
    destFolder = os.getcwd()+'./PDF'

for root, dirs, files in os.walk('./'):
    for e in files:
        if e.find('.pdf') >0:
            shutil.copy2(root+'/'+e,destFolder)
print "done!"