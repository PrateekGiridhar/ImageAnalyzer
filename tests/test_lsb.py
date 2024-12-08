import unittest
from ImageAnalyzer.core.lsb import encode_lsb, decode_lsb

class TestLSB(unittest.TestCase):
    
    def test_encode_decode(self):
        input_image = "data/sample_image.png"
        output_image = "data/output_image.png"
        test_message = "Hello World!"
        
        encode_lsb(input_image, output_image, test_message)
        decoded_message = decode_lsb(output_image)
        
        self.assertEqual(test_message, decoded_message)

if __name__ == "__main__":
    unittest.main()