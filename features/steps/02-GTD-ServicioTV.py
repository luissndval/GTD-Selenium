from behave import *

from pages.GTDServicioPage import SeleccionServicio


@when(u'Seleccionar Cobertura: "{Cobertura}" se confirma plan')
def stem_impl(context, Cobertura):
    try:
        SeleccionServicio.ContinuarCoberturaTV(context, Cobertura)
    except:
        context.driver.close()
        assert False, "La prueba fallo en : ----->>> Seleccionar Cobertura:  se confirma plan"


@when(u'Se Realiza click en continuar')
def step_impl(context):
    try:
        SeleccionServicio.ContinuarServicioTV(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en: ----->>> Realizar Click Continuar"
