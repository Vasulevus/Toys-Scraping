import selenium
import selenium.webdriver as WD
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as UI


#Список потрібного для скрапінґу:
#дата, url, url зображення, хлібні крихти, ціна теперішня та стара, опис


from selenium import webdriver as WD
from selenium.webdriver.common.by import By

class Page:
    date = list()
    urls = list()
    imgurl = list()
    breadcrumbs = list()
    pricenow = list()
    priceold = list()

    def GetLayout(self, url):
        self.url = url
        driver = WD.Chrome()
        driver.get(self.url)
        layout = driver.find_element(by=By.CLASS_NAME, value="mainWR")
        html = layout.get_attribute("outerHTML")
        print(html)
        driver.quit()

url = 'https://bi.ua/ukr/product/konstruktor-lego-creator-expert-buket-10280.html'
page = Page()
page.GetLayout(url=url)

        
