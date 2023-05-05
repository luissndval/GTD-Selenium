import csv
import os

from lxml import etree


# with open('./txt/ABMORGANISMO.csv') as csvfile:
#     Reader= csv.DictReader(csvfile)
#     for row in Reader:
#              print(row['Organismo'], row['Status'])
#
class CreateWriterRead():
    def __init__(self, driver):
        self.driver = driver

    def CrearDocumento(self, NombreDoc, NombreColumna, tipo, Xpath):
        dir_path = r"../txt/"
        file_name = f"{NombreDoc}.csv"
        file_path = os.path.join(dir_path, file_name)
        element = self.driver.find_elemet(tipo, Xpath)
        texto = element.text

        if not os.path.exists(file_path):
            with open(file_path, 'w', newline='') as csv_file:
                fieldnames = [NombreColumna]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({NombreColumna: texto})
        else:
            tree = etree.parse(file_path)
            root = tree.getroot()
            if NombreColumna not in root[0].keys():
                with open(file_path, 'a', newline="") as csv_file:
                    fieldnames = [NombreColumna]
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writerow({NombreColumna: texto})
            else:
                with open(file_path, 'a', newline="") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow([texto])

        # Capturamos el texto del elemento con el xpath especificado

        # Escribimos el texto capturado en la columna especificada
        with open(file_path, 'a', newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([texto])
