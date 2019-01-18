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

###
#print

# def print(url):

# 	#open reserved in librarika and order by date
# 	#this way should avoid needing to write for more than one result page
# 	browser.get(url)
	
# 	#return a count for rows and columns
# 	rowElem = browser.find_elements_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr''')
# 	rowLen = len(rowElem)
# 	colElem = browser.find_elements_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[1]/th''')
# 	logging.info('There are ' + str(rowLen) + ' rows.')
# 	logging.info('There are ' + str(len(colElem)) + ' columns.')

# 	#iterate through each row and check the start date of the top entry (today because we clicked on date earlier)
# 	j = 2
# 	count = 0
# 	previoususername = 'blank'
# 	isDupe = False

# 	for i in range(j,rowLen+1):

# 		#reopen and order by member
# 		logging.info('j = ' + str(j))
# 		browser.get(url)
# 		memberElem = browser.find_element_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[1]/th[5]/a''')
# 		memberElem.click()

# 		#find reserved date for each row on the table
# 		reservedDate = browser.find_element_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[''' + str(j) +  ''']/td[2]''').text.rstrip()
# 		logging.info('Item '+ str(count) + ' reserved date is ' + reservedDate)

# 		#create datetime.date.today formated to match librarika
# 		today = (datetime.date.today().strftime('%b %d, %Y'))
# 		logging.info('Item '+ str(count) + ' datetime today\'s date is ' + today)

# 		#find current user's name
# 		membername = browser.find_element_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[''' + str(j) + ''']/td[5]''').text
		
# 		#check if current name matches previous name
# 		isDupe = membername == previoususername

# 		logging.info('username is ' + membername)
# 		logging.info('previous username is ' + previoususername)
# 		logging.info('Dupe is ' + str(isDupe))

# 		#set previous username
# 		previoususername = browser.find_element_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[''' + str(j) + ''']/td[5]''').text
		
# 		#test compare selenium and datetime object and member name
# 		#if today and not an additional booking for a previously printed member receipt
# 		if reservedDate == today and isDupe == False:
				
# 			logging.info('Item ' + str(count) +" reserved date and datetime today match")

# 			#click the receipt button
# 			receiptElem = browser.find_element_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr['''+ str(j) +''']/td[12]/a[2]''')
# 			receiptElem.click()

# 			#print receipt
# 			browser.execute_script('window.print();')
# 			logging.info('receipt printed')			
# 			j += 1
# 			count += 1
			
# 		else:
# 			j+=1
# 			if reservedDate != today:
# 				logging.info('dates do not match')
# 			elif membername == previoususername:
# 				isDupe = True
# 				logging.info('duplicate member name')
# 			else:
# 				logging.info('unspecified error')
# 			continue

# 	logging.info(str(count) + ' receipt printed.')
# 	logging.info('PRINT LOOP CONCLUDED')
			