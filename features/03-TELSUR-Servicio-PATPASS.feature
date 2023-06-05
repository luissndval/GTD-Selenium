Feature: Telsur contratacion de servicio Patpass

  Scenario Outline:
    Given Se inica navegador y nos dirigimos a la url: "<Web>"
    When Se selecciona Region: "<Region>".
    When Seleccionar comuna: "<comuna>"
    When Se selecciona Calle , Numero , Depto: "<Calle>" , "<Numero>" ["<Depto>"]
    When Se ingresa Nombre y Apellido : "<Nombre>".
    When Se ingresa Rut: "<Rut>".
    When se ingresa Numero de contacto: "<Contacto>".
    When Se ingresa Nombre y Apellido : "<Nombre>".
    When se ingresa Correo electronico : "<Email>".
    When Seleccionar Cobertura: "<Cobertura>" y Realizar click en Confirmar Plan.
    When Seleccionar Algun Interes: "<Interes>".
    When Seleccionar Fecha y horario Disponible.
    When Confirmar contratacion del Servicio, Elegir metodo de Pago "<Pago>"  ingresar: "<Serie>".
    When Se visualiza Ventana Patpass, se completan los campos Numero de Tarjeta: "<Tar>" y Ciudad.
    When Se visualiza Pantalla Transbank se Completa Rut: "<RutPago>" y  Clave: "<Clave>"
    When se realiza click sobre la casilla "Acepto terminos y condiciones" , se realiza click Continuar.
    Then Se valida la obtencion del id de la solicitud realizada.


    Examples:
      | Web                                                       | Region    | comuna | Calle            | Numero | Nombre          | Contacto  | Email                           | Cobertura         | Interes               | Pago                  | Rut       | Serie      | TestCase | Tar                 | Clave | RutPago      |
      | https://mcstaging.tienda.telsur.cl/plan-internet-600.html | LOS LAGOS | OSORNO | PASAJE LOS ULMOS | 2377   | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Plan Internet 600 | Microsoft 365 Familia | Pago Automático (PAT) | 107033572 | A018961170 | TB1      | 4051-8856-0044-6623 | 123   | 11.111.111-1 |
#      | https://mcstaging.tienda.telsur.cl/plan-internet-800.html                               | BIO BIO  | CONCEPCION | SAN LUCAR DE BARRAMERA | 2972    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Plan Internet 800                                   | Router Eero Amazon    | Pago Mensual          | 17198252-9 | 522502206  | TEL-2    | 4051-8856-0044-6623 | 123   | 11.111.111-1 |
#      | https://mcstaging.tienda.telsur.cl/duopack-600-internet-fibra-television.html           | BIO BIO  | CONCEPCION | PASAJE ALMERIA         | 2937    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack 600 (Internet fibra + GTD TV)               | TNT Sport Premium     | Pago Mensual          | 17197407-0 | 517961131  | TEL-5    | 4051-8856-0044-6623 | 123   | 11.111.111-1 |
#      | https://mcstaging.tienda.telsur.cl/duopack-800-internet-fibra-television.html           | BIO BIO  | CONCEPCION | VILLANUEVA             | 1554    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack 800 (Internet fibra + GTD TV)               | TNT Sport Premium     | Pago Mensual          | 17198252-9 | 522502206  | TEL-6    | 4051-8856-0044-6623 | 123   | 11.111.111-1 |
#      | https://mcstaging.tienda.telsur.cl/duopack-giga-internet-fibra-television.html          | BIO BIO  | CONCEPCION | VILLANUEVA             | 3030    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack GIGA (Internet fibra + GTD TV)              | Router Eero Amazon    | Pago Mensual          | 17197407-0 | 517961131  | TEL-7    | 4051-8856-0044-6623 | 123   | 11.111.111-1 |
#      | https://mcstaging.tienda.telsur.cl/duopack-600-internet-fibra-telefonia.html            | BIO BIO  | CONCEPCION | JESUS PALOU            | 3034    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack 800 (Internet fibra + Telefonía)            | Router Eero Amazon    | Pago Mensual          | 17198252-9 | 522502206  | TEL-8    | 4051-8856-0044-6623 | 123   | 11.111.111-1 |
#      | https://mcstaging.tienda.telsur.cl/duopack-800-internet-fibra-telefonia.html            | BIO BIO  | CONCEPCION | JESUS PALOU            | 3038    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack GIGA (Internet fibra + Telefonía)           | Router Eero Amazon    | Pago Mensual          | 17197407-0 | 517961131  | TEL-9    | 4051-8856-0044-6623 | 123   | 11.111.111-1 |
#      | https://mcstaging.tienda.telsur.cl/duopack-giga-internet-fibra-telefonia.html           | BIO BIO  | CONCEPCION | VALENCIA               | 1085-12 | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Tripack 600 (Internet fibra + GTD TV + Telefonía)   | TNT Sport Premium     | Pago Mensual          | 17198252-9 | 522502206  | TEL-10   | 4051-8856-0044-6623 | 123   | 11.111.111-1 |
#      | https://mcstaging.tienda.telsur.cl/tripack-600-internet-fibra-television-telefonia.html | BIO BIO  | CONCEPCION | VALENCIA               | 1085    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Tripack 800 (Internet fibra + GTD TV + Telefonía)   | Router Eero Amazon    | Pago Mensual          | 17197407-0 | 517961131  | TEL-11   | 4051-8856-0044-6623 | 123   | 11.111.111-1 |
#      | https://mcstaging.tienda.telsur.cl/tripack-800-internet-fibra-television-telefonia.html | BIO BIO  | CONCEPCION | VALENCIA               | 3075    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Tripack GIGA (Internet fibra + GTD TV + Telefonía)  | Hbo pack              | Pago Mensual          | 17198252-9 | 522502206  | TEL-12   | 4051-8856-0044-6623 | 123   | 11.111.111-1 |
#      | https://mcstaging.tienda.telsur.cl/tripack-giga-internet-fibra                          | BIO BIO  | CONCEPCION | VALENCIA               | 1085-8  | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Tripack 2 GIGA(Internet fibra + GTD TV + Telefonía) | Hbo pack              | Pago Mensual          | 17197407-0 | 517961131  | TEL-13   | 4051-8856-0044-6623 | 123   | 11.111.111-1 |
##      | Web