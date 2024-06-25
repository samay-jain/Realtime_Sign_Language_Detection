import cv2
import os
import time
import uuid


imagesPath = 'RealTimeObjectDetection/Tensorflow/workspace/images/collectedimages'
os.makedirs(imagesPath, exist_ok=True)


labels = ['hello', 'bye', 'done', 'review', 'thanks']
noImages = 15

for label in labels:
    labelPath = os.path.join(imagesPath, label)
    os.makedirs(labelPath, exist_ok=True)    

    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)

    for imgnum in range(noImages):
        ret, frame = cap.read()
        imageName = os.path.join(imagesPath, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imageName, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if(cv2.waitKey(1) and 0xFF==ord('q')):
            break
    cap.release()