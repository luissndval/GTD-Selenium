from behave import *

from pages.SeleccionServicioPage import SeleccionServicio


@when(u'Seleccionar Cobertura: "{Cobertura}" se confirma plan')
def stem_impl(context, Cobertura):
    try:
        SeleccionServicio.ContinuarCoberturaTV(Cobertura)
    except TimeoutError:

        context.driver.close()
        step.failed("La prueba fallo en : ----->>> Seleccionar Cobertura:  se confirma plan")

@when(u'Se Realiza click en continuar')
def step_impl(context):
    try:
        SeleccionServicio.ContinuarServicioTV()
    except TimeoutError:

        context.driver.close()
        step.failed("La prueba fallo en: ----->>> Realizar Click Continuar")
