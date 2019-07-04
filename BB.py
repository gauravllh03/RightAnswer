import numpy as np

import cv2

import pyautogui

import pytesseract

import requests

from bs4 import BeautifulSoup as BS

from nltk.corpus import stopwords

from PIL import Image

stopw=(stopwords.words('english'))

stopw=[e for e in stopw if e not in ['most','before','after','more']]

s=set(stopw)

 

 

#print (s)

#pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

 

while 1:

    input()

   

    image=pyautogui.screenshot(region=(1400,210,520,300))

    new_size=tuple(3*x for x in image.size)

    image=image.resize(new_size,Image.ANTIALIAS)

    image=cv2.cvtColor(np.array(image),cv2.COLOR_RGB2GRAY)

    ret,image= cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)

    #cv2.imshow("//test.png",image)

    text=pytesseract.image_to_string(image)

 

    text=text.splitlines()

    print(text)

    text=list(filter(lambda x:x.strip(),text))

    print(text)

    ans_3=text[-1].lower()

 

    ans_2=text[-2].lower()

    ans_1=text[-3].lower()

 

    ques=""

    for i in range(len(text)-3):

        ques+=text[i]+" "

    ques=ques.lower().strip()

    ques=list(filter(lambda w: not w in s,ques.split()))

    question=""

    for a in ques:

        question+=a+" "

    print(question,"\n")

    print(ans_1,"\n")

    print(ans_2,"\n")

    print(ans_3,"\n")

 

    search=""

    keyword=question.replace(" ","+")

    google_search="https://www.google.co.in/search?sclient=psy-ab&client=ubuntu&hs=k5b&channel=fs&biw=1366&bin=648&noj=1&q="+keyword

    r=requests.get(google_search)

    print(r)

    soup=BS(r.text,"html.parser")

    url=soup.find_all('span',{"class":"st"})

    for u in url:

        search+=(u.text.lower())+" "

    l=[]

    l= (list(filter(lambda w: not w in s,search.split())))

    g_search=""

    for a in l:

        g_search+=a+" "

    #print(g_search)

    c1=0

    c2=0

    c3=0

    print("\n\n")

    for i in ans_1.split(' '):

        if i=='the' :

            ans_1.replace(i,'')

            continue

        c1+=search.count(i)

        print(i,search.count(i))

    for i in ans_2.split(' '):

        if i=='the':

            ans_2.replace(i,'')

            continue

        c2+=search.count(i)

        print(i,search.count(i))

    for i in ans_3.split(' '):

        if i=='the':

            ans_3.replace(i,'')

            continue

        c3+=search.count(i)

        print(i,search.count(i))

 

    print(c1)

    print(c2)

    print(c3)

 

 

    max1=max((c1,c2,c3))

    if max1==c1:

        print("Correct answer is : a)",ans_1)

    if max1==c2:

        print("Correct answer is : b)",ans_2)

    if max1==c3:

        print("Correct answer is : c)",ans_3)

 

