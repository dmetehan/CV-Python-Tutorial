import sys
import cv2 as cv
import numpy as np


def image_processing(frame, depth=0, prev=None):
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
    elif depth == 5:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        hsv = np.zeros_like(frame)
        hsv[..., 1] = 255
        flow = cv.calcOpticalFlowFarneback(cv.cvtColor(prev, cv.COLOR_BGR2GRAY), gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        mag, ang = cv.cartToPolar(flow[..., 0], flow[..., 1])
        hsv[..., 0] = ang * 180 / np.pi / 2
        hsv[..., 2] = cv.normalize(mag, None, 0, 255, cv.NORM_MINMAX)
        bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
        return bgr
    elif depth == 6:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        hsv = np.zeros_like(frame)
        hsv[..., 1] = 255
        flow = cv.calcOpticalFlowFarneback(cv.cvtColor(prev, cv.COLOR_BGR2GRAY), gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        mag, ang = cv.cartToPolar(flow[..., 0], flow[..., 1])
        hsv[..., 0] = ang * 180 / np.pi / 2
        hsv[..., 2] = cv.normalize(mag, None, 0, 255, cv.NORM_MINMAX)
        bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
        combined = cv.addWeighted(frame, 1, bgr, 0.5, 0)
        return combined
    return frame


def getting_started_videos():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    depth = 0
    prev = None
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        processed = image_processing(frame, depth=depth, prev=prev)
        # Display the resulting frame
        cv.imshow('frame', processed)
        key = cv.waitKey(1)
        if key == ord('q'):
            break
        if key == ord('n'):
            depth += 1
        prev = frame
    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()


def getting_started_images():
    img = cv.imread("lena.png")
    if img is None:
        sys.exit("Could not read the image.")
    cv.imshow("Display window", img)
    k = cv.waitKey(0)
    if k == ord("s"):
        cv.imwrite("lena.jpg", img)


if __name__ == '__main__':
    # getting_started_images()
    getting_started_videos()
