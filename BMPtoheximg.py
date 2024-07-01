import tkinter as tk
from tkinter import filedialog

class HexImageConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("BMP to HEX Image Converter")
        self.master.geometry("400x200")
        
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)
        
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open BMP", command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.quit)
        
        self.label = tk.Label(self.master, text="Select a BMP image to convert to HEX format", pady=20)
        self.label.pack()

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("BMP files", "*.bmp")])
        if file_path:
            self.convert_to_hex(file_path)

    def convert_to_hex(self, image_path):
        with open(image_path, 'rb') as f:
            # Read BMP header
            f.read(18)
            width = int.from_bytes(f.read(4), byteorder='little')
            height = int.from_bytes(f.read(4), byteorder='little')
            f.read(28)
            
            # Read BMP pixel data
            hex_data = []
            row_padded = (width * 3 + 3) & ~3
            for y in range(height):
                row = []
                for x in range(width):
                    b, g, r = f.read(3)
                    hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
                    row.append(hex_color)
                hex_data.extend(row)
                f.read(row_padded - width * 3)

        hex_file_path = filedialog.asksaveasfilename(defaultextension=".heximg", filetypes=[("HEX Image files", "*.heximg")])
        if hex_file_path:
            with open(hex_file_path, 'w') as file:
                file.write(f"{width} {height}\n")
                for color in hex_data:
                    file.write(f"{color}\n")

def main():
    root = tk.Tk()
    app = HexImageConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
