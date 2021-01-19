#!/usr/bin/env python
# coding: utf-8


import cv2
from mtcnn import MTCNN

cap = cv2.VideoCapture(0)
detector = MTCNN()


while True:
    ret, img = cap.read()
    # image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    image = img
    result = detector.detect_faces(image)
    if result:
        for person in result:
            bounding_box = person["box"]
            keypoints = person["keypoints"]

            cv2.rectangle(
                image,
                (bounding_box[0], bounding_box[1]),
                (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]),
                (0, 155, 255),
                2,
            )

            cv2.circle(image, (keypoints["left_eye"]), 2, (0, 155, 255), 2)
            cv2.circle(image, (keypoints["right_eye"]), 2, (0, 155, 255), 2)
            cv2.circle(image, (keypoints["nose"]), 2, (0, 155, 255), 2)
            cv2.circle(image, (keypoints["mouth_left"]), 2, (0, 155, 255), 2)
            cv2.circle(image, (keypoints["mouth_right"]), 2, (0, 155, 255), 2)
            cv2.imshow("image", image)
    else:
        print('No faces found!')
        break
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
