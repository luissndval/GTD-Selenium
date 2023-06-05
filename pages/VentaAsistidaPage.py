import time

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pyperclip

from Funciones.Funciones import funciones_2_0
from elements import VistaAsistidaElements
from elements import ElementSeleccionServicios

t = 3
t2 = 5
t3 = 10


class VentaAsistida(funciones_2_0):
    def __init__(self, driver):
        super().__init__(driver)

    def OpenBrowser(self, Web):
        funciones_2_0.driver_Chrome(self)
        funciones_2_0.browser(self, Web)
        funciones_2_0.screenShot(self, "Navegador-Iniciado")
        time.sleep(t2)

    def LoginAdmin(self, Usuario, Contraseña):
        funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Usuario, Usuario)
        funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Password, Contraseña)
        funciones_2_0.screenShot(self, "Usuario-Contraseña")
        funciones_2_0.click_Field(self, By.XPATH, VistaAsistidaElements.IniciarSesion)

    def BalloonReport(self):
        funciones_2_0.validates(self, By.XPATH, VistaAsistidaElements.TituloValidate)
        funciones_2_0.click_Field(self, By.XPATH, VistaAsistidaElements.balloon)
        funciones_2_0.click_Field(self, By.XPATH, VistaAsistidaElements.report)
        funciones_2_0.screenShot(self, "Generacion Reporte")

    def CreateHiring(self):
        funciones_2_0.screenShot(self, "Hiring")
        funciones_2_0.click_Field(self, By.XPATH, VistaAsistidaElements.createHiring)

    def PlanGenerate(self, PlanGenerate):
        funciones_2_0.screenShot(self, "Hiring")
        funciones_2_0.click_Field(self, By.XPATH,
                                  f"//li/..//span[contains(.,'{PlanGenerate}')]//..//a[contains(.,'Generate Hiring')]")
        funciones_2_0.screenShot(self, "Hiring")

    def Pestaña(self):
        funciones_2_0.Change_Ventana(self)
        funciones_2_0.validates(self, By.XPATH, VistaAsistidaElements.Comuna)
        time.sleep(5)

    def Formulario(self, Plataforma, Region, Comuna, Calle, Numero, Departamento, Nombre, Telefono, Correo, Rut):

        if Plataforma == "GTD":
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Region, Region)
            funciones_2_0.click_Field(self, By.XPATH, f"//div[text()='{Region}']")
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Comuna, Comuna)
            funciones_2_0.click_Field(self, By.XPATH, f"//div[text()='{Comuna}']")
            time.sleep(t2)
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Calle, Calle)
            funciones_2_0.click_Field(self, By.XPATH, f"//div[text()='{Calle}']")
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Numero, Numero)
            funciones_2_0.click_Field(self, By.XPATH, f"//div[text()='{Numero}']")
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Depto, Departamento)
            funciones_2_0.click_Field(self, By.XPATH, f"//div[@class='option element'][contains(.,'{Departamento}')]")
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Nombre, Nombre)
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Numero, Numero)
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Celular, Telefono)
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Email, Correo)
            funciones_2_0.screenShot(self, "Hiring")
            funciones_2_0.click_Field(self, By.XPATH, VistaAsistidaElements.ValidarDatos)

        else:
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Region, Region)
            funciones_2_0.click_Field(self, By.XPATH, f"//div[text()='{Region}']")
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Comuna, Comuna)
            funciones_2_0.click_Field(self, By.XPATH, f"//div[text()='{Comuna}']")
            time.sleep(t2)
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Calle, Calle)
            funciones_2_0.click_Field(self, By.XPATH, f"//div[text()='{Calle}']")
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Numero, Numero)
            funciones_2_0.click_Field(self, By.XPATH, f"//div[text()='{Numero}']")
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Depto, Departamento)
            funciones_2_0.click_Field(self, By.XPATH, f"//div[@class='option element'][contains(.,'{Departamento}')]")
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Nombre, Nombre)
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Celular, Telefono)
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Email, Correo)
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.RutServicio, Rut)
            funciones_2_0.screenShot(self, "Elementos Validados")
            funciones_2_0.screenShot(self, "Hiring")
            funciones_2_0.click_Field(self, By.XPATH, VistaAsistidaElements.ValidarDatos)

    def SeleccionarCobertura(self, Cobertura):
        time.sleep(5)
        funciones_2_0.click_Field(self, By.XPATH, f"//h3[text()='{Cobertura}']")
        time.sleep(t2)
        funciones_2_0.screenShot(self, "Cobertura")
        funciones_2_0.click_Field(self, By.XPATH, ElementSeleccionServicios.ConfirmarPlan)
        time.sleep(t3)

    def InteresesOpciones(self, Interes):
        funciones_2_0.click_Field(self, By.XPATH, f"//h3[contains(.,'{Interes}')]")
        funciones_2_0.screenShot(self, "Intereses")
        funciones_2_0.click_Field(self, By.XPATH, ElementSeleccionServicios.TambienInteresConfirmar)
        time.sleep(t2)

    def SeleccionarFecha(self):
        try:
            WebDriverWait(self.driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@class='qs-square LUN qs-num']")))
            funciones_2_0.click_Field(self, By.XPATH, "//div[@class='qs-square LUN qs-num']")
            funciones_2_0.screenShot(self, "Fecha")
            funciones_2_0.click_Field(self, By.XPATH, ElementSeleccionServicios.Horario)
            funciones_2_0.click_Field(self, By.XPATH, ElementSeleccionServicios.COntinuarHorario)
            time.sleep(t2)
        except TimeoutException:
            dias_semana = ["LUN", "MAR", "MIER", "JUE", "VIE", "SAB", "DOM"]
            for dia in dias_semana:
                dias_sin_comillas = dia.replace('"', '')
                xpath_variable = f"//div[@class='qs-square {dias_sin_comillas} qs-num']"
                try:
                    elemento_variable = self.driver.find_element(By.XPATH, xpath_variable)
                    elemento_variable.click()
                    break
                except NoSuchElementException:
                    continue
            funciones_2_0.click_Field(self, By.XPATH, ElementSeleccionServicios.Horario)
            funciones_2_0.click_Field(self, By.XPATH, ElementSeleccionServicios.COntinuarHorario)


    def CalleyAltura(self, Plataforma, Region, Comuna, Calle, Numero, Nombre, Telefono, Correo, Rut):
        if Plataforma == "GTD":
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Region, Region)
            funciones_2_0.click_Field(self, By.XPATH, f"//div[text()='{Region}']")
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Comuna, Comuna)
            funciones_2_0.click_Field(self, By.XPATH, f"//div[text()='{Comuna}']")
            time.sleep(t2)
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Calle, Calle)
            funciones_2_0.click_Field(self, By.XPATH, f"//div[text()='{Calle}']")
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Numero, Numero)
            funciones_2_0.click_Field(self, By.XPATH, f"//div[text()='{Numero}']")
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Nombre, Nombre)
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Celular, Telefono)
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Email, Correo)
            funciones_2_0.screenShot(self, "Hiring")
            funciones_2_0.click_Field(self, By.XPATH, VistaAsistidaElements.ValidarDatos)
        else:
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Region, Region)
            funciones_2_0.click_Field(self, By.XPATH, f"//div[text()='{Region}']")
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Comuna, Comuna)
            funciones_2_0.click_Field(self, By.XPATH, f"//div[text()='{Comuna}']")
            time.sleep(t2)
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Calle, Calle)
            funciones_2_0.click_Field(self, By.XPATH, f"//div[text()='{Calle}']")
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Numero, Numero)
            funciones_2_0.click_Field(self, By.XPATH, f"//div[text()='{Numero}']")
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Nombre, Nombre)
            funciones_2_0.input_Texto(self, By.XPATH, "(//input[@id='phone'])[2]", Telefono)
            funciones_2_0.input_Texto(self, By.XPATH, VistaAsistidaElements.Email, Correo)
            funciones_2_0.click_Field(self, By.XPATH, "//label[@for='rut']//..//input")
            funciones_2_0.input_Texto(self, By.XPATH, "//label[@for='rut']//..//input", Rut)
            funciones_2_0.screenShot(self, "Elementos Validados")
            funciones_2_0.screenShot(self, "Hiring")
            funciones_2_0.click_Field(self, By.XPATH, VistaAsistidaElements.ValidarDatos)
    #
    def SendEmail(self):
        funciones_2_0.click_Field(self,By.XPATH, VistaAsistidaElements.EnviarLink)
        time.sleep(15)
        funciones_2_0.screenShot(self,"Status-Email")

    def GetText(self):
        funciones_2_0.click_Field(self,By.XPATH,"//span[contains(@class,'bot')]")
        url = pyperclip.paste()
        self.driver.execute_script("window.open('about:blank','_blank');")
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[2])
        self.driver.get(url)
        funciones_2_0.screenShot(self,"Validacion-Redireccionamiento")






