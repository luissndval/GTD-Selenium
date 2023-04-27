import time

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Funciones.Funciones import funciones_2_0
from elements import ElementSeleccionServicios
t = 1
t2 = 5
t3 = 10

class telsur(funciones_2_0):

    def __init__(self, driver):
        super().__init__(driver)

    def OpenBrowser(self, Web):
        funciones_2_0.driver_Chrome(self)
        # funciones_2_0.driver_Firefox(self)
        funciones_2_0.browser(self, f"https://mcstaging.tienda.telsur.cl{Web}")
        funciones_2_0.screenShot(self, "Navegador-Iniciado")
        time.sleep(t2)

    def InputSeleciconRegion(self, Region):
        funciones_2_0.input_Texto(self, By.XPATH, "//input[contains(@id,'region')]", Region)
        funciones_2_0.click_Field(self, By.XPATH, f"//div[text()='{Region}']")

    # def selectRegion(self):
    #     fun.click_Field( By.XPATH, f"//div[text()='METROPOLITANAS']")

    def SeleccionComuna(self, comuna):
        funciones_2_0.input_Texto(self, By.XPATH, ElementSeleccionServicios.Comuna, comuna, )
        time.sleep(t)
        funciones_2_0.click_Field(self, By.XPATH, f"//div[text()='{comuna}']")

    def CalleyAltura(self, Calle, Numero):
        time.sleep(t2)
        funciones_2_0.input_Texto(self, By.XPATH, ElementSeleccionServicios.Calle, Calle)
        time.sleep(t2)
        funciones_2_0.click_Field(self, By.XPATH, f"//div[text()='{Calle}']")
        time.sleep(t2)
        funciones_2_0.input_Texto(self, By.XPATH, ElementSeleccionServicios.NumeroCalle, Numero)
        funciones_2_0.click_Field(self, By.XPATH, f"//div[text()='{Numero}']")
        funciones_2_0.screenShot(self, "Direccion")

    def NombreApellido(self, Nombre):
        funciones_2_0.input_Texto(self, By.XPATH, ElementSeleccionServicios.NombreApellido, Nombre)
    def RutServicio (self,Rut):
        funciones_2_0.input_Texto(self, By.XPATH, ElementSeleccionServicios.RutServicio,Rut)
        time.sleep(t2)

    def Contacto(self, Contacto):
        time.sleep(10)
        funciones_2_0.input_Texto(self, By.XPATH, ElementSeleccionServicios.TelefonoTELSUR, Contacto)

    def CorreoElectronico(self, Email):
        funciones_2_0.input_Texto(self, By.XPATH, ElementSeleccionServicios.CorreoElectronico, Email)
        funciones_2_0.click_Field(self, By.XPATH, ElementSeleccionServicios.ValidarDatos)
        time.sleep(15)

    def SeleccionarCobertura(self, Cobertura):
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
            elemento = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='qs-square LUN qs-num']")))
            funciones_2_0.click_Field(self, By.XPATH, "//div[@class='qs-square LUN qs-num']")
            funciones_2_0.screenShot(self, "Fecha")
            funciones_2_0.click_Field(self, By.XPATH, ElementSeleccionServicios.Horario)
            funciones_2_0.click_Field(self, By.XPATH, ElementSeleccionServicios.COntinuarHorario)
            time.sleep(t2)
        except TimeoutException:
            dias_semana = ["LUN", "MAR", "MIER", "JUE", "VIE"]
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

    def ConfirmarContratacion(self, Pago, Rut, Serie):
        funciones_2_0.click_Field(self, By.XPATH, f"//p[contains(.,'{Pago}')]")
        time.sleep(t)
        funciones_2_0.click_Field(self, By.XPATH, "//button[contains(.,'Entendido')]")
        funciones_2_0.scrollToElement(self, By.XPATH, ElementSeleccionServicios.rut)
        funciones_2_0.input_Texto(self, By.XPATH, ElementSeleccionServicios.Serie, Serie)
        funciones_2_0.click_Field(self, By.XPATH, ElementSeleccionServicios.AceptoTyC)
        funciones_2_0.click_Field(self, By.XPATH, ElementSeleccionServicios.ContinuarDatos)
        funciones_2_0.screenShot(self, "Confirmacion")
        time.sleep(15)

    def PatPass(self, Tar):
        funciones_2_0.click_Field(self, By.XPATH, ElementSeleccionServicios.TarjetaPasPass)
        funciones_2_0.input_Texto_visibility(self, By.XPATH, ElementSeleccionServicios.TarjetaPasPass, Tar)
        time.sleep(1)
        funciones_2_0.click_Field(self, By.XPATH, ElementSeleccionServicios.ListaCity)
        funciones_2_0.key_Up_Key_Down(self, Keys.ARROW_DOWN)
        funciones_2_0.key_Up_Key_Down(self, Keys.ENTER)
        time.sleep(1)
        funciones_2_0.screenShot(self, "Tarjeta-Ciudad")
        time.sleep(1)
        funciones_2_0.click_Field(self, By.XPATH, ElementSeleccionServicios.AceptarPATPASS)
        time.sleep(t2)

    def transbank(self, RutPago, Clave):
        funciones_2_0.screenShot(self, "Pantalla-Transbank")
        funciones_2_0.Iframe(self, By.XPATH, "//iframe[contains(@name,'iframeId')]")
        time.sleep(10)
        funciones_2_0.input_Texto_ActionChains(self, By.XPATH, ElementSeleccionServicios.TransbankRutClientInput,RutPago)
        funciones_2_0.input_Texto_ActionChains(self, By.XPATH, ElementSeleccionServicios.TransbankPassClientInput,Clave)
        funciones_2_0.clickAction(self, By.XPATH, ElementSeleccionServicios.TransbankSubmitButton)
        time.sleep(t2)
        funciones_2_0.screenShot(self, "Confirmar-Pago")
        funciones_2_0.click_Field(self, By.XPATH, ElementSeleccionServicios.TransbankConfirmarPago)
        time.sleep(15)

    def ValPatPass(self, ):
        funciones_2_0.click_Field(self, By.XPATH, ElementSeleccionServicios.PatpassCheckTyC)
        time.sleep(t)
        funciones_2_0.screenShot(self, "Confirmar-Suscripcion")
        time.sleep(t)
        funciones_2_0.click_Field(self, By.XPATH, ElementSeleccionServicios.PatPassSuscribir)
        time.sleep(t2)

    def IdValidate(self, ):
        funciones_2_0.validates(self, By.XPATH, ElementSeleccionServicios.validate)

    def ValidarSolicitud(self, ):
        funciones_2_0.validates(self, By.XPATH, ElementSeleccionServicios.validate)
        funciones_2_0.validates(self, By.XPATH, ElementSeleccionServicios.IDValidateGTD)

    def ContinuarServicioTV(self, ):
        funciones_2_0.click_Field(self, By.XPATH, ElementSeleccionServicios.TambienInteresConfirmar)

    def ContinuarCoberturaTV(self, Cobertura):
        funciones_2_0.click_Field(self, By.XPATH, f"//h3[@class='selected-product'][contains(.,'{Cobertura}')]")
        funciones_2_0.click_Field(self, By.XPATH, ElementSeleccionServicios.ConfirmarPlan)
