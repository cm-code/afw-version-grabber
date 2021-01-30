#!/usr/bin/python3
##
##  get-asus-fwver.py
##  Gets version of supported ASUS Products via website.
##  Required Arguments [in order]:
##  asuscategory  Category of ASUS product, like 'Motherboards'
##  asusproduct   Name of ASUS product, like 'A88XMA'   
##

##
## Import Selenium and argparse
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.service import Service
import argparse

##
## Category and Product
#asuscategory="Motherboards"
#asusproduct="A88XMA"


##
## Argument parser
cmdparse = argparse.ArgumentParser()
cmdparse.add_argument("asuscategory", help="Category of Asus product, like 'Motherboards'")
cmdparse.add_argument("asusproduct", help="Name of Asus product, like 'A88XMA'")
cmdargs = cmdparse.parse_args()
asuscategory=cmdargs.asuscategory
asusproduct=cmdargs.asusproduct
biosurl = F"https://www.asus.com/us/{asuscategory}/{asusproduct}/HelpDesk_BIOS/"

##
## Options (Headless for now)
geckooptions = options()
geckooptions.add_argument('--headless')

##
## Initialize Browser and get url 
## * with Firefox service 
## * with geckooptions 
## * with biosurl
## Wait 5s for page to load
browser = webdriver.Firefox(service_log_path='/dev/null',options=geckooptions)
browser.implicitly_wait(5)
browser.get(biosurl)

##
## Load version information
try:
    ##
    ## Get version elements
    ## Print latest version
    biosvers = browser.find_elements_by_xpath("//span[@class='version']")
    print(biosvers[0].text[8:])
except:
    ##
    ## Version content Exception
    print('Cannot Load Version Content')
##
## Clean up 
browser.quit()
