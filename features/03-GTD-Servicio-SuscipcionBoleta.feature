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
    When Confirmar contratacion, se elige metodo de Pago "<Pago>" se ingresar Rut "<Rut>" se ingresar "<Serie>"
    Then Se valida la obtencion del id de la solicitud realizada

    Examples:
      | Web                                                      | Region        | Comuna     | Calle           | Numero | Nombre          | Contacto  | Email                           | Cobertura                                           | Interes               | Pago         | Rut       | Serie | TestCase   | Tar                 | Clave | RutPago      | Depto |
      | /plan-internet-600.html                                  | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Plan Internet 600                                   | Microsoft 365 Familia | Pago Mensual | 183924494 | XXXX  | GTD-SPB-1  | 4051-8856-0044-6623 | 123   | 11.111.111-1 |       |
      | /plan-internet-800.html                                  | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Plan Internet 800                                   | Router Eero Amazon    | Pago Mensual | 183924494 | XXXX  | GTD-SPB-2  | 4051-8856-0044-6623 | 123   | 11.111.111-1 | F     |
      | /plan-internet-2-gigas.html                              | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Plan Internet 2 Gigas                               | Router Eero Amazon    | Pago Mensual | 183924494 | XXXX  | GTD-SPB-4  | 4051-8856-0044-6623 | 123   | 11.111.111-1 |       |
      | /duopack-600-internet-fibra-television.html              | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack 600 (Internet fibra + GTD TV)               | TNT Sport Premium     | Pago Mensual | 183924494 | XXXX  | GTD-SPB-5  | 4051-8856-0044-6623 | 123   | 11.111.111-1 |       |
      | /duopack-800-internet-fibra-television.html              | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack 800 (Internet fibra + GTD TV)               | TNT Sport Premium     | Pago Mensual | 183924494 | XXXX  | GTD-SPB-5  | 4051-8856-0044-6623 | 123   | 11.111.111-1 |       |
      | /duopack-giga-internet-fibra-television.html             | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack GIGA (Internet fibra + GTD TV)              | TNT Sport Premium     | Pago Mensual | 183924494 | XXXX  | GTD-SPB-6  | 4051-8856-0044-6623 | 123   | 11.111.111-1 |       |
      | /duopack-2-giga-internet-fibra-television.html           | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack 2 GIGA (Internet fibra + GTD TV)            | TNT Sport Premium     | Pago Mensual | 183924494 | XXXX  | GTD-SPB-7  | 4051-8856-0044-6623 | 123   | 11.111.111-1 |       |
      | /duopack-600-internet-fibra-telefonia.html               | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack 600 (Internet fibra + Telefonía)            | Router Eero Amazon    | Pago Mensual | 183924494 | XXXX  | GTD-SPB-8  | 4051-8856-0044-6623 | 123   | 11.111.111-1 |       |
      | /duopack-800-internet-fibra-telefonia.html               | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack 800 (Internet fibra + Telefonía)            | Router Eero Amazon    | Pago Mensual | 183924494 | XXXX  | GTD-SPB-9  | 4051-8856-0044-6623 | 123   | 11.111.111-1 |       |
      | /duopack-giga-internet-fibra-telefonia.html              | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack GIGA (Internet fibra + Telefonía)           | Router Eero Amazon    | Pago Mensual | 183924494 | XXXX  | GTD-SPB-10 | 4051-8856-0044-6623 | 123   | 11.111.111-1 |       |
      | /tripack-600-internet-fibra-television-telefonia.html    | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Tripack 600 (Internet fibra + GTD TV + Telefonía)   | TNT Sport Premium     | Pago Mensual | 183924494 | XXXX  | GTD-SPB-11 | 4051-8856-0044-6623 | 123   | 11.111.111-1 |       |
      | /tripack-800-internet-fibra-television-telefonia.html    | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Tripack 800 (Internet fibra + GTD TV + Telefonía)   | Router Eero Amazon    | Pago Mensual | 183924494 | XXXX  | GTD-SPB-12 | 4051-8856-0044-6623 | 123   | 11.111.111-1 |       |
      | /tripack-giga-internet-fibra-television-telefonia.html   | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Tripack GIGA (Internet fibra + GTD TV + Telefonía)  | Hbo pack              | Pago Mensual | 183924494 | XXXX  | GTD-SPB-13 | 4051-8856-0044-6623 | 123   | 11.111.111-1 |       |
      | /tripack-2-giga-internet-fibra-television-telefonia.html | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Tripack 2 GIGA(Internet fibra + GTD TV + Telefonía) | Hbo pack              | Pago Mensual | 183924494 | XXXX  | GTD-SPB-14 | 4051-8856-0044-6623 | 123   | 11.111.111-1 |       |
