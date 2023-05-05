@Regresion
Feature: Telsur contratacion de servicio


  Scenario Outline:
    Given Se inica navegador y nos dirigimos a la url: "https://mcstaging.tienda.telsur.cl""<Web>"
    When Se selecciona Region: "<Region>".
    When Seleccionar comuna: "<comuna>"
    When Se selecciona Calle y Numero: "<Calle>" , "<Numero>".
#    When Se selecciona Calle y Numero: "<Calle>" , "<Numero>", Depto "<Depto>"
    When Se ingresa Nombre y Apellido : "<Nombre>".
    When Se ingresa Rut: "<Rut>".
    When se ingresa Numero de contacto: "<Contacto>".
    When se ingresa Correo electronico : "<Email>".
    When Seleccionar Cobertura: "<Cobertura>" y Realizar click en Confirmar Plan.
    When Seleccionar Algun Interes: "<Interes>".
    When Seleccionar Fecha y horario Disponible.
    When Confirmar contratacion del Servicio, Elegir metodo de Pago "<Pago>"  ingresar: "<Serie>".
    Then Se valida la solicitud realizada.


    Examples:
      | Web                     | Region   | comuna   | Calle            | Numero | Nombre          | Contacto  | Email         | Cobertura         | Interes               | Pago         | Rut       | Serie     | TestCase | Tar                 | Clave | RutPago      | Depto |
      | /plan-internet-800.html | LOS RIOS | VALDIVIA | PASAJE SAN JUAN  | 3121   | ELLIOT LEOPOLDO | 957544722 | test@test.com | Plan Internet 800 | Microsoft 365 Familia | Pago Mensual | 143747107 | 107007806 | TB1      | 4051-8856-0044-6623 | 123   | 11.111.111-1 | a     |

      | /plan-internet-800.html | LOS RIOS | VALDIVIA | PASAJE SAN PABLO | 3180   | ELLIOT LEOPOLDO | 957544722 | test@test.com | Plan Internet 800 | Microsoft 365 Familia | Pago Mensual | 144816897 | 520106799 | TB1      | 4051-8856-0044-6623 | 123   | 11.111.111-1 | 2     |