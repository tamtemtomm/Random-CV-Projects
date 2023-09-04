from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.yaml')

# Use the model
results = model.train(data="C:\\Users\\HP G7\\Desktop\\IMPORTANT\\KuliahNew\\Side Quest\\Latihan Program\\Personal\\Personal Project\\DSProjects\\CV\\Object Detection\\config.yaml", epochs=3)