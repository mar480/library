import os
import sys
import time
import tkinter as tk
import logging
import datetime
#import pdfkit
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


#############
###CONNECT###
#############

def connect():
	#instance of Chrome opens Librarika log in page
	browser = webdriver.Chrome(executable_path=r'\chrome\chromedriver\chromedriver.exe',options = chrome_options)
	browser.implicitly_wait(10) # seconds
	browser.get("https://cppdlibrary.librarika.com/users/dashboard")
	
	#login credentials
	username = ''
	password = ''


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

def reserve():
	#connect
	#instance of Chrome opens Librarika log in page
	browser = webdriver.Chrome(options = chrome_options)	
	browser.implicitly_wait(10) # seconds
	browser.get("https://cppdlibrary.librarika.com/users/dashboard")
	logging.info('Connecting to Librarika')
	#login credentials
	username = ''
	password = ''


	#enters login credentials and clicks OK
	userElem = browser.find_element_by_xpath('''//*[@id="UserUsername"]''')
	userElem.clear()
	userElem.send_keys(username)
	passElem = browser.find_element_by_xpath('''//*[@id="UserPassword"]''')
	passElem.clear()
	passElem.send_keys(password)
	submitElem = browser.find_element_by_xpath('''//*[@id="UserLoginForm"]/div[2]/div/input''')
	submitElem.click()
	logging.info('Successfully connected to Librarika')

	#open pending in librarika and order by date
	#this way should avoid needing to write for more than one result page
	
	logging.info('RESERVE PROCESS STARTED')
	browser.get('https://cppdlibrary.librarika.com/media_bookings/index/Pending')
	
	#return a count for rows and columns
	rowElem = browser.find_elements_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr''')
	colElem = browser.find_elements_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[1]/th''')
	rowLen = len(rowElem) -1
	colLen = len(colElem)
	logging.info('There are ' + str(rowLen) + ' rows.')
	logging.info('There are ' + str(len(colElem)) + ' columns.')

	#iterate through each row and check the start date of the top entry (today because we clicked on date earlier)
	count = 1
	for i in range(2,rowLen+1):
		#reopen and order by date
		browser.get('https://cppdlibrary.librarika.com/media_bookings/index/Pending')
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
	browser.quit()
###########
###ISSUE###
###########

#checks for yesterday's reserved items and issues them

def issue():
	#connect
	#instance of Chrome opens Librarika log in page
	browser = webdriver.Chrome(options = chrome_options)	
	browser.implicitly_wait(10) # seconds
	browser.get("https://cppdlibrary.librarika.com/users/dashboard")
	logging.info('Connecting to Librarika')
	#login credentials
	username = ''
	password = ''


	#enters login credentials and clicks OK
	userElem = browser.find_element_by_xpath('''//*[@id="UserUsername"]''')
	userElem.clear()
	userElem.send_keys(username)
	passElem = browser.find_element_by_xpath('''//*[@id="UserPassword"]''')
	passElem.clear()
	passElem.send_keys(password)
	submitElem = browser.find_element_by_xpath('''//*[@id="UserLoginForm"]/div[2]/div/input''')
	submitElem.click()
	logging.info('Successfully connected to Librarika')
	#open reserved in librarika and order by date
	#this way should avoid needing to write for more than one result page
	browser.get('https://cppdlibrary.librarika.com/media_bookings/index/Reserved')
	
	#return a count for rows and columns
	rowElem = browser.find_elements_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr''')
	rowLen = len(rowElem) -1
	colElem = browser.find_elements_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[1]/th''')
	logging.info('There are ' + str(rowLen-1) + ' rows.')
	logging.info('There are ' + str(len(colElem)) + ' columns.')

	#iterate through each row and check the start date of the top entry (today because we clicked on date earlier)
	count = 1
	for i in range(2,rowLen+1):
		#reopen and order by date
		browser.get('https://cppdlibrary.librarika.com/media_bookings/index/Reserved')
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
	browser.quit()
###########
###PRINT###
###########

#checks for today's reserved items and prints the user receipt

