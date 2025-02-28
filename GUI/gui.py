
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import subprocess
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets")

window = Tk()

def open_cookies_page():
    window.destroy()  # Close the current window
    subprocess.run(["python", "gui1.py"])  # Open the cookies page

def open_config_page():
    window.destroy()  # Close the current window
    subprocess.run(["python", "gui2.py"])  # Open the config page

def run():
    subprocess.run(["python", "main.py"])



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window.geometry("512x384")
window.configure(bg = "#132020")


canvas = Canvas(
    window,
    bg = "#132020",
    height = 384,
    width = 512,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    5.0,
    5.0,
    anchor="nw",
    text="@spit-fires",
    fill="#E9F2F1",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    439.0,
    5.0,
    anchor="nw",
    text="@efenatuyo",
    fill="#E9F2F1",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    31.0,
    46.0,
    anchor="nw",
    text="XOLO UGC SNIPER",
    fill="#FFFFFF",
    font=("Inter", 50 * -1)
)

run_image = PhotoImage(
    file=relative_to_assets("run.png"))
run_button = Button(
    image=run_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: run(),
    relief="flat"
)
run_button.place(
    x=192.0,
    y=192.0,
    width=128.0,
    height=64.0
)

cookies_image = PhotoImage(
    file=relative_to_assets("cookies.png"))
cookies_button = Button(
    image=cookies_image,
    borderwidth=0,
    highlightthickness=0,
    command=open_cookies_page,
    relief="flat"
)
cookies_button.place(
    x=39.0,
    y=192.0,
    width=128.0,
    height=64.0
)

config_image = PhotoImage(
    file=relative_to_assets("config.png"))
config_button = Button(
    image=config_image,
    borderwidth=0,
    highlightthickness=0,
    command=open_config_page,
    relief="flat"
)
config_button.place(
    x=345.0,
    y=192.0,
    width=136.0,
    height=64.0
)
window.resizable(False, False)
window.mainloop()
