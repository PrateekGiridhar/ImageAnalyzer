from PIL import Image

def encode_lsb(input_image_path, output_image_path, message):
    img = Image.open(input_image_path)
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '00000000'
    pixels = list(img.getdata())
    
    new_pixels = []
    msg_index = 0
    
    for pixel in pixels:
        if msg_index < len(binary_message):
            r, g, b = pixel[:3]
            r = (r & ~1) | int(binary_message[msg_index])
            msg_index += 1
            new_pixels.append((r, g, b) + pixel[3:])
        else:
            new_pixels.append(pixel)
    
    img.putdata(new_pixels)
    img.save(output_image_path)

def decode_lsb(image_path):
    img = Image.open(image_path)
    pixels = list(img.getdata())
    
    binary_message = ""
    for pixel in pixels:
        r, g, b = pixel[:3]
        binary_message += str(r & 1)
    
    chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    message = ""
    
    for char in chars:
        if char == "00000000":
            break
        message += chr(int(char, 2))
    
    return message
