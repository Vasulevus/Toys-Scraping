import selenium
import selenium.webdriver as WD
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as UI
from datetime import date



#Список потрібного для скрапінґу:
#дата, url, url зображення, хлібні крихти, ціна теперішня та стара, опис


from selenium import webdriver as WD
from selenium.webdriver.common.by import By

class page:
    data = list()
    date = list()
    urls = list()
    imgurl = list()
    breadcrumbs = list()
    pricenow = list()
    priceold = list()
    driver = WD.Chrome()

    def GetUrl(self,url):
        self.url = url
        self.urls.append(url)

    def GetLayout(self, url):
        self.url = url
        self.driver.get(self.url)
        layout = self.driver.find_element(by=By.CLASS_NAME, value="mainWR")
        #html = layout.get_attribute("outerHTML")
        #print(html)
        #driver.quit()
        return layout
    
    def GetImage(self,url):
        layout = self.GetLayout(url=url)
        image_el = layout.find_element(by=By.CLASS_NAME,value="sourceImgJs")
        image_url = image_el.get_attribute("src")
        self.imgurl.append(image_url)
        #print(image_url)
    
    def GetBreadCrumbs(self,url):
        layout = self.GetLayout(url=url)
        breadcrumbs_el = layout.find_element(by=By.CLASS_NAME,value="breadcr")
        breadcrumb = breadcrumbs_el.find_elements(by=By.XPATH, value="//*[@itemprop='name' and not(@class='h1')]")
        b_list = list()
        for el in breadcrumb[1:]:
            self.breadcrumbs.append(el.text)
        #print(self.breadcrumbs)
        self.driver.quit()
    
    def GetPage(self,url):
            self.GetUrl(url=url)
            self.GetImage(url=url)
            self.GetBreadCrumbs(url=url)
            A = date.today()
            B = self.urls
            C = self.imgurl
            D = self.breadcrumbs
            self.data.append(A)
            self.data.append(B)
            self.data.append(C)
            self.data.append(D)
            print(self.data)
        
        

        
        
                 

url = 'https://bi.ua/ukr/product/nastolnaya-igra-spin-master-dzhumandzhi-sm336106072999.html'
page = page()
#page.GetLayout(url=url)
page.GetPage(url=url)
#print(page.imgurl,page.urls)

        
