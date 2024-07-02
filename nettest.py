import bs4
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0'}
URL = "https://warthunder.com/en/community/claninfo/PhoenixSquadron1"
driver = webdriver.Chrome()
driver.get(URL)
page = requests.get(URL, headers = headers)
soup = BeautifulSoup(page.content, "html.parser")
totalmax = soup.find("div", class_ ="squadrons-info__meta-item",).get_text()
spl = totalmax.split()
maxpl = int(spl[3])
scores = driver.find_elements(By.CLASS_NAME,"squadrons-counter__value")

psr = []
ign = []

for score in scores:
    x = 0
    y = 0
    for x in range(1, maxpl + 1):
        pos = (x * 6) + 2
        base_xpath = '/html/body/div[4]/div[2]/div[3]/div/section/div[3]/div/div[' + str(pos) + ']/a'
        name = score.find_elements(By.XPATH, base_xpath)
        nam = name[0].text
        ign.append(nam)
    for y in range(1, maxpl + 1):
        pos2 = (y * 6) + 3
        base_xpath = '/html/body/div[4]/div[2]/div[3]/div/section/div[3]/div/div[' + str(pos2) + ']'
        pts = score.find_elements(By.XPATH,base_xpath)
        ps = pts[0].text
        psr.append(ps)

df = pd.DataFrame({'IGN': ign, 'PSR': psr})
pd.options.display.max_rows = 1000
font_path = 'C:\Windows\Fonts\arial.ttf .'
prop = fm.FontProperties(fname=font_path)

# Create the table plot
table = plt.table(cellText=df.values, colLabels=df.columns, loc='center')

# Hide the axes and spines
ax = plt.gca()
ax.axis('off')

# Set the font properties for the table
for cell in table.get_celld().values():
    cell.set_font_properties(prop)

# Save the table plot as an image
plt.savefig('table.png', bbox_inches='tight', pad_inches=0)
plt.close()


