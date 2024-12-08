import tkinter as tk
from tkinter import filedialog
from ImageAnalyzer.core.lsb import encode_lsb, decode_lsb

def run_gui():
    def encode():
        input_path = filedialog.askopenfilename(title="Select Input Image")
        output_path = filedialog.asksaveasfilename(title="Save Output Image")
        message = entry_message.get()
        
        if input_path and output_path and message:
            encode_lsb(input_path, output_path, message)
            label_status.config(text="Message encoded successfully!")
    
    def decode():
        input_path = filedialog.askopenfilename(title="Select Image")
        
        if input_path:
            message = decode_lsb(input_path)
            label_status.config(text=f"Decoded Message: {message}")
    
    root = tk.Tk()
    root.title("ImageAnalyzer")
    
    tk.Label(root, text="Message:").pack()
    entry_message = tk.Entry(root)
    entry_message.pack()
    
    tk.Button(root, text="Encode LSB", command=encode).pack()
    tk.Button(root, text="Decode LSB", command=decode).pack()
    
    label_status = tk.Label(root, text="")
    label_status.pack()
    
    root.mainloop()