from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('https://classic.set.or.th/mkt/sectorquotation.do?sector=SET50&language=th&country=TH')

count = 0
company_list = []
print("----- Company in SET50 of Thai stock market -----")

for data in driver.find_elements(By.XPATH,'//table[@class="table-info"]//tbody//tr//td[@style="text-align: left;"]//a')[8:] :
    count += 1   
    company_list.append(data.get_attribute('href'))
    print("{0}. {1}".format(count,data.text))