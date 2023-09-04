import cv2
from ultralytics import YOLO

# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model_path = 'C:\\Users\\HP G7\\Desktop\\IMPORTANT\\KuliahNew\\Side Quest\\Latihan Program\\Personal\\Personal Project\\DSProjects\\CV\\Object Detection\\best.pt'
images_path = 'C:\\Users\\HP G7\\Desktop\\IMPORTANT\\KuliahNew\\Side Quest\\Latihan Program\\Personal\\Personal Project\\DSProjects\\CV\\Object Detection\\images.jpg'

model = YOLO(model_path)

threshold = 0.1
img = cv2.imread(images_path)
results = model(img)[0]
# print(results[0])
for result in results.boxes.data.tolist():
    x1, y1, x2, y2, score, class_id = result
    # print(x1, y1, x2, y2)
    if score > threshold:
            cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(img, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
cv2.imwrite('C:\\Users\\HP G7\\Desktop\\IMPORTANT\\KuliahNew\\Side Quest\\Latihan Program\\Personal\\Personal Project\\DSProjects\\CV\\Object Detection\\images2.jpg', img)