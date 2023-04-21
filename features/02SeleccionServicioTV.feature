Feature: Inicio de Sesion con Datos Validos


  Scenario Outline: Inicio de Sesion con Datos Validos"<TestCase>".
    Given  Iniciando Navegador en la Web : "<Web>"
    When Se selecciona region: "<Region>"
    When Se selecciona Comuna: "<Comuna>
    When Se selecciona Calle y Numero: "<Calle>" , "<Numero>"
    When Se ingresa Nombre y Apellido : "<Nombre>"
    When se ingresa Numero de contacto: "<Contacto>"
    When se ingresa Correo electronico : "<Email>"
    When Seleccionar Cobertura: "<Cobertura>" se confirma plan
    When Se Realiza click en continuar
    When Seleccionar Fecha y horario Disponible
    Then Confirmar contratacion, Elegir metodo de Pago "<Pago>" ingresar Rut "<Rut>" ingresar "<Serie>"
#    When Se visualiza Ventana Patpass, se completan los campos Numero de Tarjeta: "<Tarjeta>" y Ciudad "<Ciudad>"
##    When Se tilda la casilla "Acepto terminos y condiciones" , se realiza click Continuar.
    Examples:
      | Web                              | Region        | Comuna     | Calle           | Numero | Nombre          | Contacto  | Email         | Ciudad | Cobertura                  | Pago                  | Rut          | Serie | TestCase | Tarejta |  |
      | /television-entretenido-max.html | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | ELLIOT LEOPOLDO | 957544722 | test@test.com |        | Television Entretenido max | Pago Automático (PAT) | 36.628.878-3 | XXXX  | GB1      |         |  |