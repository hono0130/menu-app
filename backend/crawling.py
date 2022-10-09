from lib2to3.pgen2 import driver
from time import sleep
import random
import re 
import unicodedata

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


options = Options()
# options.add_argument("--headless")
# options.add_argument('--proxy-server="direct://"')
options.add_argument('--window-size=800,600')
# options.add_argument('--no-sandbox')

    # driver.set_page_load_timeout(10)    # driver.command_executor.set_timeout(10)    

def search_seasonal_ingreds(num: int) -> list[str]:
    try:
        driver = webdriver.Chrome('../../chromedriver/chromedriver', options=options)
        driver.get('https://cookien.com/')
        ingreds_elems = driver.find_elements(By.XPATH, '//*[@id="sp_search_kw_list"]/div/ul/li/a')[:num]
        link_lst = [element.get_attribute("href") for element in ingreds_elems ]
        return link_lst 
    finally:
        driver.quit()

def select_menu(link: str) -> dict[str, dict[str, str]]:
    try:
        driver = webdriver.Chrome('../../chromedriver/chromedriver', options=options)
        driver.get(link)
        
        menu_lst = driver.find_elements(By.XPATH, '//*[@id="content"]/div/article')
        print(menu_lst)
        class_lst = [element.get_attribute("class") for element in menu_lst ]
        lst_tmp = [menu for menu in class_lst if ("tag-sugumeshi" not in menu) and ("rag-cookingtime-40" not in menu) and ("rag-cookingtime-50" not in menu)]
        lst_main = [menu for menu in lst_tmp if "tag-main" in menu]
        lst_side = [menu for menu in lst_tmp if "tag-side" in menu]
        main_id = random.choice(lst_main).split(" ")[0]
        side_id = random.choice(lst_side).split(" ")[0]
        main_link = driver.find_element(By.XPATH, f'//*[@id="{main_id}"]/a').get_attribute("href")
        side_link = driver.find_element(By.XPATH, f'//*[@id="{side_id}"]/a').get_attribute("href")
        main_img = driver.find_element(By.XPATH, f'//*[@id="{main_id}"]//img').get_attribute("src")
        side_img = driver.find_element(By.XPATH, f'//*[@id="{side_id}"]//img').get_attribute("src")
        main_name = driver.find_element(By.XPATH, f'//*[@id="{main_id}"]/a/div[1]/h2').text
        side_name = driver.find_element(By.XPATH, f'//*[@id="{side_id}"]/a/div[1]/h2').text
        menu_dic = {"main": {"name": main_name, "link": main_link, "img": main_img}, "side": {"name": side_name, "link": side_link, "img": side_img}}
        return menu_dic
    finally:
        driver.quit()


def get_menu_detail(link: str) -> dict[str, str]:
    try:
        driver = webdriver.Chrome('../../chromedriver/chromedriver', options=options)
        driver.get(link)

        ingreds_detail = driver.find_elements(By.XPATH, '//*[@id="r_contents"]/p')
        ingreds_lst = [ingreds.text for ingreds in ingreds_detail]

        ingreds_dict = {}
        for i in range(len(ingreds_lst)):
            ingreds_lst[i] = unicodedata.normalize("NFKC", ingreds_lst[i])
            name = ingreds_lst[i].split("\n")[0]
            amount = ingreds_lst[i].split("\n")[1]
            if "(" in name:
                name = name.split("(")[0]
            if "(" in amount:
                amount = amount.split("(")[0] 

            number = re.search('[0-9]+\.*[0-9]*', amount)

            if not number:
                number = None
                unit = amount
            else:
                number = number.group()
                unit = amount.replace(number, "")

            amount_dic = {}
            amount_dic[unit] = number

            ingreds_dict[name] = amount_dic

        return ingreds_dict
    finally:
        driver.quit()

def crawling(num: int):
    seasonal_ingreds_link_lst = search_seasonal_ingreds(num)

    print("done")
    
    menu_lst = []
    for link in seasonal_ingreds_link_lst:
        print(link)
        menu_lst.append(select_menu(link))
        print("done")
    
    print("done")

    for dic in menu_lst:
        print(dic)
        dic["main"]["ingreds"] = get_menu_detail(dic["main"]["link"])
        dic["side"]["ingreds"] = get_menu_detail(dic["side"]["link"])
    
    return menu_lst

print(crawling(4))


