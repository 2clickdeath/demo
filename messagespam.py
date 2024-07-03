import tkinter as tk
import random

def create_error_boxes():
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    box_width = 200
    box_height = 100
    num_boxes_x = screen_width // box_width
    num_boxes_y = screen_height // box_height

    for y in range(num_boxes_y):
        for x in range(num_boxes_x):
            box = tk.Toplevel()
            box.geometry(f"{box_width}x{box_height}")
            box.title("Error")
            label = tk.Label(box, text="SIGMA GANG NIGGA ^.^")
            label.pack(pady=20)

            box_x = x * box_width
            box_y = screen_height - (y * box_height) - box_height
            box.geometry(f"+{box_x}+{box_y}")

            move_error_box(box)

def move_error_box(box):
    x, y = map(int, box.geometry().split('+')[1:])
    if y > -100:  
        box.geometry(f"+{x}+{y - 10}")
        root.after(50, move_error_box, box)
    else:
        box.destroy()
        recreate_error_box()

def recreate_error_box():
    box = tk.Toplevel()
    box.geometry("200x100")
    box.title("Error")
    label = tk.Label(box, text="SIGMA GANG NIGGA ^.^")
    label.pack(pady=20)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    box_x = random.randint(0, screen_width - 200)
    box_y = screen_height
    box.geometry(f"+{box_x}+{box_y}")

    move_error_box(box)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  
    create_error_boxes()

    root.mainloop()
