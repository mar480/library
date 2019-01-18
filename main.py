import sys
import logging
import datetime
from datetime import timedelta
import selenium
import bs4 as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException

chrome_options = Options()
chrome_options.add_argument("--kiosk-printing")

#############
###LOGGING###
#############
logging.basicConfig(level=logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.info('Date is ' + str(datetime.date.today()) + '. Datetime successfully imported.')
logging.info('Selenium version is ' + str(selenium.__version__) +'. Selenium successfully imported.')
logging.info('BS4 version is ' + bs.__version__ +'. BeautifulSoup successfully imported.')


##############
###SELENIUM###
##############

#instance of Chrome opens Librarika log in page
browser = webdriver.Chrome(options = chrome_options)
browser.implicitly_wait(10) # seconds
browser.get("https://cppdlibrary.librarika.com/users/dashboard")


#############
###CONNECT###
#############

def connect():
	#login credentials
	username = 'admin@cppd.co.uk'
	password = 'august1961'


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
###RESERVE###
#############

#checks for today's pending items and reserves them 

def reserve(url):

	#open pending in librarika and order by date
	#this way should avoid needing to write for more than one result page
	browser.get(url)
	
	#return a count for rows and columns
	rowElem = browser.find_elements_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr''')
	rowLen = len(rowElem)
	colElem = browser.find_elements_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[1]/th''')
	logging.info('There are ' + str(rowLen) + ' rows.')
	logging.info('There are ' + str(len(colElem)) + ' columns.')

	#iterate through each row and check the start date of the top entry (today because we clicked on date earlier)
	count = 0
	for i in range(2,rowLen+1):
		#reopen and order by date
		browser.get(url)
		dateHeadElem = browser.find_element_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[1]/th[2]/a''')
		dateHeadElem.click()
		#find loan date for each row on the table
		loanDate = browser.find_element_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[2]/td[2]''').text.rstrip()
		logging.info('Item '+ str(count) + ' loan date is ' + loanDate)
		#create datetime.date.today formated to match librarika
		today = (datetime.date.today().strftime('%b %d, %Y'))
		logging.info('Item '+ str(count) + ' datetime date is ' + today)
		#test compare selenium and datetime object
		if loanDate == today:
			logging.info('Item ' + str(count) +" loan date and datetime match")
			#click the Accept button
			acceptElem = browser.find_element_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[2]/td[12]/a[1]''')
			acceptElem.click()
			alertObj = browser.switch_to.alert
			alertObj.accept()
			count += 1
		#break loop
		else:
			logging.info(str(count) + ' items moved from pending to reserved.')
			logging.info('RESERVE LOOP CONCLUDED: loan date and datetime don\'t match')
			break

###########
###ISSUE###
###########

#checks for yesterday's reserved items and issues them

def issue(url):

	#open reserved in librarika and order by date
	#this way should avoid needing to write for more than one result page
	browser.get(url)
	
	#return a count for rows and columns
	rowElem = browser.find_elements_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr''')
	rowLen = len(rowElem)
	colElem = browser.find_elements_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[1]/th''')
	logging.info('There are ' + str(rowLen) + ' rows.')
	logging.info('There are ' + str(len(colElem)) + ' columns.')

	#iterate through each row and check the start date of the top entry (today because we clicked on date earlier)
	count = 0
	for i in range(2,rowLen+1):
		#reopen and order by date
		browser.get(url)
		dateHeadElem = browser.find_element_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[1]/th[2]/a''')
		dateHeadElem.click()
		#find reserved date for each row on the table
		reservedDate = browser.find_element_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[2]/td[2]''').text.rstrip()
		logging.info('Item '+ str(count) + ' reserved date is ' + reservedDate)
		#create datetime.date.yesterday formated to match librarika
		yesterday = (((datetime.date.today() - timedelta(1))).strftime('%b %d, %Y'))
		logging.info('Item '+ str(count) + ' datetime yesterday date is ' + yesterday)
		#test compare selenium and datetime object
		if reservedDate == yesterday:
			logging.info('Item ' + str(count) +" reserved date and datetime yesterday match")
			#click the Accept button
			acceptElem = browser.find_element_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[2]/td[12]/a[1]''')
			acceptElem.click()
			alertObj = browser.switch_to.alert
			alertObj.accept()
			count += 1
		#break loop
		else:
			logging.info(str(count) + ' items issued.')
			logging.info('ISSUE LOOP CONCLUDED: issue date and datetime don\'t match')
			break

###########
###PRINT###
###########

#checks for today's reserved items and prints the user receipt

def print(url):

	#open reserved in librarika and order by date
	#this way should avoid needing to write for more than one result page
	browser.get(url)
	
	#return a count for rows and columns
	rowElem = browser.find_elements_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr''')
	rowLen = len(rowElem)
	colElem = browser.find_elements_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[1]/th''')
	logging.info('There are ' + str(rowLen) + ' rows.')
	logging.info('There are ' + str(len(colElem)) + ' columns.')

	#iterate through each row and check the start date of the top entry (today because we clicked on date earlier)
	count = 0
	previoususername = 'blank'
	isDupe = False

	for i in range(2,rowLen+1):

		#reopen and order by date
		browser.get(url)
		dateHeadElem = browser.find_element_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[1]/th[2]/a''')
		dateHeadElem.click()

		#find reserved date for each row on the table
		reservedDate = browser.find_element_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[''' + str(i) +  ''']/td[2]''').text.rstrip()
		logging.info('Item '+ str(count) + ' reserved date is ' + reservedDate)

		#create datetime.date.today formated to match librarika
		today = (datetime.date.today().strftime('%b %d, %Y'))
		logging.info('Item '+ str(count) + ' datetime today\'s date is ' + today)

		#find current user's name
		membername = browser.find_element_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[''' + str(i) + ''']/td[5]''').text
		
		isDupe = membername == previoususername

		logging.info('username is ' + membername)
		logging.info('previous username is ' + previoususername)
	
		#test compare selenium and datetime object and member name

		if reservedDate == today and isDupe == False:
			j = 2

			previoususername = browser.find_element_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[''' + str(j) + ''']/td[5]''').text

			logging.info('Item ' + str(count) +" reserved date and datetime today match")

			#click the receipt button
			receiptElem = browser.find_element_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[2]/td[12]/a[2]''')
			receiptElem.click()

			#print receipt
			printElem = browser.find_element_by_xpath('''//*[@id="content"]/div/div[1]/div/div[4]/ul/li[3]/a''')
			browser.execute_script('window.print();')
			
			logging.info('dupe is ' + str(isDupe))
			j += 1
			count += 1
			isDupe = False

		#break loop
		else:
			isDupe = True
			logging.info('duplicate member name')
			continue

	logging.info(str(count) + ' receipt printed.')
	logging.info('PRINT LOOP CONCLUDED: issue date and datetime don\'t match')
			

###########
###MAIN####
###########

pendingURL = 'https://cppdlibrary.librarika.com/media_bookings/index/Pending'
reservedURL = 'https://cppdlibrary.librarika.com/media_bookings/index/Reserved'

# connect()
# reserve(pendingURL)
# issue(reservedURL)
# print(reservedURL)