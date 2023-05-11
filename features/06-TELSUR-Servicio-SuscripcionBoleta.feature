@Regresion
Feature: Telsur contratacion de servicio


  Scenario Outline:
    Given Se inica navegador y nos dirigimos a la url: "https://mcstaging.tienda.telsur.cl""<Web>"
    When Se selecciona Region: "<Region>".
    When Seleccionar comuna: "<comuna>"
#    When Se selecciona Calle y Numero: "<Calle>" , "<Numero>".
#    When Se selecciona Calle , Numero , Depto: "<Calle>" , "<Numero>" ["<Depto>"]
    When Se selecciona Calle , Numero , Depto: "<Calle>" , "<Numero>" ["<Depto>"]
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
      | Web                                                   | Region   | comuna   | Calle                         | Numero | Nombre          | Contacto  | Email                           | Cobertura                                           | Interes               | Pago         | Rut        | Serie      | TestCase | Tar                 | Clave | RutPago      | Depto |
      | /plan-internet-600.html                               | LOS RIOS | VALDIVIA | AVENIDA PEDRO AGUIRRE CERDA   | 1387   | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Plan Internet 600                                   | Microsoft 365 Familia | Pago Mensual | 14025552-1  | 514189381  | TEL-1    | 4051-8856-0044-6623 | 123   | 11.111.111-1 |       |
      | /plan-internet-800.html                               | LOS RIOS | VALDIVIA | PASAJE SIETE                  | 314    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Plan Internet 800                                   | Router Eero Amazon    | Pago Mensual | 14066768-4 | A022860204 | TEL-2    |                     |       |              |       |
      | /plan-internet-giga.html                              | LOS RIOS | VALDIVIA | CALAFQUEN                     | 221    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Plan Internet 2 Gigas                               | Router Eero Amazon    | Pago Mensual | 14227309-8 | 513357163  | TEL-3    |                     |       |              |       |
      | /plan-internet-2-gigas.html                           | LOS RIOS | VALDIVIA | PASAJE SANTA MARTA            | 3855   | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack 600 (Internet fibra + GTD TV)               | TNT Sport Premium     | Pago Mensual | 14263380-9 | 103525449  | TEL-4    |                     |       |              |       |
      | /duopack-600-internet-fibra-television.html           | LOS RIOS | VALDIVIA | KULCZEWSKI                    | 369    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack 800 (Internet fibra + GTD TV)               | TNT Sport Premium     | Pago Mensual | 14332968-2 | 111051544  | TEL-5    |                     |       |              |       |
      | /duopack-800-internet-fibra-television.html           | LOS RIOS | VALDIVIA | CALLEJON EL ROMANCE           | 332    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack GIGA (Internet fibra + GTD TV)              | TNT Sport Premium     | Pago Mensual | 14374710-7 | 107007806  | TEL-6    |                     |       |              |       |
      | /duopack-giga-internet-fibra-television.html          | LOS RIOS | VALDIVIA | AVENIDA PEDRO MONTT           | 2010   | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack 2 GIGA (Internet fibra + GTD TV)            | TNT Sport Premium     | Pago Mensual | 14481689-7 | 520106799  | TEL-7    |                     |       |              |       |
      | /duopack-2-giga-internet-fibra-television.html        | LOS RIOS | VALDIVIA | VALLE HONDO                   | 2764   | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack 600 (Internet fibra + Telefonía)            | Router Eero Amazon    | Pago Mensual | 14570804-4 | 517553243  | TEL-8    |                     |       |              |       |
      | /duopack-600-internet-fibra-telefonia.html            | LOS RIOS | VALDIVIA | PASAJE UNO                    | 578    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack 800 (Internet fibra + Telefonía)            | Router Eero Amazon    | Pago Mensual | 14594848-7 | 109341273  | TEL-9    |                     |       |              |       |
      | /duopack-800-internet-fibra-telefonia.html            | LOS RIOS | VALDIVIA | PASAJE SAN JUAN               | 3001   | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack GIGA (Internet fibra + Telefonía)           | Router Eero Amazon    | Pago Mensual | 15174341-2 | 522596064  | TEL-10   |                     |       |              |       |
      | /duopack-giga-internet-fibra-telefonia.html           | LOS RIOS | VALDIVIA | PASAJE TARAPACA               | 749    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Tripack 600 (Internet fibra + GTD TV + Telefonía)   | TNT Sport Premium     | Pago Mensual | 15275722-0 | A029502225 | TEL-11   |                     |       |              |       |
      | /tripack-600-internet-fibra-television-telefonia.html | LOS RIOS | VALDIVIA | INTENDENTE RICARDO OLEA SILVA | 945    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Tripack 800 (Internet fibra + GTD TV + Telefonía)   | Router Eero Amazon    | Pago Mensual | 15282951-5 | 152829515  | TEL-12   |                     |       |              |       |
      | /tripack-800-internet-fibra-television-telefonia.html | LOS RIOS | VALDIVIA | PASAJE VOLCAN QUETRUPILLAN    | 4633   | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Tripack GIGA (Internet fibra + GTD TV + Telefonía)  | Hbo pack              | Pago Mensual | 15381675-1 | A028773639 | TEL-13   |                     |       |              |       |
      | /tripack-giga-internet-fibra                          | LOS RIOS | VALDIVIA | JOSE VICTORINO LASTARRIA      | 2532   | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Tripack 2 GIGA(Internet fibra + GTD TV + Telefonía) | Hbo pack              | Pago Mensual | 15418683-2 | A030845570 | TEL-14   |                     |       |              |       |
