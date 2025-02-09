from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# WebDriverのセットアップ
driver = webdriver.Chrome()
driver.get('https://jp.tradingview.com/markets/stocks-japan/market-movers-52wk-high/')

# ページのロードを待機
time.sleep(5)

# ページの末尾までスクロールして「もっと読み込む」ボタンをクリック
while True:
    try:
        load_more_button = driver.find_element(By.XPATH, '//button[text()="もっと読み込む"]')
        actions = ActionChains(driver)
        actions.move_to_element(load_more_button).perform()
        load_more_button.click()
        time.sleep(2)  # データの読み込みを待機
    except:
        break

# ここで全てのデータが読み込まれた状態になります
# 必要に応じてデータを取得・保存する処理を追加

driver.quit()
