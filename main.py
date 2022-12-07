import pyautogui
import turtle
from PIL import Image
from PIL import ImageGrab

def getColor(img,x,y):
    # bbox = (x, y, x+1, y+1)
    r,g,b,s = img.getpixel((x,y))
    hex_str = '#' + getHex((r,g,b))
    return hex_str
def getHex(rgb):
    return '%02X%02X%02X'%rgb

img =  Image.open("color.png")
scren_x, scren_y = pyautogui.size()
new_img = img.resize((scren_x,scren_y))


win = turtle.Screen()
win.title('ColorHue')
while True:
    x, y = pyautogui.position()
    hex_str = getColor(new_img, x, y)
    win.bgcolor(hex_str)
