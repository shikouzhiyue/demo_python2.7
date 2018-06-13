# -*- coding:utf-8 -*-
from selenium import webdriver
import time

driver = webdriver.Chrome()
# 打开一个网站
driver.get('http://www.baidu.com')
'''
driver 操作页面的基本方法 定位网页元素
常见的定位 ID class css xpath
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_css_selector
'''
# 在百度的搜索框中输入python
driver.find_element_by_id('kw').send_keys('python')
time.sleep(2)
# 提交 即 百度一下
driver.find_element_by_id('su').click()
time.sleep(2)
driver.quit()



# 页面等待 很重要
# ajax js 这样程序就不能确定我们定位的元素是否已经加载

# time.sleep() 不推荐使用 因为也不能够确定页面的加载时间

# 显示等待 指满足某一个条件之后再执行后面的代码 可以设置最长的等待时间
from selenium import webdriver
from selenium.webdriver.common.by import By

# WebDriverWait 库负责循环等待的
from selenium.webdriver.support.ui import WebDriverWait

# exepected_conditions类 负责条件
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://www.xxxxx.com/loading')
try:
    '''
    页面会一直循环 直到 ID=mydymicElement 出现
    格式为
    WebDriverWait(driver, time).until(EC.条件（By.id,css, ……）， '')
    '''
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(By.ID, 'mydynmicElement')#接受的是一个元组
    )
finally:
    driver.quit()
'''
presece_of_all_elements_loated 判断页面的元素是否已经加载出来
element_to_be_clickable 判断当前的这个元素是否可以点击
'''



'''
css定位
# id 属性 class 标签来定位 可以组合在一起
#表示id属性 .class 标签直接使用
'''
driver.find_element_by_css_selector('#kw')
driver.find_element_by_css_selector('.s_ipt')
driver.find_element_by_css_selector('input')

driver.find_element_by_css_selector('[id="kw"]')
#组合形式的
driver.find_element_by_css_selector('input.s_ipt')
