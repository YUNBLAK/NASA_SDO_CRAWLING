import csv
import cv2
import pandas as pd
import numpy as np
from datetime import date, timedelta
import matplotlib.pyplot as plt
from urllib import request
import urllib.request
import requests
from bs4 import BeautifulSoup

def urlMaker(n):
    url = 'https://sdo.gsfc.nasa.gov/assets/img/browse/'
    today = date.today()
    yesterday = date.today() - timedelta(n)
    url = url + str(yesterday.strftime('%Y/%m/%d')) + "/"
    return [url, str(yesterday.strftime('%Y%m%d'))]

def printby(arr):
    for i in range(0, len(arr)):
        print(arr[i])

def fileprint(url):
    indexlst = []
    files = []
    number = 0
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
    else : 
        print(response.status_code)

    links = soup.find_all('a') 
    cell_line = []
    for i in links:
        href = i.attrs['href']
        cell_line.append(href)
    
    for i in range(5, len(cell_line)):
        if '512_211193171.jpg' in cell_line[i]:
            # print(cell_line[i][0:11])
            if cell_line[i][0:11] not in indexlst:
                indexlst.append(cell_line[i][0:11])
                files.append(cell_line[i])
            number += 1
    return files

def download(n, name):
    url = n
    filename = 'NEWDATA/' + name
    urllib.request.urlretrieve(url, filename)

def main():
    for i in range(0, 3000):
        x = fileprint(urlMaker(i)[0])
        for j in range(0, len(x)):
            print(urlMaker(i)[0] + x[j])
            try:
                download(urlMaker(i)[0] + x[j], x[j])
                print('DONE --- ', x[j])
            except:
                print("ERROR")
            
if __name__ == "__main__":
    main()