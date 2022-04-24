import os

import imageio
import imageio as iio
from imageio.core import Image

directory = "C:\\Users\\manue\\EmptyCanvasTest\\"
dir = "C:\\Users\\manue\\EmptyCanvasTest\\one.empty3.testscopy.tests.test3.TestPolygons\FICHIERS_2022-04-24-09-28-11\\"#FICHIERS_2022-04-24-09-58-52
filesInDir = os.listdir(dir)
writer = iio.get_writer(directory+"out-chat1" + ".mp4", fps=25)
for image in filesInDir:
    print(image)
    if not image.lower().endswith(".jpg"):
        print("Can't get data for image: " + image)
        continue
    # filename = directory + "/image__" + str(i) + ".jpg"
    # f = open(filename, "wb")
    # f.write(im)
    # f.close()
    # print(filename)
    #
    # image = Image.open(filename).convert('RGB')
    # print(image.size)
    #
    # resized_image = image.resize((1920, 1080))
    # print(resized_image.size)
    #
    # resized_image.save(filename)
    else:
        try:
            img3 = iio.imread(dir + image)
            # for r in range(25):
            writer.append_data(img3)
            # 1 -> 3 ?
        except ValueError:
            print("Error reading stored file")
        # i = i + 1

writer.close()
print("Errors: ")
