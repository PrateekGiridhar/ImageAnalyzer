import unittest
from ImageAnalyzer.core.dct import encode_dct, decode_dct

class TestDCT(unittest.TestCase):

    def test_encode_decode_dct(self):
        input_file = "data/sample_image.png"
        output_file = "data/output_image_dct.png"
        test_message = "DCT Test Message"

        # Assuming encode_dct and decode_dct are implemented
        encode_dct(input_file, output_file, test_message)
        decoded_message = decode_dct(output_file)

        self.assertEqual(test_message, decoded_message)

if __name__ == "__main__":
    unittest.main()