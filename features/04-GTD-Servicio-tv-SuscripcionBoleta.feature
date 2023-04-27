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
    When Confirmar contratacion, se elige metodo de Pago "<Pago>" se ingresar Rut "<Rut>" se ingresar "<Serie>"
    Then Se valida la obtencion del id de la solicitud realizada

    Examples:
      | Web                              | Region        | Comuna     | Calle           | Numero | Nombre          | Contacto  | Email         | Ciudad | Cobertura                  | Pago                  | Rut          | Serie | TestCase | Tar                 | Clave | RutPago      |
      | /television-entretenido-max.html | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | ELLIOT LEOPOLDO | 957544722 | test@test.com |        | Television Entretenido max | Pago Mensual | 36.628.878-3 | XXXX  | GTD-16   | 4051-8856-0044-6623 | 123   | 11.111.111-1 |