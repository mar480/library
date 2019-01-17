import sys
import logging
import datetime
import selenium
import bs4 as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#############
###LOGGING###
#############
logging.basicConfig(level=logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.info('Date is ' + str(datetime.date.today()) + '. Datetime successfully imported.')
logging.info('Selenium version is ' + str(selenium.__version__) +'. Selenium successfully imported.')
logging.info('BS4 version is ' + bs.__version__ +'. BeautifulSoup successfully imported.')

#############
###CONNECT###
#############

#login credentials
username = 'admin@cppd.co.uk'
password = 'august1961'

#instance of Chrome opens Librarika log in page
browser = webdriver.Chrome()
browser.implicitly_wait(10) # seconds
browser.get("https://cppdlibrary.librarika.com/users/dashboard")

#enters login credentials and clicks OK
userElem = browser.find_element_by_xpath('''//*[@id="UserUsername"]''')
userElem.clear()
userElem.send_keys(username)
passElem = browser.find_element_by_xpath('''//*[@id="UserPassword"]''')
passElem.clear()
passElem.send_keys(password)
submitElem = browser.find_element_by_xpath('''//*[@id="UserLoginForm"]/div[2]/div/input''')
submitElem.click()

#############
###PENDING###
#############

#open pending in librarika and order by date
#this way should avoid needing to write for more than one result page
pendingURL = 'https://cppdlibrary.librarika.com/media_bookings/index/Pending'
browser.get(pendingURL)
dateHeadElem = browser.find_element_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[1]/th[2]/a''')
dateHeadElem.click()


rowElem = browser.find_elements_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr''')
rowLen = len(rowElem)
colElem = browser.find_elements_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[1]/th''')
rowCount = 'There are ' + str(rowLen) + ' rows.'
columnCount = 'There are ' + str(len(colElem)) + ' columns.'

print(rowCount, columnCount)


for i in range(2,rowLen+1):
	loanDate = browser.find_element_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[''' + str(i) + ''']/td[2]''').text
	print(loanDate)
