import os
from ultralytics import YOLO
import cv2

model_path = 'C:\\Users\\HP G7\\Desktop\\IMPORTANT\\KuliahNew\\Side Quest\\Latihan Program\\Personal\\Personal Project\\DSProjects\\CV\\Object Detection\\best.pt'

model = YOLO(model_path)
threshold = 0.5

cap = cv2.VideoCapture(0)
cv2.namedWindow('Object Dist Measure ', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Object Dist Measure ', 700, 600)

while True:
    ret, frame = cap.read()
    results = model(frame)[0]
    
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
    
    cv2.imshow('Object Dist Measure ',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()