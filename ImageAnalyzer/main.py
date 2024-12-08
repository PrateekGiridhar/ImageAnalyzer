from ImageAnalyzer.core.lsb import encode_lsb, decode_lsb
from stegsolve.gui.gui_main import run_gui

def main():
    print("Welcome to Stegsolve Clone!")
    print("1. Run GUI")
    print("2. Encode LSB")
    print("3. Decode LSB")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        run_gui()
    elif choice == "2":
        input_image = input("Enter the path to the input image: ")
        output_image = input("Enter the path to save the output image: ")
        message = input("Enter the message to hide: ")
        encode_lsb(input_image, output_image, message)
        print("Message encoded successfully!")
    elif choice == "3":
        input_image = input("Enter the path to the image: ")
        message = decode_lsb(input_image)
        print(f"Decoded message: {message}")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
