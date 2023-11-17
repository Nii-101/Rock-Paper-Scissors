from tkinter import *
from PIL import Image, ImageTk
"""Import tkinter library and pillow library to 
allow use of .png for window icon
"""

"""Instantiates a window"""
window = Tk()

"""Setting the size of the window"""
window.geometry("450x450")

"""Setting the title of the window"""
window.title("🔥🔥🔥   ULTIMATE ROCK PAPER SCISSORS    🔥🔥🔥")


"""Changing window icon"""
icon = Image.open("Rock_Paper_Scissors.png")
tk_icon = ImageTk.PhotoImage(icon)
window.iconphoto(True, tk_icon)

""" Making changes to window"""
window.configure(background="black", cursor="shuttle")

window.mainloop()
""" Places the window on the screen"""
