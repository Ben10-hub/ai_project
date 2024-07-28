import cv2

def detect_green_plate(frame, plates):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    green_lower = (36, 25, 25)
    green_upper = (86, 255, 255)
    mask = cv2.inRange(hsv, green_lower, green_upper)
    green_plate = None
    for (x, y, w, h) in plates:
        plate_img = frame[y:y+h, x:x+w]
        plate_hsv = cv2.cvtColor(plate_img, cv2.COLOR_BGR2HSV)
        plate_mask = cv2.inRange(plate_hsv, green_lower, green_upper)
        if cv2.countNonZero(plate_mask) > 0:
            green_plate = (x, y, w, h)
            break
    return green_plate
