from datetime import time
from telnetlib import EC

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Funciones.Funciones import funciones_2_0
from pages.VentaAsistidaPage import VentaAsistida

@given(u'Se inicia el navegador , el vendedor ingresa a la pagina web "{Web}"')
def step_impl(context,Web):
    try:
        VentaAsistida.OpenBrowser(context,Web)
    except:
        context.driver.close()
        assert False, "FALLO EN:  Se inicia el navegador"


@when(u'El vendedor Inicia sesion con Usuario y contraseña: "{Usuario}" "{Contraseña}"')
def step_impl(context,Usuario,Contraseña):
    try:
        VentaAsistida.LoginAdmin(context,Usuario,Contraseña)
    except:
        context.driver.close()
        assert False,"FALLO EN: Inicia sesion "


@when(u'Como vendedor se localiza el panel "Balloon" se realiza click sobre "Report"')
def step_impl(context):
    try:
        VentaAsistida.BalloonReport(context)
    except:
        context.driver.close()
        assert False, "FALLO EN: se localiza el panel Balloon"


@when(u'Se realiza click sobre "Create Hiring"')
def step_impl(context):
    try:
        VentaAsistida.CreateHiring(context)
    except:
        context.driver.close()
        assert False, "FALLO EN: Create hiring"


@when(u'Se selecciona Plan a generar "{PlanGenerate}"')
def step_impl(context,PlanGenerate):
    try:
        VentaAsistida.PlanGenerate(context,PlanGenerate)
    except:
        context.driver.close()
        assert False, "FALLO EN: Generacion de plan"


@when(u'Se inica una nueva Pestaña en el Navegador.')
def step_impl(context):
    try:
        VentaAsistida.Pestaña(context)
    except:
        context.driver.close()
        assert False, "FALLO EN: Pestaña Nueva"

@when(u'"{Plataforma}" Se completan los datos necesarios en el formulario, Region: "{Region}", Comuna: "{Comuna}", Calle: "{Calle}", Numero: "{Numero}", Departamento: [{Departamento}], Nombre: "{Nombre}", Telefono: "{Telefono}", Correo: "{Correo}", Rut: "{Rut}"')
def step_impl(context,Plataforma,Region,Comuna,Calle,Numero,Departamento,Nombre,Telefono,Correo,Rut):
    try:
        Departamento = Departamento.strip('[]"')
        if Departamento and len(Departamento.strip()) > 0 and not Departamento.strip() == ",":
            VentaAsistida.Formulario(context,Plataforma,Region,Comuna,Calle,Numero,Departamento,Nombre,Telefono,Correo,Rut)
        else:
            VentaAsistida.CalleyAltura(context,Plataforma,Region,Comuna,Calle,Numero,Nombre,Telefono,Correo,Rut)
            funciones_2_0.screenShot(context, f"Se selecciona Calle y Numero: '{Calle}' '{Numero}'")
    except:
        context.driver.close()
        assert False, "FALLO EN: FORMULARIO"




@when(u'Se Selecciona Cobertura: "{Cobertura}" y se realiza click en Confirmar Plan')
def step_impl(context,Cobertura):
    try:
        VentaAsistida.SeleccionarCobertura(context,Cobertura)
    except:
        context.driver.close()
        assert False, "FALLO EN: SELECCION COBERTURA"



@when(u'Se selecciona Algun Interes: "{Interes}"')
def step_impl(context,Interes):
    try:
        VentaAsistida.InteresesOpciones(context,Interes)
    except:
        context.driver.close()
        assert False, "FALLO EN: SELECCION INTERES"



@when(u'Se Selecciona Fecha y horario Disponible')
def step_impl(context):
    try:
        VentaAsistida.SeleccionarFecha(context)
    except:
        context.driver.close()
        assert False, "FALLO EN:  Fecha y horario Disponible"

@when(u'Se realiza Click sobre "ENVIAR LINK"')
def step_impl(context):
    try:
        VentaAsistida.SendEmail(context)
        validador= context.driver.find_element(By.XPATH, "//small[@data-bind='text: successMsg']").text
        print(validador)
        if validador=="Enviado":
            VentaAsistida.GetText(context)
        else:
            context.driver.close()
    except:
        context.driver.close()
        assert False, "FALLO EN:  Fecha y horario Disponible"
#
#
# @when(u'Se Valida el Envio de email.')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When Se Valida el Envio de email.')