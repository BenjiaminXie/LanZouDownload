import time
import sys
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from module.interaction import Interact


class Main():

    def __init__(self):
        self.browser = webdriver.Chrome()

    def main(self, burl):

        self.browser.maximize_window()
        self.browser.get(burl)

    # 检测密码是否存在
    def detection(self, pwds):
        if self.browser.find_element_by_xpath('//*[@id="pwdload"]'):
            pwd_input = self.browser.find_element_by_xpath('//*[@id="pwd"]')
            time.sleep(1)
            pwd_input.send_keys(pwds)
            # 尝试点击确认按钮
            try:
                self.browser.find_element_by_xpath('//*[@id="sub"]').click()
                url = self.browser.current_url
                resp = requests.get(url, timeout=2)
                code = resp.status_code
                # print('返回值1为：', code)
                assert code == 200
            except TimeoutException:
                time.sleep(1)
                print('提交密码出错')

            else:
                if self.browser.find_element_by_xpath('//*[@id="info"]/div[1]/div[2]/a/span'):
                    print('打开资源页面成功！！')
                else:
                    print('输入密码失败')
                time.sleep(1)
        myLength = len(WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//div[@id="ready"]'))))
        while self.browser.find_element_by_id('filemore').is_displayed():
            # filemores = self.browser.find_element_by_id('filemore')
            # ActionChains(self.browser).move_to_element(self.browser.find_elements_by_tag_name('span')).perform()
            # if filemores.find_element_by_id('filemore').is_displayed().is_displayed():
            try:
                self.browser.execute_script("scroll(0, 400)")
                # ActionChains(self.browser).move_to_element(filemores).perform()
                WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "显示更多文件"))).click()
                WebDriverWait(self.browser, 5).until(
                    lambda driver: len(driver.find_elements_by_xpath('//div[@id="ready"]')) > myLength)
                # time.sleep(4)
                # titles = self.browser.find_elements_by_xpath("//div[@class='flip-card-header']//h3")
                # myLength = len(titles)
            except TimeoutException:
                break

        readys = self.browser.find_elements_by_xpath('//div[@id="ready"]')
        for i, flag in enumerate(readys):
            ActionChains(self.browser).move_to_element(flag).perform()  # 鼠标移动到flag处
            it.url_click(flag)

            handles = self.browser.window_handles  # 获取当前全部窗口句柄集合（列表类型）
            self.browser.switch_to.window(handles[-1])  # 跳转到第num个窗口，从0开始
            iframe = self.browser.find_element_by_class_name('ifr')
            time.sleep(3)
            ActionChains(self.browser).move_to_element(iframe).perform()  # 鼠标移动到m元素上
            self.browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[4]/iframe').click()  # 点击弹出的层上的元素

            time.sleep(3)
            self.browser.close()

            handles = self.browser.window_handles
            self.browser.switch_to.window(handles[-1])
            time.sleep(2)
            submit = self.browser.find_element_by_class_name('submit')
            ActionChains(self.browser).move_to_element(submit).perform()
            try:
                self.browser.find_element_by_xpath('//*[@id="sub"]/div').click()

            finally:
                time.sleep(2)

            try:
                self.browser.find_element_by_xpath('//*[@id="go"]/a').click()
            finally:
                time.sleep(3)
                self.browser.close()

            self.browser.switch_to.window(handles[0])

    def browser_quit(self):
        from module import resource
        resource.download_wait(r'/home/zeus/Downloads/')
        self.browser.quit()


if __name__ == '__main__':
    it = Interact()
    urls = it.linkurl()
    pwds = it.pwd()
    g = Main()
    g.main(urls)
    g.detection(pwds)
    g.browser_quit()
    sys.exit(0)
