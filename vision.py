from cscore import CameraServer
import time
import cv2
import numpy as np
from operator import attrgetter



class Particule:
    def __init__(self, cnt):
        self.cnt = cnt
        self.x, self.y, self.w, self.h = cv2.boundingRect(cnt)



def main():
    cs = CameraServer.getInstance()
    cs.enableLogging()

    camera = cs.startAutomaticCapture()
    camera.setResolution(320, 240)
    camera.setFPS(30)
    camera.setBrightness(0)
    camera.setExposureManual(0)
    camera.setWhiteBalanceManual(6000)

    cvSink = cs.getVideo()
 
    outputStream = cs.putVideo("Name", 320, 240)
 
    img = np.zeros(shape=(240, 320, 3), dtype=np.uint8)
 
    while True:
        time, img = cvSink.grabFrame(img)
        if time == 0:
            outputStream.notifyError(cvSink.getError());
            continue



        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        bin = cv2.inRange(hsv, (45, 25, 25), (70, 255, 255)) 

        cnts, _ = cv2.findContours(bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  

        
        particules = list(map(Particule, cnts))
        
        if particules != []:
            max_particule = max(particules, key=attrgetter("h"))
            centre_x = int(max_particule.w/2 + max_particule.x)
            centre_y = int(max_particule.h/2 + max_particule.y)

            norm_x = (centre_x / img.shape[1]) * 2 - 1



        for cnt in cnts:
            [x, y, w, h] = cv2.boundingRect(cnt)
        
            # cv2.drawContours(img, cnt, -1, (0, 0, 255), 1)
            # cv2.rectangle(img, (x,y), (x + w, y + h), (255, 0, 0), 2)
            cv2.circle(img, (centre_x, centre_y), 1, (255, 255, 255), 1)
            cv2.putText(img, str(round(norm_x, 2)), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        outputStream.putFrame(img)