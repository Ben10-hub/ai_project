import unittest
import cv2
from scripts.detect_green_plate import detect_green_plate

class TestDetectGreenPlate(unittest.TestCase):
    def test_detect_green_plate(self):
        image_path = '../images/captured_image.jpg'
        frame = cv2.imread(image_path)
        plates = [(50, 50, 200, 50)]  # Example plate location
        green_plate = detect_green_plate(frame, plates)
        self.assertIsNotNone(green_plate, "No green plate detected.")

if __name__ == '__main__':
    unittest.main()
