Feature: Telsur contratacion de servicio

  Scenario Outline:
    Given Se inica navegador y nos dirigimos a la url: "https://mcstaging.tienda.telsur.cl""<Web>"
    When Se selecciona Region: "<Region>".
    When Seleccionar comuna: "<comuna>"
    When Se selecciona Calle y Numero: "<Calle>" , "<Numero>".
    When Se ingresa Nombre y Apellido : "<Nombre>".
    When Se ingresa Rut: "<Rut>".
    When se ingresa Numero de contacto: "<Contacto>".
    When Se ingresa Nombre y Apellido : "<Nombre>".
    When se ingresa Correo electronico : "<Email>".
    When Seleccionar Cobertura: "<Cobertura>" y Realizar click en Confirmar Plan.
    When Seleccionar Algun Interes: "<Interes>".
    When Seleccionar Fecha y horario Disponible.
    When Confirmar contratacion del Servicio, Elegir metodo de Pago "<Pago>"  ingresar: "<Serie>".
    Then Se valida la obtencion del id de la solicitud realizada.


    Examples:
      | Web                     | Region   | comuna   | Calle                         | Numero | Nombre          | Contacto  | Email         | Cobertura         | Interes               | Pago         | Rut       | Serie      | TestCase | Tar                 | Clave | RutPago      |
      | /plan-internet-600.html | LOS RIOS | VALDIVIA | INTENDENTE RICARDO OLEA SILVA | 979    | ELLIOT LEOPOLDO | 957544722 | test@test.com | Plan Internet 600 | Microsoft 365 Familia | Pago Mensual | 107033572 | A018961170 | TB1      | 4051-8856-0044-6623 | 123   | 11.111.111-1 |