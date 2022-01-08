import csv
import json
import os
import certifi
from numpy import resize
from urlopen import urllib
from urllib.request import urlopen, HTTPError
from datetime import datetime, timedelta
import requests
import pandas as pd
from bs4 import BeautifulSoup
import webdriver_setup
import time
import imageio as iio
import numpy as np
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
ssl.SSLContext.verify_mode = ssl.VerifyMode.CERT_OPTIONAL
q = "car"
s = [  # "https://empty3.one/galerie/",
    f"http://www.google.com/search?safe=on&source=hp&q={q}&oq={q}&tbm=isch&ijn=0"]
data = []
data1 = []


# for pg in s:
#     # query the website and return the html to the variable 'page'
#     print(pg)
#
#     page = urllib.request.urlopen(pg)
#     try:
#         search_response = urllib.request.urlopen(pg)
#     except urllib.request.HTTPError:
#         pass
#     # parse the html using beautiful soap and store in variable `soup`
#     soup = BeautifulSoup(page, 'html.parser')
#     # Take out the <div> of name and get its value
#     ls = [x.get_text(strip=True) for x in soup.find_all("h2", {"class": "f18"})]
#     ls1 = [x.get_text(strip=True) for x in soup.find_all("span", {"class": "date"})]
#     # save the data in tuple
#     data.append((ls))
#     data1.append(ls1)


def fetch_image_urls(query: str, max_links_to_fetch: int, sleep_between_interactions: int = 2):
    def scroll_to_end(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_between_interactions)

        # build the google query

    # load the page
    wd = webdriver_setup.get_webdriver
    wd = wd.ChromeDriver.create_driver("")
    wd.get(query)

    image_urls = set()
    image_count = 0
    results_start = 0
    while image_count < max_links_to_fetch:
        scroll_to_end(wd)

        # get all image thumbnail results
        thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
        number_results = len(thumbnail_results)

        if number_results > 0:
            print(f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}")
            for img in thumbnail_results[results_start:number_results]:
                # try to click every thumbnail such that we can get the real image behind it
                try:
                    img.click()
                    time.sleep(sleep_between_interactions)
                except Exception:
                    continue
                # extract image urls
                actual_images = wd.find_elements_by_css_selector('img.n3VNCb')
                for actual_image in actual_images:
                    if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src') \
                            and len(actual_images) < max_links_to_fetch:
                        image_urls.add(actual_image.get_attribute('src'))
                        # image_urls.add(actual_image.get_attribute(''))
                image_count = len(image_urls)

                if len(image_urls) >= max_links_to_fetch:
                    print(f"Found: {len(image_urls)} image links, done!")
                    return image_count, image_urls
                else:
                    print("Found:", len(image_urls), "image links, looking for more ...")
                    time.sleep(0.1)
                    # load_more_button = wd.find_element_by_css_selector(".mye4qd")
                    # if load_more_button:
                    #    wd.execute_script("document.querySelector('.mye4qd').click();")

                # move the result startpoint further down
            results_start = len(thumbnail_results)
        else:
            return image_count, image_urls

    return len(image_urls), image_urls


def yoururlimg(yourUrl):
    img = None
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    # req = urllib.request.Request(yourUrl, headers=headers, method="GET")
    try:
        context = ssl.create_default_context(cafile=certifi.where())
        # context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        img = urllib.request.urlopen(yourUrl, context=context).read()
        print(json.loads(img))
        return img
    finally:
        return img


for page in s:
    err = 0
    i = 0
    count, images = fetch_image_urls(page, 10, 2)
    if count > 0:
        writer = iio.get_writer("out-" + str(i) + ".mp4", "mp4", fps=25)
        for image in images:
            print(image)
            im = yoururlimg(image)
            if im is None:
                print("Can't get data for image: " + image)
                err = err + 1
                i = i + 1
                continue
            filename = "imagesDownloads/image_" + str(datetime.date(datetime.now())) + "_" + str(i) + ".jpg"
            f = open(filename, "wb")
            f.write(im)
            f.close()
            print(filename)

            im2 = iio.imread(filename)

            img3 = resize(im2, (30, 60, 3))
            writer.append_data(img3[:, :, 1])
            i = i + 1
            # im2.close()

        writer.close()
        print("Errors: " + str(err))
