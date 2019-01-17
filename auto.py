import sys
import logging
import datetime
import selenium
import bs4 as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

logging.basicConfig(level=logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.info('Date is ' + str(datetime.date.today()) + '. Datetime successfully imported.')
logging.info('Selenium version is ' + str(selenium.__version__) +'. Selenium successfully imported.')
logging.info('BS4 version is ' + bs.__version__ +'. BeautifulSoup successfully imported.')




#def connect():
username = 'admin@cppd.co.uk'
password = 'august1961'
browser = webdriver.Chrome()
browser.implicitly_wait(10) # seconds
browser.get("https://cppdlibrary.librarika.com/users/dashboard")
#browser.implicitly_wait(10) # seconds
userElem = browser.find_element_by_xpath('''//*[@id="UserUsername"]''')
userElem.clear()
userElem.send_keys(username)
#browser.implicitly_wait(10) # seconds
passElem = browser.find_element_by_xpath('''//*[@id="UserPassword"]''')
passElem.clear()
passElem.send_keys(password)
submitElem = browser.find_element_by_xpath('''//*[@id="UserLoginForm"]/div[2]/div/input''')
submitElem.click()
#connect()

#circulationsURL = ('https://cppdlibrary.librarika.com/media_bookings')
#reservedURL = ('https://cppdlibrary.librarika.com/media_bookings/index/Reserved')

#def pendingToReserved():
pendingURL = 'https://cppdlibrary.librarika.com/media_bookings/index/Pending'
pendingHTML = browser.page_source


browser.get(pendingURL)
# dateHeadElem = browser.find_element_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[1]/th[2]/a''')
# dateHeadElem.click()


#pass page source to BS4

# pendingHTML = browser.page_source
# soup = bs.BeautifulSoup(pendingHTML, features = 'lxml')

# table = soup.table
# table_rows = table.find_all('tr')

# for tr in table_rows:
# 	td = tr.find_all('td')
# 	row = [i.text for i in td]
# 	cleanrow = [t.get_text(strip=True) for t in tr(['td', 'th'])]
# 	print(cleanrow)



# list_items = soup.find_all('div', {'class': "data-item-value"})
# print(list_items)
# browser.close()
# sys.exit()

# table_rows = table.find_all('tr')

# for rows in table_rows:
# 	td = tr.find_all('td')
# 	row = [i.text for i in td]
# 	print(row)
#for url in soup.find_all('a'):
	#print(url.get_text() + ' - ' + url.get('href'))

##############################################################################################################

# rowElem = browser.find_elements_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr''')
# rowCount = len(rowElem)
# colElem = browser.find_elements_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[1]/th''')
# columnCount = len(colElem)

# print(rowCount,columnCount)

# root1 = '''//*[@id="content"]/div/div[1]/div/table/tbody/tr['''
# root2 = ''']/td['''
# root3 = ']'

# for i in range(1, rowCount + 1):
# 	for j in range(1, columnCount + 1):
# 		xpath = root1 + str(i) + root2 + str(j) + root3
# 		tableData = browser.find_elements_by_xpath(xpath).format(text)
# 		print(tableData)

# //*[@id="content"]/div/div[1]/div/table/tbody/tr[1]
# //*[@id="content"]/div/div[1]/div/table/tbody/tr[2]/td[1]
# //*[@id="content"]/div/div[1]/div/table/tbody/tr[2]/td[2]
# //*[@id="content"]/div/div[1]/div/table/tbody/tr[2]
# //*[@id="content"]/div/div[1]/div/table/tbody/tr[3]
# //*[@id="content"]/div/div[1]/div/table/tbody/tr[4]
