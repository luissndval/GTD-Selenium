Usuario=	"//input[@id='username']"

Password=	"//input[@type='password']"

IniciarSesion=	"//span[contains(.,'Iniciar Sesión')]"

TituloValidate=	"//h1[contains(.,'Dashboard')]"

balloon=	"//span[contains(.,'Balloon')]"

report=	"(//span[contains(.,'Report')])[1]"

createHiring=	"//span[contains(.,'Create Hiring')]"

SeleccionPlan=	"//li/..//span[contains(.,'{Plan}')]//..//a[contains(.,'Generate Hiring')]"
Region=	"//input[contains(@id,'region')]"

###################VALIDAR FACTIBILIDAD##############################
Comuna=	"//input[@id='commune']"

Calle=	"//input[contains(@id,'street')]"

Numero=	"//input[contains(@id,'number')]"

Depto=	"//input[@id='flat']"

Nombre=	"//input[contains(@id,'name')]"

Celular=	"//input[@data-msg-required='El teléfono ingresado no es válido.']"

Email=	"//input[@id='email_hiring']"

ValidarDatos=	"//p[contains(.,'Validar Datos')]"

RutServicio = "//input[@id='rut']"


#####################SERVICIOS E INTERESES##########################


ConfirmarPlan = "//p[contains(.,'Confirmar Plan')]"
TambienInteresConfirmar = "//p[contains(.,'Continuar')]"


#####################Fecha/Horario##########################

Horario = "(//li[@class='clsAvailableHour'])[1]"


#############CONFIRMACION#################
EnviarLink="//p[contains(.,'Enviar link')]"


COntinuarHorario = "//p[contains(.,'Continuar')]"

#####################
RutPatPass="(//input[@name='custom_attributes[rut]'][@placeholder='Ej: 12345678-9'])[3]"
SeriePatPass="(//input[contains(@name,'1]')])[3]"
rut = "(//span[text()='RUT']//..//..//div//input[@name='custom_attributes[rut]'])[2]"
rutBoleta = "(//input[@name='custom_attributes[rut]'])[3]"
SerieBoleta= "(//input[contains(@name,'1]')])[3]"
Serie = "(//input[contains(@name,'1]')])[2]"
AceptoTyC = "//span[contains(@id,'check4')]"
ContinuarDatos = "//span[contains(.,'Continuar')]"
################ PATPASS ##############