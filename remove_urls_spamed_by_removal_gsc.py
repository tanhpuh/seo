# Import libraries and packages for the project
from playsound import playsound
from selenium import webdriver
import pickle
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pyperclip as pc
import os
import requests
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime
import csv
import urllib.request as urllib2
import re
import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe
from google.oauth2.service_account import Credentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

driver = webdriver.Firefox()
driver.get('https://accounts.google.com/signin/v2/identifier?service=sitemaps&hl=vi&continue=https%3A%2F%2Fsearch.google.com%2Fsearch-console%3Futm_source%3Dabout-page&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
sleep(2)
# signin
credential = open('account')
line = credential.readlines()
account = line[0]
password = line[1]
sleep(2)
email_field = driver.find_element(By.XPATH,'//*[@id="identifierId"]')
input_email = email_field.send_keys(account)
sleep(2)
click_next = driver.find_element(By.XPATH,'//div[@id="identifierNext"]').click()
sleep(3)
password_field = driver.find_element(By.XPATH,'//input[@type="password"]')
input_password = password_field.send_keys(password)
sleep(2)
click_next = driver.find_element(By.XPATH,'//div[@id="passwordNext"]').click()
sleep(1)
playsound('/Users/lap02651/Documents/backup/code/Python/Sound/sound.mp3')
sleep(1)
#add code
verify = input('Done Verify: ')

credential = open('removal_urls')
line = credential.readlines()
content = line
for x in content:
    click_removals = driver.find_elements(By.XPATH,'//div[@class="cp8g2d"]')[8].click()
    sleep(2)
    #new request
    ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
    sleep(1)
    ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
    sleep(1)
    ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
    sleep(1)
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    #input url
    ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
    sleep(1)
    ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
    sleep(1)
    pc.copy(x)
    ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
    sleep(1)
    #next
    ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
    sleep(1)
    ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
    sleep(1)
    ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
    sleep(1)
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    #submit
    ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
    sleep(1)
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    #load time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log_time_report = now.strftime("%Y-%m-%d %H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")
    current_hour = now.strftime("%H")
    current_minute = now.strftime("%M")
    current_second = now.strftime("%S")
    #load data into a DataFrame object:
    data = {
    "date_time": [log_time_report],
    "url": [x.strip()]
    }
    # dataframe (create or import it)
    df = pd.DataFrame(data)

    #load scope spreadsheets
    scopes = ['https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive']

    credentials = Credentials.from_service_account_file('/Users/lap02651/Documents/backup/code/Python/Pandas Google Spreadsheets/service_account.json', scopes=scopes)

    gc = gspread.authorize(credentials)

    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)

    # share service account email to sheet: email service_account

    # open a google sheet
    gs = gc.open_by_key('1qdRJjVagX5ZI39Y7aXPhvyX6DvaM6QJB8NAk3pOVYg4')
    # select a work sheet from its name
    worksheet1 = gs.worksheet('url_removed')

    # write to dataframe
    # dataframe (create or import it)
    df_values = df.values.tolist()
    gs.values_append('url_removed', {'valueInputOption': 'RAW'}, {'values': df_values})
    # worksheet1.clear()
    # set_with_dataframe(worksheet=worksheet1, dataframe=df, include_index=False, include_column_header=True, resize=True)
    print(x)
    sleep(3)
    driver.get('https://search.google.com/search-console/removals?resource_id=https%3A%2F%2Ftiki.vn%2F')
    sleep(6)
playsound('/Users/lap02651/Documents/backup/code/Python/Sound/sound.mp3')
