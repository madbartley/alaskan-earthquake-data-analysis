from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import pandas as pd

# only uncomment the following if you need a new csv - this code is how we generated the csv, by
'''
driver = webdriver.Chrome()

driver.get("https://earthquake.alaska.edu/earthquakes/shakemaps/list")

# this will make the program wait so that the page has time to load
driver.implicitly_wait(0.5)

table = driver.find_elements(By.TAG_NAME, 'a')

magnitudes = []
infos = []
depths = []


for i in range(45, len(table)-3, 3):
    magnitude = table[i].text
    info = table[i+1].text
    depth = table[i+2].text
    magnitudes.append(magnitude)
    infos.append(info)
    depths.append(depth)

'''print(magnitudes)
print(infos)
print(depths)
print("Length of magnitudes :", len(magnitudes))
print("Length of infos :", len(infos))
print("Length of depths :", len(depths))'''

driver.get("https://earthquake.alaska.edu/earthquakes/shakemaps/list/previous")

table = driver.find_elements(By.TAG_NAME, 'a')

for i in range(45, len(table)-3, 3):
    magnitude = table[i].text
    info = table[i+1].text
    depth = table[i+2].text
    magnitudes.append(magnitude)
    infos.append(info)
    depths.append(depth)

'''print(magnitudes[407])
print(infos[407])
print(depths[407])
print("Length of magnitudes :", len(magnitudes))
print("Length of infos :", len(infos))
print("Length of depths :", len(depths))'''

driver.get("https://earthquake.alaska.edu/earthquakes/shakemaps/list/older")

table = driver.find_elements(By.TAG_NAME, 'a')

for i in range(45, len(table)-3, 3):
    magnitude = table[i].text
    info = table[i+1].text
    depth = table[i+2].text
    magnitudes.append(magnitude)
    infos.append(info)
    depths.append(depth)

'''print(magnitudes[917])
print(infos[917])
print(depths[917])
print("Length of magnitudes :", len(magnitudes))
print("Length of infos :", len(infos))
print("Length of depths :", len(depths))'''


df = pd.read_csv("alaskan-earthquakes.csv")

df["magnitudes"] = magnitudes
df["infos"] = infos
df["depths"] = depths

df.to_csv('alaskan-earthquakes.csv')'''





