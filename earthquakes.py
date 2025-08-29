from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import pandas as pd
import time

# only uncomment the following if you need a new csv - this code is how we generated the csv, by

driver = webdriver.Chrome()

# these are the lists that will make up our csv
magnitudes = []
infos = []
depths = []
latitudes = []
longitudes = []

# here is the function that will extract and do some processing on the data we want
def get_data(url):
    driver.get(url)

    # this will make the program wait so that the page has time to load
    driver.implicitly_wait(0.5)

    table = driver.find_elements(By.TAG_NAME, 'a')

    parent_element = driver.find_elements(By.TAG_NAME,"b")
    element_list = []
    links_all = []

    for i in range(len(parent_element)):
        element = parent_element[i].find_element(By.TAG_NAME,"a")
        element_list.append(element)
        link = element_list[i].get_attribute("href")
        links_all.append(link)

    links = []
    for i in range(0, len(links_all)-2, 3):
        links.append(links_all[i])

    print(links)

    for i in links:
        time.sleep(3)
        driver.get(i)
        info = driver.find_element(By.TAG_NAME, "p").text
        info_list = info.split("\n")
        lat_long = info_list[1].split("    ")
        lat_longs = lat_long[0].split(" ")
        latitudes.append(lat_longs[0])
        longitudes.append(lat_longs[1])

    driver.get(url)

    # this will make the program wait so that the page has time to load
    driver.implicitly_wait(0.5)

    table = driver.find_elements(By.TAG_NAME, 'a')

    for i in range(45, len(table)-3, 3):
        magnitude = table[i].text
        info = table[i+1].text
        depth = table[i+2].text
        magnitudes.append(magnitude)
        infos.append(info)
        depths.append(depth)


# all 3 pages of data that we want to extract
page_urls = ["https://earthquake.alaska.edu/earthquakes/shakemaps/list",
             "https://earthquake.alaska.edu/earthquakes/shakemaps/list/previous",
             "https://earthquake.alaska.edu/earthquakes/shakemaps/list/older"]

# this is where we will call the actual pages to extract their data
for i in page_urls:
    get_data(i)


df = pd.read_csv("alaskan-earthquakes.csv")

df["magnitudes"] = magnitudes
df["infos"] = infos
df["depths"] = depths
df["latitudes"] = latitudes
df["longitudes"] = longitudes

df.to_csv('alaskan-earthquakes.csv')








