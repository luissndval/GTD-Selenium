Feature: Solicitud Servicio

  Scenario Outline: Solicitud Servicio "<TestCase>"
    Given  Iniciando Navegador en la Web : "<Web>"
    When Se selecciona region: "<Region>"
    When Se selecciona Comuna: "<Comuna>
    When Se selecciona Calle y Numero: "<Calle>" , "<Numero>"
    When Se ingresa Nombre y Apellido : "<Nombre>"
    When se ingresa Numero de contacto: "<Contacto>"
    When se ingresa Correo electronico : "<Email>"
    When Seleccionar Cobertura: "<Cobertura>" y Realizar click en Confirmar Plan
    When Seleccionar Algun Interes: "<Interes>"
    When Seleccionar Fecha y horario Disponible
    When Confirmar contratacion, Elegir metodo de Pago "<Pago>" ingresar Rut "<Rut>" ingresar "<Serie>"
    When Se visualiza Ventana Patpass, se completan los campos Numero de Tarjeta: "<Tar>" y Ciudad
    When Se visualiza Pantalla Transbank se Completa Rut: "<RutPago>" y  Clave: "<Clave>"
    When Se tilda la casilla "Acepto terminos y condiciones" , se realiza click Continuar.
    Then Se valida la obtencion del id de la solicitud realizada

    Examples:
      | Web                     | Region        | Comuna     | Calle           | Numero | Nombre          | Contacto  | Email         | Cobertura         | Interes               | Pago                  | Rut          | Serie | TestCase | Tar                 | Clave | RutPago      |
      | /plan-internet-600.html | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | ELLIOT LEOPOLDO | 957544722 | test@test.com | Plan Internet 600 | Microsoft 365 Familia | Pago Automático (PAT) | 36.628.878-3 | XXXX  | GB1      | 4051-8856-0044-6623 | 123   | 11.111.111-1 |
#      | /plan-internet-800.html | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | ELLIOT LEOPOLDO | 957544722 | test@test.com | Plan Internet 800 | Router Eero Amazon    | Pago Automático (PAT) | 36.628.878-3  | XXXX | GB2      | 4051-8856-0044-6623 | 123   | 11.111.111-1 |
#      | /plan-internet-giga.html                                | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | ELLIOT LEOPOLDO | 957544722 | test@test.com | Plan Internet GIGA                                      | Router Eero Amazon    | Pago Automático (PAT) | 10340004-K | 106493750 | GB3      |         |      |
#      | /plan-internet-2-gigas.html                             | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | ELLIOT LEOPOLDO | 957544722 | test@test.com | Plan Internet 2 Gigas                                   | Router Eero Amazon    | Pago Automático (PAT) | 10340004-K | 106493750 | GB4      |         |      |
#      | /duopack-600-internet-fibra-television.html             | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | ELLIOT LEOPOLDO | 957544722 | test@test.com | Duopack 600 (Internet fibra + Televisión)               | TNT Sport Premium     | Pago Automático (PAT) | 10340004-K | 106493750 | GB5      |         |      |
#      | /duopack-800-internet-fibra-television.html             | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | ELLIOT LEOPOLDO | 957544722 | test@test.com | Duopack 800 (Internet fibra + Televisión)               | TNT Sport Premium     | Pago Automático (PAT) | 10340004-K | 106493750 | GB6      |         |      |
#      | /duopack-giga-internet-fibra-television.html            | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | ELLIOT LEOPOLDO | 957544722 | test@test.com | Duopack GIGA (Internet fibra + Televisión)              | TNT Sport Premium     | Pago Automático (PAT) | 10340004-K | 106493750 | GB7      |         |      |
#      | /duopack-2-giga-internet-fibra-television.html          | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | ELLIOT LEOPOLDO | 957544722 | test@test.com | Duopack 2 GIGA (Internet fibra + Televisión)            | TNT Sport Premium     | Pago Automático (PAT) | 10340004-K | 106493750 | GB8      |         |      |
#      | /duopack-600-internet-fibra-telefonia.html              | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | ELLIOT LEOPOLDO | 957544722 | test@test.com | Duopack 600 (Internet fibra + Telefonía)                | Router Eero Amazon    | Pago Automático (PAT) | 10340004-K | 106493750 | GB9      |         |      |
#      | /duopack-800-internet-fibra-telefonia.html              | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | ELLIOT LEOPOLDO | 957544722 | test@test.com | Duopack 800 (Internet fibra + Telefonía)                | Router Eero Amazon    | Pago Automático (PAT) | 10340004-K | 106493750 | GB10     |         |      |
#      | /duopack-giga-internet-fibra-telefonia.html             | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | ELLIOT LEOPOLDO | 957544722 | test@test.com | Duopack GIGA (Internet fibra + Telefonía)               | Router Eero Amazon    | Pago Automático (PAT) | 10340004-K | 106493750 | GB11     |         |      |
#      | /tripack-600-internet-fibra-television-telefonia.html   | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | ELLIOT LEOPOLDO | 957544722 | test@test.com | Tripack 600 (Internet fibra + GTD TV + Telefonía)       | TNT Sport Premium     | Pago Automático (PAT) | 10340004-K | 106493750 | GB12     |         |      |
#      | /tripack-800-internet-fibra-television-telefonia.html   | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | ELLIOT LEOPOLDO | 957544722 | test@test.com | Tripack 800 (Internet fibra + Televisión + Telefonía)   | Router Eero Amazon    | Pago Automático (PAT) | 10340004-K | 106493750 | GB13     |         |      |
#      | /tripack-giga-internet-fibra-television-telefonia.html  | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | ELLIOT LEOPOLDO | 957544722 | test@test.com | Tripack GIGA (Internet fibra + Televisión + Telefonía)  | Hbo pack              | Pago Automático (PAT) | 10340004-K | 106493750 | GB14     |         |      |
#      | tripack-2-giga-internet-fibra-television-telefonia.html | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | ELLIOT LEOPOLDO | 957544722 | test@test.com | Tripack 2 GIGA(Internet fibra + Televisión + Telefonía) | Hbo pack              | Pago Automático (PAT) | 10340004-K | 106493750 | GB15     |         |      |
