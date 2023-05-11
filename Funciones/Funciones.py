import csv
import os
import time
import warnings

import allure
from allure_commons.types import AttachmentType
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


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

    def driver_chrome_headless(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        options.add_argument("--headless")
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        display = Display(visible=0, size=(800, 600))
        display.start()

    def driver_mobile(self):
        mobile_emulation = {"deviceName": "iPhone X"}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    ############################################################################################
    ################################## element_to_be_clickable##################################
    ############################################################################################

    def browser(self, link):
        self.driver.get(link)
        self.driver.maximize_window()
        print("Página abierta: " + str(link))

    def input_Texto(self, tipo, selector, texto):
        WebDriverWait(self.driver, timeout=20).until(EC.visibility_of_element_located((tipo, selector))).send_keys(
            texto)
        time.sleep(1)
        print("\n Escribir en el campo {} el texto -> {} ".format(selector, texto))

    def click_Field(self, tipo, selector):
        WebDriverWait(self.driver, timeout=20).until(EC.visibility_of_element_located((tipo, selector))).click()
        time.sleep(2)
        print("\n Click sobre el elemento -> {} ".format(selector))

    def clear_Field(self, tipo, selector):
        WebDriverWait(self.driver, timeout=20).until(EC.element_to_be_clickable((tipo, selector))).clear()
        print("\n Texto eliminado -> {} ".format(selector))

    def validates(self, tipo, selector):
        element = WebDriverWait(self.driver, timeout=20).until(EC.presence_of_element_located((tipo, selector))).text
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
        try:
            val = self.driver.find_element(tipo, selector, texto)
            action.click(val).perform()
            action.send_keys(texto).perform()
            time.sleep(1)
        except Exception as ex:
            print(ex)
            print(f"No se Completa el campo {selector}")

    def clickAction(self, tipo, selector):
        action = ActionChains(self.driver)
        try:
            val = self.driver.find_element(tipo, selector)
            action.click(val).perform()
            time.sleep(1)
        except Exception as ex:
            print(ex)
            print(f"No se Completa el campo {selector}")

    def key_Up_Key_Down(self, tecla):
        action = ActionChains(self.driver)
        try:
            action.key_down(tecla).perform()
            action.key_up(tecla).perform()
            time.sleep(1)
        except Exception as ex:
            print(ex)

    ############################################################################################
    ############################ visibility_of_element_located #################################
    ############################################################################################

    def input_Texto_visibility(self, tipo, selector, texto):
        WebDriverWait(self.driver, timeout=20).until(EC.visibility_of_element_located((tipo, selector))).send_keys(
            texto)
        time.sleep(1)
        print("\n Escribir en el campo {} el texto -> {} ".format(selector, texto))

    def click_Field_visibility(self, tipo, selector):
        WebDriverWait(self.driver, timeout=20).until(EC.visibility_of_element_located((tipo, selector))).click()
        time.sleep(2)
        print("\n Click sobre el elemento -> {} ".format(selector))

    def clear_Field_visibility(self, tipo, selector):
        WebDriverWait(self.driver, timeout=20).until(EC.visibility_of_element_located((tipo, selector))).clear()
        print("\n Texto eliminado -> {} ".format(selector))

    def validates_visibility(self, tipo, selector):
        element = WebDriverWait(self.driver, timeout=20).until(
            EC.visibility_of_element_located((tipo, selector))).text
        print(element)
        print("\n Elemento Validado -> {} ".format(selector))

    def subirArchivo_visibility(self, tipo, selector, ruta):
        val = self.driver.find_element(tipo, selector)
        val.send_keys(ruta)
        print("\n Elemento Cargado -> {} ".format(selector))

    def scrollToElement_visibility(self, tipo, elemento):
        val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((tipo, elemento)))
        self.driver.execute_script("arguments[0].scrollIntoView();", val)
        print("\n Desplazando al elemento -> {} ".format(elemento))

    def Iframe(self, tipo, selector):
        element = self.driver.find_element(tipo, selector)
        self.driver.switch_to.frame(element)

    # def CrearDocumento(self, nombre_doc, nombre_columna, tipo, selector):
    #     ruta_csv = "..\\txt\\{}.csv".format(nombre_doc)  # definir la ruta predefinida
    #     elemento = WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located((tipo, selector))).text
    #     valor_replace = elemento.replace('"', '').replace('\n', ' ')
    #     print(valor_replace)
    #     try:
    #         if not os.path.exists(ruta_csv):
    #             with open(ruta_csv, 'w', newline='') as csvfile:
    #                 fieldnames = [nombre_columna]
    #                 writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #                 writer.writeheader()
    #                 writer.writerow({nombre_columna: valor_replace})
    #         else:
    #             with open(ruta_csv, 'a', newline='') as csvfile:
    #                 fieldnames = [nombre_columna]
    #                 writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #                 writer.writerow({nombre_columna: valor_replace})
    #     except Exception as e:
    #         print(f"Error al crear o escribir en el documento: {e}")
    #
    #     # Captura el texto del elemento con el xpath especificado
    #     try:
    #         elemento = WebDriverWait(self.driver, timeout=5).until(
    #             EC.visibility_of_element_located((tipo, selector))).text
    #     except Exception as e:
    #         print(f"No se pudo encontrar el elemento con el xpath especificado: {e}")
    #         return e

    def CrearDocumento(self, nombre_doc, nombre_columna, tipo, selector):
        # Obtener la ruta absoluta del archivo actual
        ruta_actual = os.path.abspath(__file__)

        # Obtener la ruta del directorio padre de la carpeta que contiene el archivo actual
        ruta_padre = os.path.dirname(os.path.dirname(ruta_actual))

        # Combinar la ruta del directorio padre con la ruta relativa a la carpeta que contiene los archivos CSV
        ruta_txt = os.path.join(ruta_padre, 'txt')

        # Combinar la ruta de la carpeta txt con el nombre del archivo CSV
        ruta_csv = os.path.join(ruta_txt, '{}.csv'.format(nombre_doc))
        # ruta_csv = "C:\\Users\\Luis Sandoval\\Documents\\Automation\\GTD-Selenium\\txt\\{}.csv".format(nombre_doc) # definir la ruta predefinida
        elemento = WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located((tipo, selector))).text
        valor = elemento
        print(valor)
        try:
            if not os.path.exists(ruta_csv):
                with open(ruta_csv, 'w', newline='', encoding='utf-8') as csvfile:
                    fieldnames = [nombre_columna]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    elemento = WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located((tipo, selector))).text
                    valor = elemento
                    valor_repleace = valor.replace('"', '').replace('\n', '')
                    writer.writerow({nombre_columna: valor_repleace})
            else:
                with open(ruta_csv, 'a', newline='', encoding='utf-8') as csvfile:
                    fieldnames = [nombre_columna]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    elemento = WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located((tipo, selector))).text
                    valor = elemento
                    valor_repleace = valor.replace('"', '').replace('\n', '')
                    writer.writerow({nombre_columna: valor_repleace})
        except Exception as e:
            print(f"Error al crear o escribir en el documento: {e}")

