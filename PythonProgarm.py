import cv2
import pytesseract
import os
import glob
import numpy as np
from pdf2image import convert_from_path
from pathlib import Path



#Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

#Working directory
dir = os.path.dirname(__file__)
#Transcripts is the folder that has the pdfs
files=glob.glob(dir+'\Transcripts\*.pdf')

#To remove the strings of zeroes
zero="0"
unwanted=["0"]
n=30;
for i in range(2,n):
    z=zero.zfill(i)
    unwanted.append(z);




for i in files:
    images = convert_from_path(str(i))#Convert each pdf to images , stored in 'images'
    l=1
    for img in images: 
            text = pytesseract.image_to_string(img, lang='hin')
            lst=[]
            with open(dir+'/TextFiles/'+Path(i).stem+'_'+'page'+str(l)+".txt","w",encoding="utf8") as file: #store the generated text files in folder 'TextFiles'
                text=text[:-1]
                file.write(text)
            with open(dir+'/TextFiles/'+Path(i).stem+'_'+'page'+str(l)+".txt","r",encoding="utf8") as f:    #Remove if the line has zero string
                for line in f:
                    for word in unwanted:
                        if word in line:
                            line=line.replace(word,' ')
                    lst.append(line)
                f.close()
            with open(dir+'/TextFiles/'+Path(i).stem+'_'+'page'+str(l)+".txt","w",encoding="utf8") as f:    #update the file
                for line in lst:
                    f.write(line)
                f.close()
            l=l+1

       

