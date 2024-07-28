import unittest
from scripts.detect_plate import recognize_license_plate

class TestLicensePlateRecognition(unittest.TestCase):
    def test_recognize_license_plate(self):
        image_path = '../images/captured_image.jpg'
        image, plates = recognize_license_plate(image_path)
        self.assertGreater(len(plates), 0, "No plates detected.")

if __name__ == '__main__':
    unittest.main()