def printReceipts():
	#connect
	#instance of Chrome opens Librarika log in page
	browser = webdriver.Chrome(options = chrome_options)	
	browser.implicitly_wait(10) # seconds
	browser.get("https://cppdlibrary.librarika.com/users/dashboard")
	logging.info('Connecting to Librarika')
	#login credentials
	username = ''
	password = ''


	#enters login credentials and clicks OK
	userElem = browser.find_element_by_xpath('''//*[@id="UserUsername"]''')
	userElem.clear()
	userElem.send_keys(username)
	passElem = browser.find_element_by_xpath('''//*[@id="UserPassword"]''')
	passElem.clear()
	passElem.send_keys(password)
	submitElem = browser.find_element_by_xpath('''//*[@id="UserLoginForm"]/div[2]/div/input''')
	submitElem.click()
	logging.info('Successfully connected to Librarika')
	
	#open circulations/reserved in librarika and order by date
	browser.get("https://cppdlibrary.librarika.com/media_bookings/index/Reserved")
	
	#return a count for rows and columns
	rowElem = browser.find_elements_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr''')
	colElem = browser.find_elements_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[1]/th''')

	logging.info('There are ' + str(len(rowElem) - 1) + ' rows.')
	logging.info('There are ' + str(len(colElem)) + ' columns.')

	#open page and order table by member
	memberElem = browser.find_element_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[1]/th[5]/a''')
	memberElem.click()

	#create variables
	rownumber = 2 #rownumber
	itemnumber = 0 #itemnumber
	receiptnumber = 0 #receiptnumber
	previoususername = 'blank' #sets first user name to blanks #the first iteration now doesn't cause an error when it looks above row 1 and can't find a row 0 
	isDupe = False #checks if the user receipt has already been printed by only printing one receipt per user
	rowLen = len(rowElem) + 1 #range upper limit = total rows + 1 because of range function upper limit
	memberNameList = [] #list of members who have had receipts printed
		

	#for every row in range (starting row number for xpath, total number of rows)
	for i in range(2,rowLen):

		#increase item number
		itemnumber +=1
		#find and format reserved date for each row on the table
		reservedDate = browser.find_element_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[''' + str(i) +  ''']/td[2]''').text.rstrip()
		logging.info('Item '+ str(itemnumber) + "'s reserved date is " + reservedDate)

		#create datetime.date.today formated to match librarika
		today = (datetime.date.today().strftime('%b %d, %Y'))
		logging.info('Item '+ str(itemnumber) + "'s datetime today date is " + today)

		#find this row's username
		membername = browser.find_element_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[''' + str(i) + ''']/td[5]''').text.rstrip()

		#check if current username matches the previously looped name # first loop the previous user is set to 'blank' as above
		isDupe = membername == previoususername

		logging.info('Current username is ' + membername)
		logging.info('Previous username is ' + previoususername)
		logging.info('Dupe is set to ' + str(isDupe))
		
		#test compare selenium and datetime object and member name
		#if today and not an additional booking for a previously printed member receipt
		if reservedDate == today and isDupe == False and membername not in memberNameList:
				
			logging.info('Item ' + str(itemnumber) +" reserved date and datetime today match")
			logging.info('No receipt printed so far for ' + (membername))

			#click on receipt button
			receiptElem = browser.find_element_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr['''+ str(i) +''']/td[12]/a[2]''')
			receiptElem.click()

			#print receipt and pause because otherwise it doesn't technically work for some reason?!
			browser.execute_script('window.print();')	
			time.sleep(1) # seconds

			#add member name to member list
			memberNameList.append(membername)
			logging.info(membername + ' added to memberNameList')
			logging.info('RESULT: ' + membername + ' receipt(s) printed')			
			
			receiptnumber += 1
			
		else:
			
			if reservedDate != today:
				logging.info('RESULT: This booking is not for today')
			elif membername in memberNameList:
				logging.info('RESULT: Already in memberNameList')
			elif membername == previoususername:
				logging.info('RESULT: Receipt already printed')
			else:
				logging.info('RESULT: Unspecified error')
				
			continue


		#reset the loop
		browser.back()
		logging.info(memberNameList)


		# set previous username for next iteration
		logging.info('Previous username was ' + previoususername)
		previoususername = browser.find_element_by_xpath('''//*[@id="content"]/div/div[1]/div/table/tbody/tr[''' + str(i) + ''']/td[5]''').text.rstrip()
		logging.info('Previous username is now ' + previoususername)

	logging.info('FINAL RESULT: '+str(receiptnumber) + ' receipt(s) printed.')
	logging.info('PRINT LOOP CONCLUDED')
	browser.quit()	

###########
###MAIN####
###########

#############
###TKINTER###
#############

root=tk.Tk()

button_1 = tk.Button(root, text = 'Accept today\'s reservations', command = reserve)
button_2 = tk.Button(root, text = 'Print today\'s receipts', command = printReceipts)
button_3 = tk.Button(root, text = 'Issue yesterday\'s books', command = issue)

img = tk.PhotoImage(file = 'img\\img.png')
imglabel = tk.Label(root, image = img)
imglabel.grid(column = 1, ipadx = 5, ipady= 5, rowspan = 3)

button_1.grid(row = 0, padx = (10, 5), pady = (7, 5), ipadx = 5, ipady= 9, sticky = 'nsew')
button_2.grid(row = 1, padx = (10, 5), pady = (5, 5), ipadx = 5, ipady= 9, sticky = 'nsew')
button_3.grid(row = 2, padx = (10, 5), pady = (5, 7), ipadx = 5, ipady= 9, sticky = 'nsew')

root.mainloop()
#connect()
#reserve()
#issue()
#print()

