import os
from ultralytics import YOLO
import cv2


model_path = os.path.join('.', 'runs', 'detect', 'train', 'weights', 'best.pt')
model = YOLO(model_path)


cap = cv2.VideoCapture(0)  # 0 is usually the default camera index


threshold = 0.8

while True:

    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting...")
        break


    results = model(frame)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)


    cv2.imshow('Object Detection', frame)


    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
