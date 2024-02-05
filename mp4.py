import cv2
import numpy as np
import glob

img_array = []

# size = (1920, 1080)
size = (1600, 720)
# size = (640, 480)

frame = 0

filename_video_output = "output\\ChatHumain2.avi"

# out = cv2.VideoWriter(filename_video, cv2.VideoWriter_fourcc(*'DIVX'), 50, size)

print(size)

filename = ("C:\\Users\\manue\\EmptyCanvasTest\\"
            "one.empty3.tests.coursecheval.TestChatHumain\\FICHIERS_2024-02-05-11-54-28"
            "\\*.JPG")
for filename_img in glob.glob(filename):
    img = cv2.imread(filename_img)
    if type(img) is not None:
        h, w, c = img.shape
        size = (w, h)

out = cv2.VideoWriter(filename_video_output, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30, size)

print("Construction du tableau d'images")

for filename_img in glob.glob(filename):
    img = cv2.imread(filename_img)
    if type(img) is not None:
        print("Frame ajoutée dans tableau" + filename_img)
        frame = frame + 1
        try:
            out.write(img)
        except:
            print("Image non correcte")

        print("Frame " + str(frame) + " encodée.")

out.release()

print("Terminé.")

print(filename_video_output)
