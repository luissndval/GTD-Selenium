from behave import *

from Funciones.Funciones import funciones_2_0
from pages.TELSURServicioPage import telsur


@given(u'Se inica navegador y nos dirigimos a la url: "https://mcstaging.tienda.telsur.cl""{Web}"')
def step_impl(context, Web):
    try:
        telsur.OpenBrowser(context, Web)
    except:
        funciones_2_0.screenShot(context, "Fallo al iniciar navegador")
        context.driver.close()
        assert False, "La prueba fallo en: ----->>> Iniciando Navegador"


@when(u'Se selecciona Region: "{Region}".')
def step_impl(context, Region):
    try:
        telsur.InputSeleciconRegion(context, Region)
    except:
        funciones_2_0.screenShot(context, "Se selecciona region: '{Region}'")
        context.driver.close()
        assert True, "La prueba Fallo en: ----->>> Seleccione Region"


@when(u'Seleccionar comuna: "{comuna}"')
def step_impl(context, comuna):
    try:
        telsur.SeleccionComuna(context, comuna)
    except:
        funciones_2_0.screenShot(context, "Se selecciona region: '{comuna}'")
        context.driver.close()
        assert True, "La prueba Fallo en: ----->>> Seleccione Region"


@when(u'Se selecciona Calle y Numero: "{Calle}" , "{Numero}".')
def step_impl(context, Calle, Numero):
    try:
        telsur.CalleyAltura(context, Calle, Numero)
    except:
        funciones_2_0.screenShot(context, "Se selecciona Calle y Numero: '{Calle}' '{Numero}'")
        context.driver.close()
        assert False, "La prueba fallo: ----->>> en Seleccionar calle y numero"


@when(u'Se ingresa Nombre y Apellido : "{Nombre}".')
def step_impl(context, Nombre):
    try:
        telsur.NombreApellido(context, Nombre)
    except:
        funciones_2_0.screenShot(context, 'Se ingresa Nombre y Apellido : "{Nombre}"')
        context.driver.close()
        assert False, "La prueba fallo: ----->>> Se ingresa Nombre y Apellido : '{Nombre}'"


@when(u'Se ingresa Rut: "{Rut}".')
def step_impl(context, Rut):
    try:
        telsur.RutServicio(context, Rut)
    except:
        funciones_2_0.screenShot(context, 'Se ingresa Rut: "{Rut}".')
        context.driver.close()
        assert False, "La prueba fallo: ----->>> Se ingresa Rut: '{Rut}'."


@when(u'se ingresa Numero de contacto: "{Contacto}".')
def step_impl(context, Contacto):
    try:
        telsur.Contacto(context, Contacto)
    except:
        funciones_2_0.screenShot(context, 'se ingresa Numero de contacto: "{Contacto}"')
        context.driver.close()
        assert False, "La prueba fallo en : ----->>> ingresar numero de contacto"


@when(u'se ingresa Correo electronico : "{Email}".')
def step_impl(context, Email):
    try:
        telsur.CorreoElectronico(context, Email)
    except:
        funciones_2_0.screenShot(context, 'se ingresa Correo electronico : "{Email}"')
        context.driver.close()
        assert False, "La prueba fallo en: ----->>> ingresar correo electronico"


@when(u'Seleccionar Cobertura: "{Cobertura}" y Realizar click en Confirmar Plan.')
def step_impl(context, Cobertura):
    try:
        telsur.SeleccionarCobertura(context, Cobertura)
    except:
        funciones_2_0.screenShot(context, 'Seleccionar Cobertura: "{Cobertura}" y Realizar click en Confirmar Plan')
        context.driver.close()
        assert False, "la prueba fallo: ----->>> en realizar click confirmar plan"


@when(u'Seleccionar Algun Interes: "{Interes}".')
def step_impl(context, Interes):
    try:
        telsur.InteresesOpciones(context, Interes)
    except:
        funciones_2_0.screenShot(context, 'Seleccionar Algun Interes: "{Interes}"')
        context.driver.close()
        assert False, "Seleccionar Algun Interes: '{Interes}'"


@when(u'Seleccionar Fecha y horario Disponible.')
def step_impl(context):
    try:
        telsur.SeleccionarFecha(context)
    except:
        funciones_2_0.screenShot(context, 'Seleccionar Fecha y horario Disponible')
        context.driver.close()
        assert False, "La prueba fallo en:  ----->>> Seleccionar fecha y horario"


@when(u'Confirmar contratacion, Elegir metodo de Pago "{Pago}"  ingresar: "{Serie}".')
def step_impl(context, Pago, Serie):
    try:
        telsur.ConfirmarContratacion(context, Pago, Serie)
    except:
        funciones_2_0.screenShot(context, "No-Contraseña")
        context.driver.close()
        assert False, "La prueba fallo en :  ----->>> Confirmar contratacionRut"


@when(u'Se visualiza Ventana Patpass, se completan los campos Numero de Tarjeta: "{Tar}" y Ciudad.')
def step_impl(context, Tar):
    try:
        telsur.PatPass(context, Tar)
    except:
        funciones_2_0.screenShot(context,
                                 'Se visualiza Ventana Patpass, se completan los campos Numero de Tarjeta: "{Tar}" y Ciudad')
        context.driver.close()
        assert False, "La prueba fallo en :  ----->>> Confirmar contratacionRut"


@when(u'Se visualiza Pantalla Transbank se Completa Rut: "{RutPago}" y  Clave: "{Clave}".')
def step_impl(context, RutPago, Clave):
    try:
        telsur.transbank(context, RutPago, Clave)
    except:
        funciones_2_0.screenShot(context,
                                 'Se visualiza Pantalla Transbank se Completa Rut: "{RutPago}" y  Clave: "{Clave}"')
        context.driver.close()
        assert False, "La prueba fallo en :  ----->>> Confirmar contratacionRut"


@when(u'se realiza click sobre la casilla "Acepto terminos y condiciones" , se realiza click Continuar.')
def step_impl(context, RutPago, Clave):
    try:
        telsur.transbank(context, RutPago, Clave)
    except:
        funciones_2_0.screenShot(context,
                                 'Se visualiza Pantalla Transbank se Completa Rut: "{RutPago}" y  Clave: "{Clave}"')
        context.driver.close()
        assert False, "La prueba fallo en :  ----->>> Confirmar contratacionRut"


@then(u'Se valida la obtencion del id de la solicitud realizada.')
def step_impl(context):
    try:
        telsur.ValidarSolicitud(context, )
        context.driver.close()
    except:
        funciones_2_0.screenShot(context, 'Se valida la obtencion del id de la solicitud realizada')
        context.driver.close()
        assert False, "La prueba fallo en :  ----->>> Se tilda la casilla Acepto terminos y condiciones"
