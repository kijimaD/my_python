import sys
import time
import datetime
import os
import psycopg2
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib import request

"""
- homeにenv.pyファイルを作り、m_id=""とm_pass=""を書いておく。パスワードがあるため。
- 同ディレクトリにchromedriverを配置しておく。
"""

sys.path.append('/home/kijima/')
import env


class Scrape():
    def __init__(self):
        self.soup = 0

    def site_access():
        driver = webdriver.Chrome("chromedriver")
        driver.get("https://trade.03trade.com/web/")

        name = driver.find_element_by_xpath('//*[@id="CmnCauSysLgiInitInput_block"]/table[1]/tbody/tr[1]/td/table/tbody/tr/td/input')
        name.send_keys(env.m_id)

        word = driver.find_element_by_xpath('//*[@id="passwd1"]')
        word.send_keys(env.m_pass)
        driver.find_element_by_xpath('//*[@id="CmnCauSysLgiInitBtn_block"]/div/input').click()  # 送信ボタン
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="CmnCauSysLgiBtn_block"]/div/input').click()  # 確認ボタン
        time.sleep(1)

        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="maintile"]/form/table/tbody/tr/td[2]/a/img').click()  # テレコンをクリック
        time.sleep(2)

        # ウィンドウハンドルを取得する
        handle_array = driver.window_handles
        # seleniumで操作可能なdriverを切り替える
        driver.switch_to.window(handle_array[1])

        driver.find_element_by_link_text('きょうの新聞').click()
        time.sleep(1)
        driver.execute_script("javascript:(function (){var inputs = document.getElementsByTagName('input');for(var i=0; ; i++){for (var j=0; j < inputs.length; j ++) {var e = inputs[j];if (e.type == 'checkbox')e.checked = true;}if(i < window.frames.length){try {inputs = window.frames[i].document.getElementsByTagName('input');}catch(e){}}else{break;}}})();")

        driver.find_element_by_xpath('/html/body/main/div/div[2]/form[2]/div[3]/p/label/input').click()
        driver.find_element_by_xpath('/html/body/main/div/div[2]/form[2]/div[3]/p/label/input').click()
        driver.find_element_by_xpath('/html/body/main/div/div[2]/form[2]/div[2]/p/span/input').click()
        time.sleep(1)

        # ページまるごと取得してreturn

    def scrape(input, connection):
        cursor = connection.cursor()
        soup = BeautifulSoup(input, 'html.parser')
        titles = []
        titles = soup.find_all('h2')
        contents = []
        contents = soup.find_all('div', class_="Honbun")
        for p in range(len(titles)):
            title = titles[p].text
            content = contents[p].text
            pubtime = datetime.date.today()
            print('title:', title)
            print('content:', content)
            print('pubtime:', pubtime)
            sql = """insert into django_test_news (title, content, pubdate) values
            (%(title)s, %(content)s, %(pubdate)s);
            """
            cursor.execute(sql, {'title': title, 'content': content, 'pubdate': pubtime})
            connection.commit()

    def test_input():
        test_data = open("/home/kijima/Desktop/test.html", "r")
        return test_data
        test_data.close()

    def response_input():
        pass

    def db_connect():
        connection = psycopg2.connect(
            user='kijima',
            password='digital',
            host='localhost',
            port='5432',
            database='django_test')
        return connection


connection = Scrape.db_connect()
raw_input = Scrape.test_input()
Scrape.scrape(raw_input, connection)
