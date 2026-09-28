import os
import glob
import cv2
import numpy as np
from PIL import Image

img_array = []

# size = (1600, 720)
#size = (640, 480)
size = (1920*2, 1080*2)

frame = 0

filename_video_output = "output\\MoonRotation4K-1-rotate180.mp4"
output_dir = os.path.dirname(filename_video_output)
if output_dir:
    os.makedirs(output_dir, exist_ok=True)

# out = cv2.VideoWriter(filename_video, cv2.VideoWriter_fourcc(*'DIVX'), 50, size)

print(size)

filename = "D:\\Current\\EmptyCanvasTest\\one.empty3.testagentcode_jvm.MoonRotation4K\\2026-09-26-06-54-29\\"

print(filename)

if os.path.isdir(filename):
    search_pattern = os.path.join(filename, "*")
else:
    search_pattern = filename

# Using sorted() to ensure frames are encoded in alphabetical/numerical order
image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff', 'tif', '.webp')
file_list = sorted([
    f for f in glob.glob(search_pattern)
    if os.path.isfile(f) and f.lower().endswith(image_extensions)
])

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

    # Source - https://stackoverflow.com/q/53724035
    # Posted by 0xEbo, modified by community. See post 'Timeline' for change history
    # Retrieved 2026-07-12, License - CC BY-SA 4.0

    # PIL Image object which holds a transparent background png image.
    pil_img = Image.open(filename_img).convert('RGBA')
    #pil_img.show()

    # Create a solid black background
    background = Image.new('RGBA', pil_img.size, (0, 0, 0, 255))
    # Paste the original image over the black background, using its alpha channel as a mask
    background.paste(pil_img, mask=pil_img)
    background = background.rotate(180)
    # I use numpy to convert the background into a numpy array
    numpy_image = np.array(background)

    # I convert to a openCV2 image, notice the COLOR_RGBA2BGR which means that
    # the color is converted from RGBA to BGR format
    opencvImage = cv2.cvtColor(numpy_image, cv2.COLOR_RGBA2BGR)

    img = opencvImage

    #img = cv2.imread(filename_img, cv2.CV_LOAD_IMAGE_UNCHANGED)
    if img is not None:
        # Ensure the image has the correct size
        h, w, c = img.shape
        #if (w, h) != size:
        #    img = cv2.resize(img, size)

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
