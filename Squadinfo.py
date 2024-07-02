import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from tabulate import tabulate
import numpy as np

class Squadinfo():
    def __init__(self,squad):
        self.squad = squad

class Scrape(Squadinfo):
    def __init__(self,squad):
        Squadinfo.__init__(self,squad)
        self.maxi = 0
        self.elements = 0

    @classmethod
    def search(self):
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0'}
        URL = "https://warthunder.com/en/community/claninfo/PhoenixSquadron1"
        driver = webdriver.Chrome()
        driver.get(URL)
        page = requests.get(URL, headers = headers)
        soup = BeautifulSoup(page.content, "html.parser")
        totalmax = soup.find("div", class_ ="squadrons-info__meta-item",).get_text()
        spl = totalmax.split()  
        self.maxi = int(spl[3])
        self.elements = driver.find_elements(By.CLASS_NAME,"squadrons-counter__value")
        ign = []
        pts = []
        data = []
        for element in self.elements:
            x = 0
            for x in range(1, ((self.maxi) + 1)):
                pos_ign = self.websearch(x, 'ign')
                pos_pts = self.websearch(x, 'scr')
                ign_xpath = '/html/body/div[4]/div[2]/div[3]/div/section/div[3]/div/div[' + str(pos_ign) + ']/a'
                pts_xpath = '/html/body/div[4]/div[2]/div[3]/div/section/div[3]/div/div[' + str(pos_pts) + ']'
                name = element.find_elements(By.XPATH, ign_xpath)
                score = element.find_elements(By.XPATH, pts_xpath)
                nam = name[0].text
                psr = score[0].text
                ign.append(nam)
                pts.append(psr)
        data = pd.DataFrame(data={'IGN': ign, 'PSR': pts})
        data = data.drop_duplicates(subset='IGN', keep='first')
        table = tabulate(data)
        return table
    
    def websearch(num, mode):
        pos = 0
        if mode == 'scr':
            pos = (num * 6) + 3
        elif mode == 'ign':
            pos = (num * 6) + 2
        elif mode != 'ign' and mode != 'scr':
            pos = 0
        return pos