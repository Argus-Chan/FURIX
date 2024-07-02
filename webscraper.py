import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

class Squadinfo():
    def __init__(self,squad,pts,max,ign,num,score):
        self.squad = squad
        self.pts = pts
        self.ign = ign
        self.num = num
        self.max = max
        self.score = score
    
    def scrapenum(self):
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0'}
        URL = "https://warthunder.com/en/community/claninfo/PhoenixSquadron1"
        driver = webdriver.Chrome()
        driver.get(URL)
        page = requests.get(URL, headers = headers)
        soup = BeautifulSoup(page.content, "html.parser")
        totalmax = soup.find("div", class_ ="squadrons-info__meta-item",).get_text()
        spl = totalmax.split()
        self.max = spl
        halfpl = (spl + 1)/2
        scores = driver.find_elements(By.CLASS_NAME,"squadrons-counter__value")
        self.num = halfpl
        self.score = scores
     
    def findign(num):
        pos = (num * 6) + 2
        return pos
    
    def findpts(num):
        pos = (num * 6) + 2
        return pos

    def webscrape(self):
        self.scrapenum()
        for score in self.score:
            x = 0
            y = 0
            for x in range(1,self.score)
                posx = 

    def show(self):
        return('Details: ',self.squad,self.pts,self.ign)
