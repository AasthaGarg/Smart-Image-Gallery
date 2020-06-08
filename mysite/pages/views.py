from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login
import os
import math
from django.shortcuts import render, HttpResponse, redirect
import face_recognition
import cv2
from .forms import *
import numpy as np
from tkinter.filedialog import askopenfilename
def facedect(loc):
        cam = cv2.VideoCapture(0)
        s, img = cam.read()
        if s:
                cv2.namedWindow("cam-test")
                cv2.imshow("cam-test", img)
                # cv2.waitKey(0)
                cv2.destroyWindow("cam-test")
                cv2.imwrite("filename.jpg", img)

                BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                MEDIA_ROOT = os.path.join(BASE_DIR, 'pages')
                print(MEDIA_ROOT, loc)
                loc = (str(MEDIA_ROOT) + loc)
                print(loc)
                print("E:\final_project\Face-Recognition-Login-System-master\djangoproject\mysite\pages")
                face_1_image = face_recognition.load_image_file(loc)
                face_1_face_encoding = face_recognition.face_encodings(face_1_image)[0]
                small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

                rgb_small_frame = small_frame[:, :, ::-1]

                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                check = face_recognition.compare_faces(face_1_face_encoding, face_encodings)

                print(check)
                if check[0]:
                        return True

                else:
                        return False



def about(request):
    return render(request,"about.html",{})




  #NOW HERE IS WHERE I WANT TO WRITE THE CODE THAT SAVE THE IMAGE INTO THE FOLDER I JUST CREATED




def base(request):
        if request.method =="POST":
                form =LoginForm(request.POST)
                if form.is_valid():
                        username=request.POST['email']
                        password=request.POST['password']
                        user = authenticate(request,username=username,password=password)
                        if user is not None:
                                if facedect(user.userprofile.head_shot.url):
                                        login(request,user)
                                return redirect('index')
                        else:
                                return redirect('index')        
        else:
                MyLoginForm = LoginForm()
                return render(request,"base.html",{"MyLoginForm": MyLoginForm})  

def home(request):
   return render(request, 'home.html', {})

def edit(request):
        return render(request,'edit.html',{})



def choose(request):
        filename=askopenfilename(filetypes=[("E:/final_project/Face-Recognition-Login-System-master/djangoproject/mysite/pages/","*.jpg")])
        img=cv2.imread(filename)
        img = cv2.resize(img,(400,400))
        cv2.imwrite('E:/final_project/Face-Recognition-Login-System-master/djangoproject/mysite/static/images/mimg.jpg',img)
        #cv2.imshow('img', img)
        return redirect('edit')
def blur(request):
        img=cv2.imread('E:/final_project/Face-Recognition-Login-System-master/djangoproject/mysite/static/images/mimg.jpg',cv2.IMREAD_GRAYSCALE)
        height = img.shape[0]
        width = img.shape[1]

        threshold = 150

        for i in np.arange(3, height - 3):
                for j in np.arange(3, width - 3):
                        sum = 0
                        for k in np.arange(-3, 4):
                                for l in np.arange(-3, 4):
                                        a = img.item(i + k, j + k)
                                        sum = sum + a
                        b = int(sum / 49.0)
                        img.itemset((i, j), b)
        cv2.imwrite(
                'E:\final_project\Face-Recognition-Login-System-master\djangoproject\mysite\static\images\img_blur.jpg',
                img)

        cv2.imshow('img_blur', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return redirect('edit')
# Create your views here.

#from django.contrib.auth.forms import UserCreationForm
def rotate(request):
        image = cv2.imread(
                'E:/final_project/Face-Recognition-Login-System-master/djangoproject/mysite/static/images/mimg.jpg')

        rows, cols = image.shape[:2]
        # (col/2,rows/2) is the center of rotation for the image
        # M is the cordinates of the center
        M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 180, 1)
        dst = cv2.warpAffine(image, M, (cols, rows))
        cv2.imshow('image3', dst)

        # saving image
        cv2.imwrite('rotation.jpeg', dst)

        # so that the image stays
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return redirect('edit')
def bright(request):
        img = cv2.imread(
                'E:/final_project/Face-Recognition-Login-System-master/djangoproject/mysite/static/images/mimg.jpg',cv2.IMREAD_GRAYSCALE)
        height = img.shape[0]
        width = img.shape[1]

        brightness = 50

        for i in np.arange(height):
                for j in np.arange(width):
                        a = img.item(i, j)
                        b = a + brightness
                        if b > 255:
                                b = 255
                        img.itemset((i, j), b)
        cv2.imwrite('img_bright.jpeg', img)

        cv2.imshow('img_bright', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return redirect('edit')
def face(request):
        face_cascade = cv2.CascadeClassifier("E:/final_project/Face-Recognition-Login-System-master/djangoproject/mysite/pages/haarcascade_frontalface_default.xml")
        img = cv2.imread(
                'E:/final_project/Face-Recognition-Login-System-master/djangoproject/mysite/static/images/mimg.jpg')
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=5)

        for x, y, w, h in faces:
                img = cv2.rectangle(img, (x, y), (x + w, y + w), (0, 255, 0), 3)

        cv2.imshow("face_detection", img)

        cv2.imwrite('face_detection.jpeg', img)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return redirect('edit')
def contrast(request):
        img = cv2.imread(
                'E:/final_project/Face-Recognition-Login-System-master/djangoproject/mysite/static/images/mimg.jpg',cv2.IMREAD_GRAYSCALE)
        height = img.shape[0]
        width = img.shape[1]

        contrast = 1.3

        for i in np.arange(height):
                for j in np.arange(width):
                        a = img.item(i, j)
                        b = math.ceil(a * contrast)
                        if b > 255:
                                b = 255
                        img.itemset((i, j), b)
        cv2.imwrite('img_contrast.jpeg', img)

        cv2.imshow('contrast', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return redirect('edit')
def mirror(request):
        img = cv2.imread(
                'E:/final_project/Face-Recognition-Login-System-master/djangoproject/mysite/static/images/mimg.jpg')
        img = cv2.flip(img, 1)

        cv2.imwrite('img_mirror.jpeg', img)

        cv2.imshow('img_mirror', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return redirect('edit')
def index(request):
    return render(request,"index.html",{})


def common(request):
        return render(request,'common.html',{})