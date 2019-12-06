import sys
import time
from selenium import webdriver

"""
- homeにenv.pyファイルを作り、m_id=""とm_pass=""を書いておく。
- 同ディレクトリにchromedriverを配置しておく。
"""

sys.path.append('/home/kijima/')
import env

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
time.sleep(2)
