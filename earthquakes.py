from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import pandas as pd

# only uncomment the following if you need a new csv - this code is how we generated the csv, by

driver = webdriver.Chrome()

magnitudes = []
infos = []
depths = []
latitudes = []
longitudes = []

driver.get("https://earthquake.alaska.edu/earthquakes/shakemaps/list")

# this will make the program wait so that the page has time to load
driver.implicitly_wait(0.5)

table = driver.find_elements(By.TAG_NAME, 'a')

parentElement = driver.find_elements(By.TAG_NAME,"b")
elementList = []
links_all = []

for i in range(len(parentElement)):
    element = parentElement[i].find_element(By.TAG_NAME,"a")
    elementList.append(element)
    link = elementList[i].get_attribute("href")
    links_all.append(link)

links = []
for i in range(0, len(links_all)-2, 3):
    links.append(links_all[i])

print(links)


for i in links:
    driver.get(i)
    info = driver.find_element(By.TAG_NAME, "p").text
    info_list = info.split("\n")
    lat_long = info_list[1].split("    ")
    lat_longs = lat_long[0].split(" ")
    latitudes.append(lat_longs[0])
    longitudes.append(lat_longs[1])


for i in range(45, len(table)-3, 3):
    magnitude = table[i].text
    info = table[i+1].text
    depth = table[i+2].text
    magnitudes.append(magnitude)
    infos.append(info)
    depths.append(depth)

# print(magnitudes)
# print(infos)
# print(depths)
# print("Length of magnitudes :", len(magnitudes))
# print("Length of infos :", len(infos))
# print("Length of depths :", len(depths))

'''

driver.get("https://earthquake.alaska.edu/earthquakes/shakemaps/list/previous")

table = driver.find_elements(By.TAG_NAME, 'a')

for i in range(45, len(table)-3, 3):
    magnitude = table[i].text
    info = table[i+1].text
    depth = table[i+2].text
    magnitudes.append(magnitude)
    infos.append(info)
    depths.append(depth)

print(magnitudes[407])
print(infos[407])
print(depths[407])
print("Length of magnitudes :", len(magnitudes))
print("Length of infos :", len(infos))
print("Length of depths :", len(depths))

driver.get("https://earthquake.alaska.edu/earthquakes/shakemaps/list/older")

table = driver.find_elements(By.TAG_NAME, 'a')

for i in range(45, len(table)-3, 3):
    magnitude = table[i].text
    info = table[i+1].text
    depth = table[i+2].text
    magnitudes.append(magnitude)
    infos.append(info)
    depths.append(depth)

print(magnitudes[917])
print(infos[917])
print(depths[917])
print("Length of magnitudes :", len(magnitudes))
print("Length of infos :", len(infos))
print("Length of depths :", len(depths))


df = pd.read_csv("alaskan-earthquakes.csv")

df["magnitudes"] = magnitudes
df["infos"] = infos
df["depths"] = depths
df["latitudes"] = latitudes
df["longitudes"] = longitudes

df.to_csv('alaskan-earthquakes.csv')'''








