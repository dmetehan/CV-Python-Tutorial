import numpy as np
import cv2 as cv
import sys


def getting_started_images():
    img = cv.imread("lena.png")
    if img is None:
        sys.exit("Could not read the image.")
    cv.imshow("Display window", img)
    k = cv.waitKey(0)
    if k == ord("s"):
        cv.imwrite("lena.jpg", img)


def image_processing(frame, depth=0):
    if depth == 1:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        w, h = gray.shape
        return gray
    elif depth == 2:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        gray_upside_down = gray[::-1, :]
        combined = cv.add(gray, gray_upside_down)
        return combined
    elif depth == 3:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        gray_upside_down = gray[::-1, :]
        combined = cv.addWeighted(gray, 0.5, gray_upside_down, 0.5, 0)
        return combined
    elif depth == 4:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        edge_detected = cv.Canny(gray, 50, 150)
        return edge_detected
    return frame


def getting_started_videos():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    depth = 0
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        processed = image_processing(frame, depth=depth)
        # Display the resulting frame
        cv.imshow('frame', processed)
        key = cv.waitKey(1)
        if key == ord('q'):
            break
        if key == ord('n'):
            depth += 1
    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    # getting_started_images()
    getting_started_videos()
