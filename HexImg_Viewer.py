import tkinter as tk
from tkinter import filedialog, Canvas

class HexImageViewer:
    def __init__(self, master):
        self.master = master
        self.master.title("HEX Image Viewer")
        self.master.geometry("800x600")
        
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)
        
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open HEX Image", command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.quit)
        
        self.canvas = Canvas(self.master, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("HEX Image files", "*.heximg")])
        if file_path:
            self.display_hex_image(file_path)
    
    def display_hex_image(self, file_path):
        with open(file_path, 'r') as file:
            dimensions = file.readline().strip().split()
            width, height = int(dimensions[0]), int(dimensions[1])
            hex_data = [line.strip() for line in file.readlines()]
            
        self.canvas.config(width=width, height=height)
        self.canvas.delete("all")
        
        for y in range(height):
            for x in range(width):
                hex_color = hex_data[y * width + x]
                self.canvas.create_rectangle(
                    x, y, x+1, y+1, outline=hex_color, fill=hex_color
                )

def main():
    root = tk.Tk()
    app = HexImageViewer(root)
    root.mainloop()

if __name__ == "__main__":
    main()

