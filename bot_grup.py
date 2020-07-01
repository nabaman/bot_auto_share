from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import json
import os


PATH = os.getcwd() + '/chromedriver'
driver = webdriver.Chrome(PATH)
driver.get('https://web.facebook.com/')

#buka data dari file data.json
with open('data.json') as f:
    data = json.load(f)

e = driver.find_element_by_id('email')
e.send_keys(data['username'])
e = driver.find_element_by_id('pass')
e.send_keys(data['password'])
e = driver.find_element_by_id('loginbutton')
e.click()
sleep(5)
driver.get('https://web.facebook.com/groups/') #untuk mencari list grup dalam akun

x = driver.find_element_by_xpath("//*[contains(text(), 'Lihat Selengkapnya')]") #untuk mencari semua grup yang ada
i = 0
while x:
    try:
        x = driver.find_element_by_xpath("//*[contains(text(), 'Lihat Selengkapnya')]")
        x.click()
        sleep(3)
        z = driver.find_element_by_xpath("//*[contains(text(),'Grup tempat Anda Menjadi Anggota')]")
        z.click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.perform()
        sleep(3)

    except NoSuchElementException:
        x = False
else:
    e = driver.find_elements_by_class_name('_2yav')
    data = []
    for i in e:
        data.append(i.text)

    data.pop(0)

#untuk masuk ke profile
for isi in set(data):
    driver.get('https://web.facebook.com/pipit.smfgaming.5')
    sleep(5)
    e = driver.find_element_by_css_selector('span._1j6m') #untuk mencari tombol share pada postingan paling atas
    e.click()
    sleep(5)
    e = driver.find_element_by_xpath("//span[contains(text(), 'Bagikan di Grup')]") #untuk menekan tombol bagikan di grup
    e.click()
    sleep(5)
    e = driver.find_element_by_xpath("//label[@class='_55r1 _55r2 _58ak _3ct8']") #untuk mengisi grup tujuan
    e.click
    sleep(3)

    for i in isi:
        e.send_keys(i)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_DOWN)
    sleep(2)
    actions.send_keys(Keys.RETURN)
    sleep(2)
    actions.perform()
    e = driver.find_element_by_xpath("//div[@aria-label='Katakan sesuatu tentang ini...']") #untuk mengisi pesan share
    e.click()
    sleep(2)
    e.send_keys('RICARDO MILOS BOYAH SOLO LAWAN SQUADD!!! DI JAMIN KOCAKK ... \nAYO SEMUANYA DI TONTON !! !! !! JANGAN LUPA SUBSCRIBE AND SHARE YA CHANNELNYA \npipit smf GAMING \nhttps://www.youtube.com/channel/UC_P9mZuz2d8vVO0TnMZ3Pew bakal ada give away di 3000 subscriber !!!')
    sleep(2)
    e = driver.find_element_by_xpath("//button[@class='_2g61 _4jy0 _4jy3 _4jy1 _51sy selected _42ft']")
    e.click()
    sleep(5)











    #untuk posting status
# e = driver.find_element_by_tag_name('textarea')
# e.click()
# e.send_keys('hahahahahaha')
# sleep(7)
# e = driver.find_element_by_xpath('//button[@class="_1mf7 _4r1q _4jy0 _4jy3 _4jy1 _51sy selected _42ft"]')
# e.click()
# print("Posted...")
#





