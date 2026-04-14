import cv2
import numpy as np
import glob

img_array = []

# size = (1920, 1080)
# size = (1600, 720)
size = (640, 480)

frame = 0

filename_video_output = "output\\morphing.mp4"

# out = cv2.VideoWriter(filename_video, cv2.VideoWriter_fourcc(*'DIVX'), 50, size)

print(size)

filename = ("D:\\Current\\autosave\\*.JPG")
# Using sorted() to ensure frames are encoded in alphabetical/numerical order
file_list = sorted(glob.glob(filename))

for filename_img in file_list:
    img = cv2.imread(filename_img)
    if img is not None:
        h, w, c = img.shape
        size = (w, h)
        break  # We only need the size from the first valid image

# Changed fourcc to *'mp4v' which is standard for .mp4 files
out = cv2.VideoWriter(filename_video_output, cv2.VideoWriter_fourcc(*'mp4v'), 30, size)

print("Construction du tableau d'images")

for filename_img in file_list:
    img = cv2.imread(filename_img)
    if img is not None:
        # Ensure the image has the correct size
        h, w, c = img.shape
        if (w, h) != size:
            img = cv2.resize(img, size)

        print("Frame ajoutée dans tableau " + filename_img)
        frame = frame + 1
        try:
            out.write(img)
            print("Frame " + str(frame) + " encodée.")
        except Exception as e:
            print("Image non correcte:", e)

# IMPORTANT: The video writer must be released to correctly save the file header
out.release()

print("Terminé.")

print(filename_video_output)
