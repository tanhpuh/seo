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

credential = open('Kw list')
line = credential.readlines()
lines = line [0:]
for query in lines:
    sleep(35)
    driver.get('https://www.google.com.vn/')
    sleep(2)
    driver.find_element(By.XPATH,'//textarea[@id="APjFqb"]').click()
    sleep(1)
    kw = query + 'tiki.vn'
    pc.copy(kw)
    ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
    sleep(1)
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    page_source = BeautifulSoup(driver.page_source, "html.parser")
    url_domanin_s_div = page_source.find_all('div',{'class':'yuRUbf'})
    all_domain = []
    for n in url_domanin_s_div:
        n = n.find_all('a')[0].get('href')
        if ('https://tiki.vn/search' in n and '〖' in n) or  ('https://tiki.vn/search' in n and '【' in n) or ('https://tiki.vn/search' in n and '】' in n) or ('https://tiki.vn/search' in n and '』' in n) or ('https://tiki.vn/search' in n and '《' in n) or ('https://tiki.vn/search' in n and '%E3%80%8F' in n) or ('https://tiki.vn/search' in n and '%E3%80%8A' in n) or ('https://tiki.vn/search' in n and '%E3%80%91' in n) or ('https://tiki.vn/search' in n and '%E3%80%90' in n) or ('https://tiki.vn/search' in n and '@' in n) or ('https://tiki.vn/search' in n and 'B6H3319' in n) or ('https://tiki.vn/search' in n and 'में' in n) or ('https://tiki.vn/search' in n and 'PDF9' in n) or ('https://tiki.vn/search' in n and 'lienge89867' in n) or ('https://tiki.vn/search' in n and 'jl9188' in n) or ('https://tiki.vn/search' in n and '.nl' in n) or ('https://tiki.vn/search' in n and 'Web:' in n) or ('https://tiki.vn/search' in n and '.pl' in n) or ('https://tiki.vn/search' in n and '☞' in n) or ('https://tiki.vn/search' in n and 'E2%98%9E' in n) or ('https://tiki.vn/search' in n and 'sudo6' in n) or ('https://tiki.vn/search' in n and 'Sudo6' in n)  or ('https://tiki.vn/search' in n and 'Sodo6' in n) or ('https://tiki.vn/search' in n and 'sodo6' in n):
            all_domain.append(n)
            url_list = all_domain
    num_url = len(all_domain)
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
    "num_url": [num_url],
    "query": [query.strip()],
    "url_list": [str(url_list)]
    }
    # dataframe (create or import it)
    df = pd.DataFrame(data)

    #load scope spreadsheets
    scopes = ['https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive']

    credentials = Credentials.from_service_account_file('/Users/lap02651/Documents/backup/code/Python/Pandas Google Spreadsheets/service_account.json', scopes=scopes)

    gc = gspread.authorize(credentials)

    # share service account email to sheet: email service_account

    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)

    # open a google sheet
    gs = gc.open_by_key('google_sheet_key')
    # select a work sheet from its name
    worksheet1 = gs.worksheet('google_sheet_name')
    # dataframe (create or import it)
    df_values = df.values.tolist()
    gs.values_append('url_crawled', {'valueInputOption': 'RAW'}, {'values': df_values})
    # worksheet1.clear()
    # set_with_dataframe(worksheet=worksheet1, dataframe=df, include_index=False, include_column_header=True, resize=True)
    sleep(3)

playsound('/Users/lap02651/Documents/backup/code/Python/Sound/sound.mp3')
