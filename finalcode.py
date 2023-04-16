#INITIAL SETUP
#----------------------------------------------------------------
import os
import cv2
from cvzone import HandTrackingModule, overlayPNG
import numpy as np


folderPath = 'frames'
mylist = os.listdir(folderPath)
graphic = [cv2.imread(f'{folderPath}/{imPath}') for imPath in mylist]
intro = graphic[0]
kill = graphic[1]
winner = graphic[2]
cam = cv2.VideoCapture(0)
detector = HandTrackingModule.HandDetector(maxHands=1,detectionCon=0.77)

#sets the minimum confidence threshold for the detection
ret, frame = cam.read()
ref = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
frameDelta = cv2.absdiff(ref, gray)
thresh = cv2.threshold(frameDelta, 20, 255, cv2.THRESH_BINARY)[1]
change = np.sum(thresh)

#INITILIZING GAME COMPONENTS
#----------------------------------------------------------------

#INTRO SCREEN WILL STAY UNTIL Q IS PRESSED

while True:
    cv2.imshow('Cookie Cutter', cv2.resize(intro, (0, 0), fx=0.69, fy=0.69))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

TIMER_MAX = 45
TIMER = TIMER_MAX
maxMove = 6500000
font = cv2.FONT_HERSHEY_SIMPLEX
frameHeight = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
frameWidth = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
gameOver = False
NotWon =True
#GAME LOGIC UPTO THE TEAMS
#-----------------------------------------------------------------------------------------
while not gameOver:
        continue
#LOSS SCREEN
while gameOver == True:
    kill = cv2.imshow("frames/img2.png")
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

if NotWon:
    for i in range(10):
       #show the loss screen from the kill image read before
        cv2.imshow('Cookie-Cutter', cv2.resize(kill, (0, 0), fx=0.69, fy=0.69))
    while True:
        #show the loss screen from the kill image read before and end it after we press q
        cv2.imshow('Cookie-Cutter', cv2.resize(kill, (0, 0), fx=0.69, fy=0.69))
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

else:
#WIN SCREEN
#show the win screen from the winner image read before
    cv2.imshow('Cookie-Cutter', cv2.resize(winner, (0, 0), fx=0.69, fy=0.69))
    cv2.waitKey(125)

    while True:
        #show the win screen from the winner image read before and end it after we press q
        cv2.imshow('Cookie-Cutter', cv2.resize(winner, (0, 0), fx=0.69, fy=0.69))
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()