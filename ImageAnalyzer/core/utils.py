# Utility functions for image/audio processing

def convert_to_binary(data):
    return ''.join(format(byte, '08b') for byte in data)

def binary_to_string(binary_data):
    chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    return ''.join(chr(int(char, 2)) for char in chars if char != "00000000")
