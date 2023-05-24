Feature: Solicitud Servicio

  @regresion
  Scenario Outline: Solicitud Servicio "<TestCase>"
    Given  Iniciando Navegador en la Web : "<Web>"
    When Se selecciona region: "<Region>"
    When Se selecciona Comuna: "<Comuna>
    When Se selecciona Calle y Numero: "<Calle>" , "<Numero>", Depto ["<Depto>"]
#    When Se selecciona Calle y Numero: "<Calle>" , "<Numero>"
#    When Se selecciona Calle , Numero , Depto: "<Calle>" , "<Numero>" ["<Depto>"]
    When Se ingresa Nombre y Apellido : "<Nombre>"
    When se ingresa Numero de contacto: "<Contacto>"
    When se ingresa Correo electronico : "<Email>"
    When Seleccionar Cobertura: "<Cobertura>" y Realizar click en Confirmar Plan
    When Seleccionar Algun Interes: "<Interes>"
    When Seleccionar Fecha y horario Disponible
    When Confirmar contratacion, se elige metodo de Pago "<Pago>" se ingresar Rut "<Rut>" se ingresar "<Serie>"
    Then Se valida la obtencion del id de la solicitud realizada

    Examples:
      | Web                                                    | Region        | Comuna     | Calle           | Numero | Nombre          | Contacto  | Email                           | Cobertura                                          | Interes               | Pago         | Rut       | Serie      | TestCase   | Tar                 | Clave | RutPago      | Depto |
      | /plan-internet-600.html                                | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Plan Internet 600                                  | Microsoft 365 Familia | Pago Mensual | 106318891 | 103699471  | GTD-SPB-1  | 4051-8856-0044-6623 | 123   | 11.111.111-1 |       |
      | /plan-internet-800.html                                | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Plan Internet 800                                  | Router Eero Amazon    | Pago Mensual | 126998279 | 104170613  | GTD-SPB-2  | 4051-8856-0044-6623 | 123   | 11.111.111-1 | F     |
      | /duopack-600-internet-fibra-television.html            | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack 600 (Internet fibra + GTD TV)              | TNT Sport Premium     | Pago Mensual | 142096250 | A027688580 | GTD-SPB-3  | 4051-8856-0044-6623 | 123   | 11.111.111-1 |       |
      | /duopack-800-internet-fibra-television.html            | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack 800 (Internet fibra + GTD TV)              | TNT Sport Premium     | Pago Mensual | 160893362 | 109875278  | GTD-SPB-4  | 4051-8856-0044-6623 | 123   | 11.111.111-1 |       |
      | /duopack-giga-internet-fibra-television.html           | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack GIGA (Internet fibra + GTD TV)             | TNT Sport Premium     | Pago Mensual | 17343264K | 515818185  | GTD-SPB-5  | 4051-8856-0044-6623 | 123   | 11.111.111-1 |       |
      | /duopack-600-internet-fibra-telefonia.html             | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack 600 (Internet fibra + Telefonía)           | Router Eero Amazon    | Pago Mensual | 176172223 | 524892172  | GTD-SPB-6  | 4051-8856-0044-6623 | 123   | 11.111.111-1 |       |
      | /duopack-800-internet-fibra-telefonia.html             | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack 800 (Internet fibra + Telefonía)           | Router Eero Amazon    | Pago Mensual | 263337441 | 601614117  | GTD-SPB-7  | 4051-8856-0044-6623 | 123   | 11.111.111-1 |       |
      | /duopack-giga-internet-fibra-telefonia.html            | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack GIGA (Internet fibra + Telefonía)          | Router Eero Amazon    | Pago Mensual | 81851948  | 524918471  | GTD-SPB-8  | 4051-8856-0044-6623 | 123   | 11.111.111-1 |       |
      | /tripack-600-internet-fibra-television-telefonia.html  | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Tripack 600 (Internet fibra + GTD TV + Telefonía)  | TNT Sport Premium     | Pago Mensual | 106318891 | 103699471  | GTD-SPB-9  | 4051-8856-0044-6623 | 123   | 11.111.111-1 |       |
      | /tripack-800-internet-fibra-television-telefonia.html  | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Tripack 800 (Internet fibra + GTD TV + Telefonía)  | Router Eero Amazon    | Pago Mensual | 126998279 | 104170613  | GTD-SPB-10 | 4051-8856-0044-6623 | 123   | 11.111.111-1 |       |
      | /tripack-giga-internet-fibra-television-telefonia.html | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Tripack GIGA (Internet fibra + GTD TV + Telefonía) | Hbo pack              | Pago Mensual | 142096250 | A027688580 | GTD-SPB-11 | 4051-8856-0044-6623 | 123   | 11.111.111-1 |       |
