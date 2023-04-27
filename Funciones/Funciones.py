import os
import time
import warnings
import csv
import allure
from allure_commons.types import AttachmentType
from lxml import etree
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

    ############################################################################################
    ################################## element_to_be_clickable##################################
    ############################################################################################

    def browser(self, link):
        self.driver.get(link)
        self.driver.maximize_window()
        print("Página abierta: " + str(link))

    def input_Texto(self, tipo, selector, texto):
        WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((tipo, selector))).send_keys(texto)
        time.sleep(1)
        print("\n Escribir en el campo {} el texto -> {} ".format(selector, texto))

    def click_Field(self, tipo, selector):
        WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((tipo, selector))).click()
        time.sleep(2)
        print("\n Click sobre el elemento -> {} ".format(selector))

    def clear_Field(self, tipo, selector):
        WebDriverWait(self.driver, timeout=10).until(EC.element_to_be_clickable((tipo, selector))).clear()
        print("\n Texto eliminado -> {} ".format(selector))

    def validates(self, tipo, selector):
        element = WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located((tipo, selector))).text
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
        WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((tipo, selector))).send_keys(
            texto)
        time.sleep(1)
        print("\n Escribir en el campo {} el texto -> {} ".format(selector, texto))

    def click_Field_visibility(self, tipo, selector):
        WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((tipo, selector))).click()
        time.sleep(2)
        print("\n Click sobre el elemento -> {} ".format(selector))

    def clear_Field_visibility(self, tipo, selector):
        WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((tipo, selector))).clear()
        print("\n Texto eliminado -> {} ".format(selector))

    def validates_visibility(self, tipo, selector):
        element = WebDriverWait(self.driver, timeout=10).until(
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

    import csv
    import os
    from lxml import etree

    # with open('./txt/ABMORGANISMO.csv') as csvfile:
    #     Reader= csv.DictReader(csvfile)
    #     for row in Reader:
    #              print(row['Organismo'], row['Status'])
    #

    # def CrearDocumento(self, NombreDoc, tipo ,selector,NameColum):
    #
    #     dir_path = r"../txt"
    #     file_name = NombreDoc
    #     file_path = os.path.join(dir_path, file_name)
    #     texto = WebDriverWait(self.driver, timeout=10).until(
    #         EC.visibility_of_element_located((tipo, selector))).text
    #     try:
    #         Validate = os.path.exists(NombreDoc)
    #         if Validate == False:
    #             with open(file_path, 'w', newline='') as csvfile:
    #                 fieldnames = [NameColum]
    #                 writer = csv.DictWriter(csvfile, fieldnames=fieldnames, )
    #                 writer.writeheader()
    #                 writer.writerow({NameColum: texto})
    #
    #         else:
    #
    #             with open(file_path, 'a', newline="") as csv_file:
    #                 fieldnames = [NameColum]
    #                 Dates = ([{NameColum: texto}])
    #                 writer = csv.DictWriter(csv_file, fieldnames=fieldnames, )
    #                 for row in Dates:
    #                     writer.writerow(row)
    #     except:
    #         assert True
    # def CrearDocumento(self, NombreDoc,tipo, selector):
    #
    #     dir_path = r"../txt"
    #     file_name = NombreDoc
    #     file_path = os.path.join(dir_path, file_name)
    #     Capturado = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((tipo, selector))).text
    #     print(Capturado)
    #     try:
    #         Validate = os.path.exists(dir_path)
    #         if Validate == False:
    #             with open(file_path, 'w', newline='') as csvfile:
    #                 fieldnames = ["ID-Operacion"]
    #                 writer = csv.DictWriter(csvfile, fieldnames=fieldnames, )
    #                 writer.writeheader()
    #                 writer.writerow({'Nombre': Capturado})
    #
    #         else:
    #
    #             with open(file_path, 'a', newline="") as csv_file:
    #                 fieldnames = ["ID-Operacion"]
    #                 Dates = ([{'ID-Operacion': Capturado}])
    #                 writer = csv.DictWriter(csv_file, fieldnames=fieldnames, )
    #                 for row in Dates:
    #                     writer.writerow(row)
    #     except:
    #         assert True

    def CrearDocumento(self, nombre_doc: str, nombre_columna: str, tipo, selector):
        ruta_csv = "..\\txt\\{}.csv".format(nombre_doc)  # definir la ruta predefinida
        elemento = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((tipo, selector))).text
        valor = elemento
        print(valor)
        try:
            if not os.path.exists(ruta_csv):
                with open(ruta_csv, 'w', newline='', encoding='utf-8') as csvfile:
                    fieldnames = [nombre_columna]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    valor_repleace = valor.replace('"', '').replace('\n','')
                    writer.writerow({nombre_columna: valor_repleace})
            else:
                with open(ruta_csv, 'a', newline='', encoding='utf-8') as csvfile:
                    fieldnames = [nombre_columna]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    elemento = WebDriverWait(self.driver, timeout=10).until(
                        EC.visibility_of_element_located((tipo, selector))).text
                    valor = elemento
                    valor_repleace = valor.replace('"', '').replace('\n','')
                    writer.writerow({nombre_columna: valor_repleace})
        except Exception as e:
            print(f"Error al crear o escribir en el documento: {e}")

        # Captura el texto del elemento con el xpath especificado
        try:
            elemento = WebDriverWait(self.driver, timeout=10).until(
                EC.visibility_of_element_located((tipo, selector))).text
        except Exception as e:
            print(f"No se pudo encontrar el elemento con el xpath especificado: {e}")
            return
    # def CrearDocumento(self,nombre_doc: str,nombre_columna: str,tipo, selector):
    #     ruta_csv = "..\\txt\\{}".format(nombre_doc)  # definir la ruta predefinida
    #     elemento = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((tipo, selector))).text
    #     valor = elemento
    #     print(valor)
    #     try:
    #         if not os.path.exists(ruta_csv):
    #             with open(ruta_csv, 'w', newline='') as csvfile:
    #                 fieldnames = [nombre_columna]
    #                 writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #                 writer.writeheader()
    #                 valor_repleace = valor.replace('"', '')
    #                 writer.writerow({nombre_columna: valor_repleace})
    #         else:
    #             with open(ruta_csv, 'a', newline='') as csvfile:
    #                 fieldnames = [nombre_columna]
    #                 writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #                 elemento = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((tipo, selector))).text
    #                 valor = elemento
    #                 valor_repleace = valor.replace('"', '')
    #                 writer.writerow({nombre_columna: valor_repleace})
    #     except Exception as e:
    #         print(f"Error al crear o escribir en el documento: {e}")
    #
    #     # Captura el texto del elemento con el xpath especificado
    #     try:
    #         elemento = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((tipo, selector))).text
    #     except Exception as e:
    #         print(f"No se pudo encontrar el elemento con el xpath especificado: {e}")
    #         return

        # # Escribe el texto capturado en la columna correspondiente del archivo CSV
        # try:
        #     with open(ruta_csv, 'a', newline='') as csvfile:
        #         fieldnames = [nombre_columna]
        #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #         writer.writerow({nombre_columna: valor})
        # except Exception as e:
        #     print(f"Error al escribir en el documento: {e}")

