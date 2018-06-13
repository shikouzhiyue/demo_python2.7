# -*-coding:utf-8-*-
'''
使用selenium模拟登陆淘宝网，并且实现翻页。部分内容可与demo_9_22内容作为参考
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
# WebDeriverWait 库负责循环等待的
from selenium.webdriver.support.ui import WebDriverWait
# expected_codition类 负责条件
from selenium.webdriver.support import expected_conditions as EC
# 超时异常
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

# #不显示接受自动测试的方式
# options = webdriver.ChromeOptions()
# options.add_argument('disable-infobars')
# driver = webdriver.Chrome(chrome_options=options)

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


def search(shop=None):
    print u'开始搜索了'
    driver.get('http://www.taobao.com')
    try:
        # 判断输入框是否加载完成
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#q'))
        )
        input.send_keys(u'{}'.format(shop))
        submit = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button'))
        )
        submit.click()
        get_response()
    except TimeoutException:
        return search(shop)


def get_response():
    # 判断当前的商品加载出来没有
    wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, '#mainsrp-itemlist .items .item'))
    )
    html = driver.page_source  # 获取当前页面的网页源代码
    soup = BeautifulSoup(html, 'lxml')  # 选择使用什么方式来进行网页解析
    items = soup.find('div', class_='m-itemlist').find_all('div', class_='item')
    for item in items:
        product = {
            'image': item.find('a').find('img')['src'],
            # 获取标签下的文本
            'price': item.find('div', class_='price g_price g_price-highlight').text,
            'num': item.find('div', class_='deal-cnt').text[:-3],
            'title': item.find('div', class_='row row-2 title').text,
            'location': item.find('div', class_='location').text
        }
        print product


def next_page(page):
    print u'当前是第{}页'.format(page)
    try:
        input = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '#mainsrp-pager > div > div > '
                                  'div > div.form > input'))
        )[0]
        submit = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > '
                                  'div.form > span.btn.J_Submit'))
        )
        input.clear()  # 清除输入框里的内容
        input.send_keys(page)
        submit.click()
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '#mainsrp-pager > div > div > '
                                  'div > ul > li.item.active > span'), str(page))
        )
        get_response()
    except TimeoutException:
        return next_page(page)


if __name__ == '__main__':
    shop = raw_input('请输入商品名字')
    search(shop)
    for i in range(2, 10):
        next_page(i)
