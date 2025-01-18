import selenium
import selenium.webdriver as WD
import selenium.webdriver
import selenium.webdriver.common
from selenium.webdriver.common.by import By
import selenium.webdriver.common.by
import selenium.webdriver.support.ui as UI
from datetime import date


# що потрібно отримати:
# вибрати якийсь розділ, перейти на розділи та обрати підрозділи
# забрати всі урли на сторінці підрозділа,
# пройтися по всім сторінкам і забрати дані звідти,
# натиснути кнопку перейти на наступну сторінку, якщо така є
# перенести в dataframe
# зберегти в sqlite та ms-sql
# вивести це все в dash


class scraping:
    urls_list = list()
    data = list()
    date = list()
    urls = str('')
    imgurl = str('')
    breadcrumbs = list()
    pricenow = str('')
    priceold = str('')
    driver = WD.Chrome()

    driver = WD.Chrome()

    def Get_Urls(self, url):
        self.url = url
        self.driver.get(self.url)
        list_of_urls = self.driver.find_elements(by=By.XPATH, value="//a[@class='goodsItemLink']")
        for url in list_of_urls:
            href = url.get_attribute('href')
            self.urls.append(href)
        print(self.urls)
        # зупинка тут. Треба додати перехід на наступну сторінку
        # для оптимізації потрібно, щоб використовувася той самий драйвер

        #self.GetPage()

        self.driver.quit()



    def GetSingleUrl(self,url): # метод для отримання урла
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
        self.GetSingleUrl(url=url)
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
        print(self.data)


#запарсити найбільше число із сторінки. зробити єдиний запуск драйвера. Подивитися багатопоточність в уроках.

Scraping = scraping()
Scraping.Get_Urls('https://bi.ua/ukr/nastolnye-igry-i-pazly/nastolnye-igry/')