from ultralytics import YOLO
import torch


if __name__ == "__main__":
    model = YOLO("yolov8n.yaml")

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    print(device)


    results = model.train(data="config.yaml", epochs=100, device=device)