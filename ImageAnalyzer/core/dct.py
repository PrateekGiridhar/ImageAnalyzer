import cv2
import numpy as np

# Helper function to convert a message into binary
def message_to_binary(message):
    binary = ''.join([format(ord(char), '08b') for char in message])
    return binary

# Helper function to convert binary back to a string
def binary_to_message(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    message = ''.join([chr(int(char, 2)) for char in chars])
    return message

# Encode a secret message into an image using DCT
def encode_dct(input_file, output_file, message):
    # Read the input image
    image = cv2.imread(input_file, cv2.IMREAD_GRAYSCALE)  # Use grayscale for simplicity
    if image is None:
        raise ValueError("Image not found or unable to read.")
    
    # Convert the message to binary and append a delimiter (e.g., '11111111' as EOF marker)
    binary_message = message_to_binary(message) + '11111111'
    
    # Get the height and width of the image
    h, w = image.shape
    
    # Split the image into 8x8 blocks and apply DCT
    encoded_image = np.zeros_like(image, dtype=np.float32)
    idx = 0  # Index to track which bit of the message we're embedding
    
    for i in range(0, h, 8):
        for j in range(0, w, 8):
            if i + 8 > h or j + 8 > w:
                continue
            
            block = image[i:i+8, j:j+8]
            dct_block = cv2.dct(np.float32(block))  # Apply DCT
            
            # Modify the least significant bit of the DC coefficient to embed the message
            if idx < len(binary_message):
                dc_value = dct_block[0, 0]
                dc_value = int(dc_value) & ~1 | int(binary_message[idx])  # Embed bit in LSB
                dct_block[0, 0] = dc_value
                idx += 1
            
            encoded_block = cv2.idct(dct_block)  # Apply inverse DCT
            encoded_image[i:i+8, j:j+8] = encoded_block
    
    # Clip values to valid range and save the output image
    encoded_image = np.clip(encoded_image, 0, 255).astype(np.uint8)
    cv2.imwrite(output_file, encoded_image)
    print(f"Message encoded and saved to {output_file}")

# Decode a secret message from an image using DCT
def decode_dct(input_file):
    # Read the encoded image
    image = cv2.imread(input_file, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("Image not found or unable to read.")
    
    # Get the height and width of the image
    h, w = image.shape
    
    binary_message = ''
    
    for i in range(0, h, 8):
        for j in range(0, w, 8):
            if i + 8 > h or j + 8 > w:
                continue
            
            block = image[i:i+8, j:j+8]
            dct_block = cv2.dct(np.float32(block))  # Apply DCT
            
            # Extract the least significant bit from the DC coefficient
            dc_value = int(dct_block[0, 0])
            binary_message += str(dc_value & 1)
            
            # Check for EOF marker ('11111111')
            if len(binary_message) % 8 == 0 and binary_message[-8:] == '11111111':
                break
    
        else:
            continue
        break
    
    # Convert binary to a readable string (excluding EOF marker)
    decoded_message = binary_to_message(binary_message[:-8])
    print(f"Decoded Message: {decoded_message}")
    return decoded_message

# Example usage:
if __name__ == "__main__":
    input_image_path = "input_image.jpg"   # Replace with your input file path
    output_image_path = "encoded_image.jpg"
    
    secret_message = "Hello, world!"
    
    print("Encoding...")
    encode_dct(input_image_path, output_image_path, secret_message)
    
    print("Decoding...")
    decode_dct(output_image_path)