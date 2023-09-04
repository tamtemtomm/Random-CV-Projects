import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np
import math
import argparse
import os

reader = easyocr.Reader(['en'], gpu=False)
threshold = .25

def subtitle(img, reader):
    full_text = reader.readtext(img)

    for _, t in enumerate(full_text):
        box, text, score = t
        if score > threshold :
            print(t)
            
            box = [
                [math.floor(box[0][0]), math.floor(box[0][1])],
                [math.floor(box[1][0]), math.floor(box[1][1])],
                [math.floor(box[2][0]), math.floor(box[2][1])],
                [math.floor(box[3][0]), math.floor(box[3][1])],
            ]
            box = np.array(box)
            
            cv2.drawContours(img, [box], -1, (0,255,0), 3)
            cv2.putText(img, text, [math.floor(box[0][0]), math.floor(box[0][1])], cv2.FONT_HERSHEY_COMPLEX, .65, (255, 0, 0), 2)
        
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

arg = argparse.ArgumentParser()
arg.add_argument("--mode", default='webcam')
arg.add_argument("--input", default='image.jpg')
arg = arg.parse_args()

output_dir = './output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

if arg.mode in ["image"] :
    img = cv2.imread("./image.jpg")
    img = subtitle(img, reader)
    
    cv2.imwrite(os.path.join(output_dir, 'output.png'), img)
    plt.imshow(img)
    plt.show()

elif arg.mode in ["video"] :
    cap = cv2.VideoCapture(arg.input)
    ret, frame = cap.read()
    
    output = cv2.VideoWriter(os.path.join(output_dir, 'output.mp4'),
                                 cv2.VideoWriter_fourcc(*'MP4V'),
                                 25,
                                 (frame.shape[1], frame.shape[0]))
    
    while ret:
            frame = subtitle(frame, reader)
            output.write(frame)
            ret, frame = cap.read()
        
    cap.release()
    output.release()

elif arg.mode in ['webcam'] :
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    
    while ret :
        frame = subtitle(frame, reader)
        cv2.imshow("frame", frame)
        cv2.waitKey(25)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        ret, frame = cap.read()
        
    cap.release()

        
