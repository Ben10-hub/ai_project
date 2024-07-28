import unittest
from scripts.capture_image import capture_image
import os

class TestCaptureImage(unittest.TestCase):
    def test_capture_image(self):
        output_path = '../images/test_image.jpg'
        capture_image(output_path)
        self.assertTrue(os.path.exists(output_path))
        os.remove(output_path)

if __name__ == '__main__':
    unittest.main()
