import cv2
import os
import mediapipe as mp
import imutils
import datetime
import time

if not os.path.exists('Rostros detectados'):
    print('Carpeta creada: Rostros detectados')
    os.makedirs('Rostros detectados')

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(2, cv2.CAP_DSHOW)
tiempoA = datetime.datetime.now()
gun = cv2.CascadeClassifier('pistoladetect.xml')


count = 0
with mp_face_detection.FaceDetection(
    min_detection_confidence=0.5) as face_detection:
    

    while True:

        ret, frame = cap.read()
        lectura_frame_exitosa, gundt = cap.read()
        k = cv2.waitKey(1) 
        frame = imutils.resize(frame, width=720)
        frame = cv2.flip(frame, 1)
        height, width, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)        
        results = face_detection.process(frame_rgb)
        bw_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        coordenadas_rostro = gun.detectMultiScale(bw_img)
        Auxframe = frame

        if results.detections is not None:
            for detection in results.detections:
                

                xmin = int(detection.location_data.relative_bounding_box.xmin * width)
                ymin = int(detection.location_data.relative_bounding_box.ymin * height)
                w = int(detection.location_data.relative_bounding_box.width * width)
                h = int(detection.location_data.relative_bounding_box.height * height)
                if xmin < 0 or ymin < 0:
                    continue
                              
                aligned_face = frame[ymin : ymin + h, xmin : xmin + w]
                aligned_face = cv2.resize(aligned_face,(300,300),interpolation = cv2.INTER_CUBIC)
                
                
                font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX 
                dt = str(datetime.datetime.now()) 
                #cv2.rectangle(frame,(0,0),(800,40),(255,255,255),-100)
                aligned_face = cv2.putText(aligned_face, dt, (30, 30), 1, 2, (0, 0, 0), 3, cv2.LINE_8) 
                cv2.putText(frame,'Sujeto',(xmin,ymin-10),2,0.7,(0,255,0),1,cv2.LINE_AA)

                cv2.imshow("aligned_face", aligned_face)
                #cv2.imshow("Frame", frame)

                for(x,y,w,h) in coordenadas_rostro:
                    cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
                    cv2.putText(frame,'Arma',(x,y-10),2,0.7,(0,255,0),1,cv2.LINE_AA)
                    arma = Auxframe[y : y + h , x : x + w]
                    arma = cv2.resize(arma,(300,300),interpolation = cv2.INTER_CUBIC)
                    cv2.imshow("arma_detectada", arma)


                    
                tiempoB = datetime.datetime.now()
                tiempoTranscurrido = tiempoB - tiempoA

                if tiempoTranscurrido.seconds >= 1:
                    count += 1
                    cv2.imwrite('Rostros detectados/rostro_{}.jpg'.format(count),aligned_face)
                    tiempoTranscurrido = 0 
                    tiempoA = datetime.datetime.now()
                    key = cv2.waitKey(1)  


                mp_drawing.draw_detection(frame, detection,
                    mp_drawing.DrawingSpec(color=(0, 0,255), circle_radius=1),
                    mp_drawing.DrawingSpec(color=(0, 255, 0)))

                print(count)
                print(tiempoTranscurrido)


        font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX 
        dt = str(datetime.datetime.now()) 
        #cv2.rectangle(frame,(0,0),(800,40),(255,255,255),-100)
        frame = cv2.putText(frame, dt, (100, 30), 1, 2, (0, 0, 0), 2, cv2.LINE_8) 
        cv2.imshow('BRAVO', frame) 
        print(k)
        if k == 27:
            break
            cap.release()
                     
