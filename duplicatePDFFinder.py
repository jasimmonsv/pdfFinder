'''
Created on Jul 13, 2012

@author: J.A. Simmons V
Run this program in the root directory of a collection of PDF files and it will
move all pdf's into a new directory called ./PDF
'''

import os
import sys
import shutil
import random

def copyRandPDF(root,e, destFolder):
    if random.randrange(0,1000)%70 == 0: #this is to grab a small subest of all pdf files available
        shutil.copy2(os.path.join(root,e),destFolder)
        print "!",
        return True
    else: 
        print".",
        return False
    
def copyPDF(root, e, destFolder):
    shutil.copy2(os.path.join(root,e), destFolder)
    print "!",
    return True
 
print "Finding PDFs...",
startPath = os.getcwd()
#Create needed directories
samplePDFDir = '../sPDF'
samplePDFPurDir = '../sPDFPurified'
try:
    os.mkdir(samplePDFDir)
except OSError:
    sys.stderr.write('Directory exists')
finally:    
    destFolder1 = os.path.join(startPath,samplePDFDir)
try:
    os.mkdir(samplePDFPurDir)
except OSError:
    sys.stderr.write('Directory exists')
finally:    
    destFolder2 = os.path.join(startPath,samplePDFPurDir)

#Start the search for pdf's
files1 = []
root1 = []
for root, dirs, files in os.walk(startPath):
    for e in files:
        if e.find('.pdf')>0:
            if copyRandPDF(root, e, destFolder1):
                root1.append(root)
                files1.append(e)                
#start the search for duplicates
print '\nCopying duplicates'
#os.chdir('../PDFPurified')
os.chdir('../PDFPurified')
files2 = []
root2 = []
for root, dirs, files in os.walk(os.getcwd()):
    for e in files:
        if e in files1:
            copyPDF(root,e, destFolder2)

    
    
print "done!"