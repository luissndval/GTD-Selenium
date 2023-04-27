from behave import *

from Funciones.Funciones import funciones_2_0
from pages.TELSURServicioPage import telsur


@when(u'Confirmar contratacion del Servicio, Elegir metodo de Pago "{Pago}"  ingresar: "{Serie}".')
def step_impl(context, Serie, Pago):
    try:
        telsur.SuscripcionBoletaTelsur(context, Pago, Serie)

    except:
        funciones_2_0.screenShot(context,
                                 'Se visualiza Pantalla Transbank se Completa Rut: "{RutPago}" y  Clave: "{Clave}"')
        context.driver.close()
        assert False, "La prueba fallo en :  ----->>> Confirmar contratacionRut"
