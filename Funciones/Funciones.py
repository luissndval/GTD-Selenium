import os
import time
import warnings

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class funciones_2_0:
    def __init__(self, driver):
        self.driver = driver

    ############################################################################################
    ################################## Navegador ###############################################
    ############################################################################################
    def driver_Firefox(self):
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = os.path.join("C:\drivers\geckodriver")
        s = Service(os.path.join("C:\drivers\geckodriver"))
        self.driver = webdriver.Firefox(service=s)
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

    def driver_Chrome(self):
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = webdriver.Chrome("\\..\\drivers\\chromedriver.exe")

    ############################################################################################
    ################################## element_to_be_clickable##################################
    ############################################################################################

    def browser(self, link):
        self.driver.get(link)
        self.driver.maximize_window()
        print("Página abierta: " + str(link))

    def input_Texto(self, tipo, selector, texto):
        WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located((tipo, selector))).send_keys(texto)
        time.sleep(1)
        print("\n Escribir en el campo {} el texto -> {} ".format(selector, texto))

    def click_Field(self, tipo, selector):
        WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located((tipo, selector))).click()
        time.sleep(2)
        print("\n Click sobre el elemento -> {} ".format(selector))

    def clear_Field(self, tipo, selector):
        WebDriverWait(self.driver, timeout=5).until(EC.element_to_be_clickable((tipo, selector))).clear()
        print("\n Texto eliminado -> {} ".format(selector))

    def validates(self, tipo, selector):
        element = WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located((tipo, selector))).text
        print(element)
        print("\n Elemento Validado -> {} ".format(selector))

    def subirArchivo(self, tipo, selector, ruta):
        val = self.driver.find_element(tipo, selector)
        val.send_keys(ruta)
        print("\n Elemento Cargado -> {} ".format(selector))

    def scrollToElement(self, tipo, elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((tipo, elemento)))
        self.driver.execute_script("arguments[0].scrollIntoView();", val)
        print("\n Desplazando al elemento -> {} ".format(elemento))

    ###################################################################################

    ########################## Allure-Report ##########################################
    ###################################################################################

    def screenShot(self, nombre):
        allure.attach(self.driver.get_screenshot_as_png(), name=nombre, attachment_type=AttachmentType.PNG)

        ###################################################################################
        ########################## ACTION CHAINS ##########################################
        ###################################################################################

    def input_Texto_ActionChains(self, tipo, selector, texto):
        action = ActionChains(self.driver)
        val = self.driver.find_element(tipo, selector, texto)
        action.click(val).perform()
        action.send_keys(texto).perform()
        time.sleep(1)

    def clickAction(self, tipo, selector):
        action = ActionChains(self.driver)

        val = self.driver.find_element(tipo, selector)
        action.click(val).perform()
        time.sleep(1)

    def key_Up_Key_Down(self, tecla):
        action = ActionChains(self.driver)

        action.key_down(tecla).perform()
        action.key_up(tecla).perform()
        time.sleep(1)

    ############################################################################################
    ############################ visibility_of_element_located #################################
    ############################################################################################

    def input_Texto_visibility(self, tipo, selector, texto):
        WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located((tipo, selector))).send_keys(
            texto)
        time.sleep(1)
        print("\n Escribir en el campo {} el texto -> {} ".format(selector, texto))

    def click_Field_visibility(self, tipo, selector):
        WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located((tipo, selector))).click()
        time.sleep(2)
        print("\n Click sobre el elemento -> {} ".format(selector))

    def clear_Field_visibility(self, tipo, selector):
        WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located((tipo, selector))).clear()
        print("\n Texto eliminado -> {} ".format(selector))

    def validates_visibility(self, tipo, selector):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((tipo, selector))).text
        print(element)
        print("\n Elemento Validado -> {} ".format(selector))

    def subirArchivo_visibility(self, tipo, selector, ruta):
        val = self.driver.find_element(tipo, selector)
        val.send_keys(ruta)
        print("\n Elemento Cargado -> {} ".format(selector))

    def scrollToElement_visibility(self, tipo, elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((tipo, elemento)))
        self.driver.execute_script("arguments[0].scrollIntoView();", val)
        print("\n Desplazando al elemento -> {} ".format(elemento))

    def Iframe(self, tipo, selector):
        element = self.driver.find_element(tipo, selector)
        self.driver.switch_to.frame(element)
