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
    urls = str('')
    imgurl = str('')
    breadcrumbs = list()
    pricenow = str('')
    priceold = str('')
    driver = WD.Chrome()

    def GetUrl(self,url): # метод для отримання урла
        self.url = url
        self.urls = url

    def GetLayout(self, url): # метод для необхідних даних із однієї сторінки
        self.url = url 
        self.driver.get(self.url) #підключаємо драйвер до урла
        layout = self.driver.find_element(by=By.CLASS_NAME, value="mainWR") #отримуємо всю стоірнку
        image_el = layout.find_element(by=By.CLASS_NAME,value="sourceImgJs") # шукаємо посилання на зображення
        image_url = image_el.get_attribute("src") # знаходимо атрибут посилання
        self.imgurl = image_url # зберігаємо урл 
        breadcrumbs_el = layout.find_element(by=By.CLASS_NAME,value="breadcr") # шукаємо хлібні крихти
        breadcrumb = breadcrumbs_el.find_elements(by=By.XPATH, value="//*[@itemprop='name' and not(@class='h1')]") # знаходимо кожну хлібну крихту
        for el in breadcrumb[1:]: # кожну хлібну крихту...
            self.breadcrumbs.append(el.text) # ...додаємо в список
        price_class = layout.find_element(by=By.XPATH, value ="//*[@class='costIco' and @itemprop='price']") # знаходимо теперішню ціну
        price = price_class.get_attribute('content') # позбавляємося пробіла та слова "грн"
        self.pricenow = price # зберігаємо в змінну
        old_price_class =  layout.find_element(by=By.XPATH, value ="//*[@class='old']").text # знаходимо стару ціну
        old_price = ('').join(old_price_class.split(" ")[:-1]) # забираємо стару ціну та позбавляємося пробліу
        #price = ('').join(price)
        self.priceold = old_price
    
    def GetPage(self,url):
        self.GetUrl(url=url)
        self.GetLayout(url=url)
        A = date.today()
        B = self.urls
        C = self.imgurl
        D = self.breadcrumbs
        E = self.pricenow
        F = self.priceold
        self.data.append(A)
        self.data.append(B)
        self.data.append(C)
        self.data.append(D)
        self.data.append(E)
        self.data.append(F)
        self.driver.quit()
        #print(self.data)
        
        

        
        
                 

url = 'https://bi.ua/ukr/product/nastolnaya-igra-hasbro-gaming-monopoliya-klassicheskaya-c1009eg4b.html'
page = page()
#page.GetLayout(url=url)
page.GetLayout(url=url)
#print(page.imgurl,page.urls)

        
