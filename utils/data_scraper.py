"""
Author - Sharat Gujamagadi
Date - 04.01.2021

Python script to download the Datasets (car) from wiki link
"""
import argparse
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import time
import os

def get_drive_images(driver):
    """
        method to scrolls the webpage
    """
    # while loop scrolls the webpage
    ticks = 0
    while ticks < 10:
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        try:
            driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[5]/input").click()
        except Exception as e:
            pass
        time.sleep(5)
        ticks += 1

    # parsing
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # closing web browser
    driver.close()

    # scraping image urls
    img_tags = soup.find_all("img", class_="rg_i")

    return img_tags

def download_all_images(img_tags, curr_dir, car_model):
    """
        Downloads the images from google search, and save them in the respective car-brand file
    """

    os.makedirs(curr_dir[:-6] + '/data' + '/' + str(car_model))
    image_path = os.path.join(curr_dir[:-6] + '/data' + '/' + str(car_model) + '/')

    img_count = 0
    for i in img_tags:
        try:
            print(i['src'])
            # passing image urls one by one and downloading
            urllib.request.urlretrieve(i['src'], image_path + str(img_count) + ".jpg")
            img_count += 1
            print("Number of images downloaded = " + str(img_count), end='\r')
        except Exception as e:
            print('Bad src found, ignoring the image')

def main():
    """
        main driver method, by default it will download audi cars
    """
    parser = argparse.ArgumentParser(description="Download images from Wiki Webpage")
    parser.add_argument('--car-brand', type=str, default='audi',
                        choices=['audi', 'benz', 'bmw'],
                        help='Default datasets (default: audi)')

    args = parser.parse_args()
    site = 'https://www.google.com/search?tbm=isch&q=' + args.car_brand
    current_dir = os.getcwd()
    # driver path
    driver = webdriver.Firefox(executable_path=current_dir + '/driver' +r'/geckodriver')

    driver.get(site)
    img_tags = get_drive_images(driver)
    download_all_images(img_tags, current_dir, args.car_brand )

if __name__ == '__main__':
    main()
