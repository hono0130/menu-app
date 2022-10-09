import random
import re 
import unicodedata
import asyncio

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import nest_asyncio
from schema import Menu

options = Options()
options.add_argument("--headless")
# options.add_argument('--proxy-server="direct://"')
options.add_argument('--window-size=800,600')
# options.add_argument('--no-sandbox')

    # driver.set_page_load_timeout(10)    # driver.command_executor.set_timeout(10)    

def search_seasonal_ingreds(num: int) -> dict[str, str]:
    try:
        driver = webdriver.Chrome('../../chromedriver/chromedriver', options=options)
        driver.get('https://cookien.com/')
        ingreds_elems = driver.find_elements(By.XPATH, '//*[@id="sp_search_kw_list"]/div/ul/li/a')[:num]
        link_lst = [element.get_attribute("href") for element in ingreds_elems ]
        name_lst = [element.get_attribute("textContent") for element in ingreds_elems ]
        dic = {}
        for i in range(len(name_lst)):
            dic[name_lst[i]] = link_lst[i]
        return dic
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
        main_duration = driver.find_element(By.XPATH, f'//*[@id="{main_id}"]/a//span[1]/span[2]').get_attribute("textContent")
        side_duration = driver.find_element(By.XPATH, f'//*[@id="{side_id}"]/a//span[1]/span[2]').get_attribute("textContent")
        menu_dic = {"main": {"name": main_name, "link": main_link, "img": main_img, "duration": main_duration}, "side": {"name": side_name, "link": side_link, "img": side_img, "duration": side_duration}}
        return menu_dic
    finally:
        driver.quit()


def get_menu_detail(link: str) -> dict[str, dict[str, any]]:
    try:
        driver = webdriver.Chrome('../../chromedriver/chromedriver', options=options)
        driver.get(link)

        ingreds_detail = driver.find_elements(By.XPATH, '//*[@id="r_contents"]/p')
        ingreds_lst = [ingreds.text for ingreds in ingreds_detail]

        ingreds_dict = {}
        for i in range(len(ingreds_lst)):
            ingreds_lst[i] = unicodedata.normalize("NFKC", ingreds_lst[i])
            # 改行かあるか判別
            # 改行がなければ、name = 全部の文字列 amount = None
            name = ingreds_lst[i].split("\n")[0]
            try:
                amount = ingreds_lst[i].split("\n")[1]
            except: 
                amount = ""
            if "(" in name:
                name = name.split("(")[0]
            if "(" in amount:
                amount = amount.split("(")[0] 

            number = re.search('[0-9]+\.*\/*[0-9]*', amount)

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

def _crawling_once(menu_lst: list, name: str, link: str):
    dic = select_menu(link)

    dic["main"]["is_side"] = False
    dic["main"]["tag"] = name
    dic["main"]["ingreds"] = get_menu_detail(dic["main"]["link"])
    menu_lst.append(dic["main"])
    dic["side"]["is_side"] = True
    dic["side"]["tag"] = name
    dic["side"]["ingreds"] = get_menu_detail(dic["side"]["link"])
    menu_lst.append(dic["side"])

async def crawling_once(menu_lst: list, name: str, link: str):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, _crawling_once, menu_lst, name, link)

async def crawling(num: int):
    nest_asyncio.apply()
    seasonal_ingreds_link_dict = search_seasonal_ingreds(num)
    
    loop = asyncio.get_event_loop()

    menu_lst = []
    # for name, link in seasonal_ingreds_link_dict.items():
    #     crawling(menu_lst, name, link)

    gather = asyncio.gather(*[crawling_once(menu_lst, name, link) for name, link in seasonal_ingreds_link_dict.items()])
    loop.run_until_complete(gather)

<<<<<<< HEAD
    return [Menu.marshal(menu["name"], menu["link"], menu["img"], menu["duration"], menu["is_side"], menu["tag"], menu["ingreds"]) for menu in menu_lst]

# loop = asyncio.get_event_loop()
# result = loop.run_until_complete((crawling(5)))
# loop.close()
# print(len(result))
=======
    return menu_lst

print(crawling(8))
>>>>>>> a8321aa (feat: 改行の有無で場合分け)
