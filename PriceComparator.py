import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests as re
from bs4 import BeautifulSoup 
import csv
import time
#importing the library selenium in order to import chromedriver to access
#websites

product = "oppo a31"
#here the user will write the product name he/she is searching for

PATH = "C:\webdrivers\chromedriver.exe"
#this represents the path for chromedriver that each device has its own
driver = webdriver.Chrome(PATH)




driver.get("http://www.amazon.in/")
#here we access the amazon website
search = driver.find_element_by_xpath("//*[@id='twotabsearchtextbox']")
#copying the xpath of the search button from the html content 
search.click()
#clicking on the search button with the help of xpath of search button
search.send_keys(product)
#here the code sends the name of the product mentioned by the user to the website
searchIcon = driver.find_element_by_xpath("//*[@id='nav-search-submit-button']")
searchIcon.click()
#here the search icon of the website gets clicked with the help of the xpath 
#copied from the website
currUrl = driver.current_url
content=re.get(currUrl).content 
soup = BeautifulSoup(content,'html.parser')
#using the library beautiful soup in order to extract the html content of the 
#product on the website 
searchProduct = soup.find_all('div', {"data-component-type" : "s-search-result"})
#here we get the information about the products that appear on the screen after 
#clicking on the search icon
flag = 0
if searchProduct == [] :
	#it implies that the product mentioned by the user does not match with 
	#any product on the website
	print("Product not available on Amazon")
else :
	for elements in searchProduct :
		currProduct = elements.find("a",class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
		currProductName = currProduct.get_text()
		#here we get the name of the product we are searching from ,, 
		#from the search results with the help of html content 
		currProductNameSplit = currProductName.split()
		#storing each word of the name of the product in a list(currProductNameSplit)
		productSplit = product.split()
		#storing each word of the product written by the user in list(productSplit)
		for i in range(len(currProductNameSplit)) :
			currProductNameSplit[i] = currProductNameSplit[i].lower()
			#converting the elements of the currProductNameSplit in the lower case letters 
			#if in case the user has typed in the lower case letters

		j = 0
		for i in productSplit :
			if i.lower() not in currProductNameSplit :
				#here we are checking whether the elements in the two lists defined
				#above match or not 
				j = 1
				#it implies the product does not match with the search results 
				#and hence not available on the website(amazon)
				break

		if j == 0 :
			priceSpan = elements.find("span",class_="a-offscreen")
			#here we access the price of the product through the html content
			#on the website by making use of beautiful soup
			price = priceSpan.get_text()
			print("Price on Amazon is " + price)
			#here we print the price of the product
			flag = 1
			break
		else :
			break
if flag == 0 :
	print("Product not available on Amazon")
	#it implies that the product metioned by the user does not completely match 
	#with search results and hence it prints "Product not available on amazon"

driver.get("https://www.flipkart.com/fossil-virginia-analog-watch-women/p/itmf3zhcncfkf9dh?pid=WATDGSZZGEFWGVYG&lid=LSTWATDGSZZGEFWGVYGB9RMWZ&marketplace=FLIPKART&q=watch&store=r18%2Ff13&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=en_pOBF7iSsLXxBs4PIudHqOASi2u0GxZwJr81DDoR5sRlRCCY5mTZHkNbzzilXa4cGF1fEmyoywdn8HFKdfugagw%3D%3D&ppt=sp&ppn=sp&ssid=d76d6y9aj40000001653833892537&qH=d2974c96dc96b3f3")
#here we access the amazon website
search=driver.find_element_by_xpath("//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
#copying the xpath of the search button from the html content
search.click()
#clicking on the search button with the help of xpath of search button

search.send_keys(product)
#here the code sends the name of the product mentioned by the user to the website
searchIcon = driver.find_element_by_xpath("//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
searchIcon.click()
#here the search icon of the website gets clicked with the help of the xpath 
#copied from the website
currUrl = driver.current_url
content=re.get(currUrl).content 
soup = BeautifulSoup(content,'html.parser')
#using the library beautiful soup in order to extract the html content of the 
#product on the website 
searchProduct = soup.find_all('div', {"class" : "_1AtVbE col-12-12"})
#here we get the information about the products that appear on the screen after 
#clicking on the search icon
flag = 0
if searchProduct == [] :
	#it implies that the product mentioned by the user does not match with 
	#any product on the website
	print("Product not available on flipkart")
else :
	for elements in searchProduct :
		currProduct = elements.find('div', {"class" : "_4rR01T"})
		if str(currProduct) != "None" : 
			currProductName = currProduct.get_text()
			#here we get the name of the product we are searching from ,, 
		#from the search results with the help of html content 
			currProductNameSplit = currProductName.split()
			#storing each word of the name of the product in a list(currProductNameSplit)
			productSplit = product.split()
			#storing each word of the product written by the user in list(productSplit)
			for i in range(len(currProductNameSplit)) :
				currProductNameSplit[i] = currProductNameSplit[i].lower()
				#converting the elements of the currProductNameSplit in the lower case letters 
			#if in case the user has typed in the lower case letters


			j = 0
			for i in productSplit :
				if i.lower() not in currProductNameSplit :
					#here we are checking whether the elements in the two lists defined
				#above match or not 
					j = 1
					#it implies the product does not match with the search results 
				#and hence not available on the website(flipkart)
					break
			if j == 0 :
				priceSpan = elements.find("div", {"class" : "_30jeq3 _1_WHN1"})
				#here we access the price of the product through the html content
			#on the website by making use of beautiful soup
				price = priceSpan.get_text()
				print("Price on Flipkart is " + price)
				#here we print the price of the product
				flag = 1
				break
			else :
				continue
if flag == 0 :
	print("Product not available on flipkart")
	#it implies that the product metioned by the user does not completely match 
	#with search results and hence it prints "Product not available on flipkart"