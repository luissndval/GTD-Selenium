from behave import *

from Funciones.Funciones import funciones_2_0
from pages.GTDServicioPage import SeleccionServicio


@when(u'Seleccionar Cobertura: "{Cobertura}" se confirma plan')
def stem_impl(context, Cobertura):
    try:
        context.driver.refresh()
        SeleccionServicio.ContinuarCoberturaTV(context, Cobertura)
    except:
        context.driver.close()
        funciones_2_0.screenShot(context, "Seleccionar Cobertura:  se confirma plan")
        assert False, "La prueba fallo en : ----->>> Seleccionar Cobertura:  se confirma plan"


@when(u'Se Realiza click en continuar')
def step_impl(context):
    try:
        SeleccionServicio.ContinuarServicioTV(context)
    except:
        funciones_2_0.screenShot(context, "Click Continuar.")
        context.driver.close()
        assert False, "La prueba fallo en: ----->>> Realizar Click Continuar"
