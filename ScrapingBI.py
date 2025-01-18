import selenium
import selenium.webdriver as WD
import selenium.webdriver
import selenium.webdriver.common
from selenium.webdriver.common.by import By
import selenium.webdriver.common.by
import selenium.webdriver.support.ui as UI


# що потрібно отримати:
# вибрати якийсь розділ, перейти на розділи та обрати підрозділи
# забрати всі урли на сторінці підрозділа,
# пройтися по всім сторінкам і забрати дані звідти,
# натиснути кнопку перейти на наступну сторінку, якщо така є
# перенести в dataframe
# зберегти в sqlite та ms-sql
# вивести це все в dash


class url_list:
    urls = list()
    driver = WD.Chrome()

    def Get_Urls(self, url):
        self.url = url
        self.driver.get(self.url)
        list_of_urls = self.driver.find_elements(by=By.XPATH, value="//a[@class='goodsItemLink']")
        for url in list_of_urls:
            href = url.get_attribute('href')
            self.urls.append(href)
        print(self.urls)
        self.driver.quit()



list_urls = url_list()
list_urls.Get_Urls('https://bi.ua/ukr/nastolnye-igry-i-pazly/nastolnye-igry/')