Feature: Venta Asistida.


  Scenario Outline: Como vendedor oficial de Gtd y Telsur , debe poder ingresar y asisitr la compra del usuario.
    Given Se inicia el navegador , el vendedor ingresa a la pagina web "<Web>"
    When El vendedor Inicia sesion con Usuario y contraseña: "<Usuario>" "<Contraseña>"
    When Como vendedor se localiza el panel "Balloon" se realiza click sobre "Report"
    When Se realiza click sobre "Create Hiring"
    When Se selecciona Plan a generar "<PlanGenerate>"
    When Se inica una nueva Pestaña en el Navegador.
    When "<Plataforma>" Se completan los datos necesarios en el formulario, Region: "<Region>", Comuna: "<Comuna>", Calle: "<Calle>", Numero: "<Numero>", Departamento: ["<Departamento>"], Nombre: "<Nombre>", Telefono: "<Telefono>", Correo: "<Correo>", Rut: "<Rut>"
    When Se Selecciona Cobertura: "<Cobertura>" y se realiza click en Confirmar Plan
    When Se selecciona Algun Interes: "<Interes>"
    When Se Selecciona Fecha y horario Disponible
    When Se realiza Click sobre "ENVIAR LINK"
#    When Se Valida el Envio de email.

    Examples:
      | Web                                   | Usuario | Contraseña | PlanGenerate                                            | Plataforma | Region    | Comuna | Calle            | Numero | Departamento | Nombre          | Rut        | Telefono  | Correo                          | Cobertura                                         | Interes           | Serie |
#      | https://mcstaging.tienda.gtd.cl/admin | sluis01 | Temporal01 | Plan Internet 600(GB1)                                  | GTD        | METROPOLITANA | LAS CONDES | CERRO PROVINCIA  | 125    |              | Testing Balloon | 366288783  | 957544722 | luis.sandoval@balloon-group.com | Plan Internet 600 | Microsoft 365 Familia | XXXX  |
      | https://mcstaging.tienda.gtd.cl/admin | sluis01 | Temporal01 | Tripack 600 (Internet fibra + GTD TV + Telefonía)(TB12) | TELSUR     | LOS LAGOS | OSORNO | PASAJE LOS ULMOS | 2377   |              | Testing Balloon | 17198252-9 | 957544722 | luis.sandoval@balloon-group.com | Tripack 600 (Internet fibra + GTD TV + Telefonía) | Router Eero Amazon  |       |
#      | https://mcstaging.tienda.gtd.cl/admin | sluis01 | Temporal01 | Duopack 600 (Internet fibra + GTD TV)(GB5)              | GTD        | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    |              | Testing Balloon | 366288783 | 957544722 | luis.sandoval@balloon-group.com | Duopack 600 (Internet fibra + GTD TV)             | TNT Sport Premium   | XXXX  |
#      | https://mcstaging.tienda.gtd.cl/admin | sluis01 | Temporal01 | Duopack 800 (Internet fibra + GTD TV)(GB6)              | GTD        | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    |              | Testing Balloon | 366288783 | 957544722 | luis.sandoval@balloon-group.com | Duopack 800 (Internet fibra + GTD TV)             | TNT Sport Premium   | XXXX  |
#      | https://mcstaging.tienda.gtd.cl/admin | sluis01 | Temporal01 | Duopack 600 (Internet fibra + Telefonía)(GB9)           | GTD        | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    |              | Testing Balloon | 366288783 | 957544722 | luis.sandoval@balloon-group.com | Duopack 600 (Internet fibra + Telefonía)          | Router Eero Amazon  | XXXX  |
#      | https://mcstaging.tienda.gtd.cl/admin | sluis01 | Temporal01 | Duopack 800 (Internet fibra + Telefonía)(GB10)          | GTD        | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    |              | Testing Balloon | 366288783 | 957544722 | luis.sandoval@balloon-group.com | Duopack 800 (Internet fibra + Telefonía)          | Router Eero Amazon  | XXXX  |
#      | https://mcstaging.tienda.gtd.cl/admin | sluis01 | Temporal01 | Duopack GIGA (Internet fibra + Telefonía)(GB11)         | GTD        | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    |              | Testing Balloon | 366288783 | 957544722 | luis.sandoval@balloon-group.com | Duopack GIGA (Internet fibra + Telefonía)         | Router Eero Amazon  | XXXX  |
#      | https://mcstaging.tienda.gtd.cl/admin | sluis01 | Temporal01 | Tripack 600 (Internet fibra + GTD TV + Telefonía)(GB12) | GTD        | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    |              | Testing Balloon | 366288783 | 957544722 | luis.sandoval@balloon-group.com | Tripack 600 (Internet fibra + GTD TV + Telefonía) | TNT Sport Premium   | XXXX  |
#      | https://mcstaging.tienda.gtd.cl/admin | sluis01 | Temporal01 | Tripack 800 (Internet fibra + GTD TV + Telefonía)(GB13) | GTD        | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    |              | Testing Balloon | 366288783 | 957544722 | luis.sandoval@balloon-group.com | Tripack 800 (Internet fibra + GTD TV + Telefonía) | Router Eero Amazon  | XXXX  |
#
#
#
#
