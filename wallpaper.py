import os
import ctypes

SPI_SETDESKWALLPAPER = 20

def set_wallpaper(image_path):
    result = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

if __name__ == "__main__":
    script_dir = os.getcwd() 
    image_path = os.path.join(script_dir, "sg.png")  
    set_wallpaper(image_path)
