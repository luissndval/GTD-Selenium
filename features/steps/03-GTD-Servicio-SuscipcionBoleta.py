from behave import *

from Funciones.Funciones import funciones_2_0
from pages.GTDServicioPage import SeleccionServicio


@when(u'Confirmar contratacion, se elige metodo de Pago "{Pago}" se ingresar Rut "{Rut}" se ingresar "{Serie}"')
def step_impl(context, Pago, Rut, Serie):
    try:
        context.driver.refresh()
        SeleccionServicio.SuscripcionBoletaGTD(context, Pago, Rut, Serie)
    except:
        funciones_2_0.screenShot(context,
                                 'Confirmar contratacion, Elegir metodo de Pago "{Pago}" ingresar Rut "{Rut}" ingresar "{Serie}"')
        context.driver.close()
        assert False, "La prueba fallo en :  ----->>> Confirmar contratacion Rut"
