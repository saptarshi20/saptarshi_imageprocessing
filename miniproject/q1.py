from tkinter import *
import tkinter as tk
from tkinter import filedialog,Text
from PIL import Image,ImageTk
import cv2
import numpy as np
import pytesseract as pt
from pytesseract import Output

img=np.zeros((),np.uint8)
new_img=np.zeros((),np.uint8)
text=''
counter=0

root=tk.Tk()
canvas=tk.Canvas(root,height=700,width=700,bg='#00FFFF')
canvas.pack()
frame=tk.Frame(root,bg='black')
frame.place(relwidth=0.6,relheight=0.8,relx=0.2,rely=0.05)
text_box=tk.Frame(frame,bg='#FAEBD7')
text_box.place(relwidth=0.6,relheight=0.6,relx=0.2,rely=0.2)

def open_button_click():
    filename = filedialog.askopenfilename(initialdir = '/Users/Desktop/',title = 'Select an Image',filetypes = (('JPG','*.jpg'),('All files','*.*')))
    print(filename)
    global img,new_img
    img = cv2.imread(filename)
    print(img.shape)
    img=cv2.resize(img,(700,700))
    new_img=img.copy()
    cv2.imshow('frame',img)
    cv2.waitKey(0)

def blur_button_click():
    global new_img,img
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    kernel=np.ones((2,2))
    gaussian_blur=cv2.GaussianBlur(img_gray,(5,5),2)
    new_img=gaussian_blur.copy()
    cv2.imshow('frame',gaussian_blur)

def auto_button_click():
    global new_img,img
    image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    kernel=np.ones((5,5))
    gaussian_blur=cv2.GaussianBlur(image,(5,5),2)
    edge=cv2.Canny(gaussian_blur,40,280)
    contours,hierarchy=cv2.findContours(edge,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    areas=[cv2.contourArea(c) for c in contours]
    max_index=np.argmax(areas)
    max_contour=contours[max_index]
    perimeter=cv2.arcLength(max_contour,True)
    ROI=cv2.approxPolyDP(max_contour,0.01*perimeter,True)
    cv2.drawContours(img,[ROI],-1,(0,255,0),2)
    pts_1=np.array([ROI[0],ROI[1],ROI[3],ROI[2]],np.float32)
    pts_2=np.array([(0,0),(500,0),(0,500),(500,500)],np.float32)
    perspective=cv2.getPerspectiveTransform(pts_1,pts_2)
    transformed=cv2.warpPerspective(img,perspective,(500,500))
    cv2.imshow('output',transformed)

def manual_button_click():
    pts=[]
    def mouse(event,x,y,flags,param):
        global new_img,img
        if event==cv2.EVENT_LBUTTONDOWN:
            pts.append((x,y))
        if len(pts)==4:
            warp(pts)
    def warp(pts):
        global new_img,img
        pts_1=np.array([pts[0],pts[1],pts[3],pts[2]],np.float32)
        pts_2=np.array([(0,0),(500,0),(0,500),(500,500)],np.float32)
        perspective=cv2.getPerspectiveTransform(pts_1,pts_2)
        transformed=cv2.warpPerspective(img,perspective,(500,500))
        new_img=transformed.copy()
        cv2.imshow('frame',transformed)
    cv2.namedWindow('frame')
    cv2.setMouseCallback('frame',mouse)



def ocr_button_click():
    
    global new_img,text
    ret,global_thresh=cv2.threshold(new_img,170,255,cv2.THRESH_BINARY)
    text = pt.image_to_string(global_thresh,lang= 'eng')
    data = pt.image_to_data(global_thresh,output_type= Output.DICT)
    no_word = len(data['text'])
    for i in range(no_word):
        if int(data['conf'][i]) > 50:
            x,y,w,h = data['left'][i],data['top'][i],data['width'][i],data['height'][i]
            cv2.rectangle(global_thresh,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.imshow('frame',global_thresh)
            cv2.waitKey(200)
    'new_img=global_thresh.copy()'


def show_button_click():
    global text
    textbox = tk.Frame(frame,bg = '#FDFFD6')
    textbox.place(relx = 0.2,rely = 0.2,relwidth =0.6,relheight =0.6)
    text_frame = Text(textbox,bg = '#FDFFD6')
    text_frame.insert('1.0',text)
    text_frame.pack()

def save_button_click():
    global counter
    global new_img
    counter+=1
    cv2.imwrite('image_'+str(counter) + '.jpg', new_img) 

def original_img_button_click():
    global new_img
    new_img=img.copy()
    cv2.imshow('frame',img)

def flip_button_click():
    global new_img
    flipped=cv2.flip(new_img,1)
    cv2.imshow('frame',flipped)

def rotate_button_click():
    global new_img
    rotate=cv2.rotate(new_img,cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow('frame',rotate)


def destroy_button_click():
    cv2.destroyAllWindows()

label=tk.Label(frame,text='TEXT DETECTED',fg='black',bg='white',font=('Bold',16))
label.place(relx=0.3,rely=0.1)

openfile = tk.Button(canvas,text = 'Open Image',fg = '#000000',padx = 5,pady = 5, command = open_button_click)
openfile.place(relx=0.04,rely=0.1)

blurimage=tk.Button(canvas,text='Blur Image',fg = '#000000',padx = 5,pady = 5, command = blur_button_click)
blurimage.place(relx=0.038,rely=0.2)

autocrop=tk.Button(canvas,text='Auto Crop',fg = '#000000',padx = 5,pady = 5, command = auto_button_click)
autocrop.place(relx=0.038,rely=0.3)

manualcrop=tk.Button(canvas,text='Manual Crop',fg = '#000000',padx = 5,pady = 5, command = manual_button_click)
manualcrop.place(relx=0.035,rely=0.4)

ocrbutton=tk.Button(canvas,text='OCR',fg = '#000000',padx = 20,pady = 5, command = ocr_button_click)
ocrbutton.place(relx=0.85,rely=0.1)

showtext=tk.Button(canvas,text='Show text',fg = '#000000',padx = 5,pady = 5, command = show_button_click)
showtext.place(relx=0.85,rely=0.2)

saveimage=tk.Button(canvas,text='Save Image',fg = '#000000',padx = 5,pady = 5, command = save_button_click)
saveimage.place(relx=0.85,rely=0.3)

showoriginal=tk.Button(canvas,text='Original Image',fg = '#000000',padx = 5,pady = 5, command = original_img_button_click)
showoriginal.place(relx=0.83,rely=0.4)

flipimage=tk.Button(canvas,text='Flip Image',fg = '#000000',padx = 5,pady = 5, command = flip_button_click)
flipimage.place(relx=0.037,rely=0.5)

rotateimage=tk.Button(canvas,text='Rotate Image',fg = '#000000',padx = 5,pady = 5, command = rotate_button_click)
rotateimage.place(relx=0.84,rely=0.5)

destroywindow=tk.Button(canvas,text='Close windows',fg = '#000000',padx = 8,pady = 8, command = destroy_button_click)
destroywindow.place(relx=0.4,rely=0.88)

root.mainloop()