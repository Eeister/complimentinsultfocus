import cv2
import numpy as np
import simpleaudio as sa 
import random
import os
from pathlib import Path
from playsound import playsound
import time

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

cap = cv2.VideoCapture(0)

compliments = os.listdir("complimentfiles")
insults = os.listdir("insultfiles")
datacompfolder = Path("complimentfiles")
datainsultfolder = Path("insultfiles")

while True:
    ret, img = cap.read()
    num = random.randrange(0,len(compliments))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3,5)

    cv2.imshow("img",img)
    k = cv2.waitKey(30) & 0xff

    #for (x,y,w,h) in faces:
        #rect = cv2.rectangle(img, (x,y), (x+w, y+h), (255,122,0),2)

    if np.any(faces) == True:
        #playsound(("complimentfiles/" +compliments[num]))
        wave_obj = sa.WaveObject.from_wave_file(str(datacompfolder / compliments[num]))
        play_obj = wave_obj.play()
        play_obj.wait_done()
    elif np.any(faces) == False:
        wave_obj = sa.WaveObject.from_wave_file(str(datainsultfolder / insults[num]))
        play_obj = wave_obj.play()
        play_obj.wait_done()

    if k == 27:
        break



#developed with help based on https://www.youtube.com/watch?v=88HdqNDQsEk&t=557s
