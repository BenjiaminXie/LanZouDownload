
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Interact():

    def linkurl(self):
        up = input('请输入蓝奏资源地址：') #'https://wwe.lanzous.com/b01c1v44j'
        return up

    def pwd(self):
        pwds = input('该资源已加密，请输入密码：')
        return pwds

    def downloadurl(self):
        dl = input('v请选择需要下载的文件v')
        return dl

    def url_click(self,flag):
        self.flag = flag
        try:
            WebDriverWait(self.flag, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'a'))).click()
        except TimeoutException:
            time.sleep(1)
            print('提交密码出错')
            #self.flag.close()
