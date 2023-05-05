import argparse
import subprocess

if __name__ == '__main__':
    p = argparse.ArgumentParser()

    # --testdir command line argument added

    p.add_argument('--testdir', required=False, help="File path")

    a = p.parse_args()

    t01 = "01-GTD-Servicio-PATPASS.feature"  # PATPASS Desactivado.
    t02 = "02-GTD-Servicio-tv-PATPASS.feature"  # PATPASS Desactivado
    t03 = "03-GTD-Servicio-SuscipcionBoleta.feature"
    t04 = "04-GTD-Servicio-tv-SuscripcionBoleta.feature"
    t05 = "05-TELSUR-Servicio-PATPASS.feature"
    t06 = "06-TELSUR-Servicio-SuscripcionBoleta.feature"

    # testdir = f"C:\\proyectos\\Turnera\\turnera-backend-administracion\\TestAutomation\\features\\{t03}"  # PUEDES INDICAR EL SCRIPT A EJECUTAR

    testdir = f"..\\features\\{t01}"  # PUEDES INDICAR EL SCRIPT A EJECUTAR

    # complete command

    c = f'behave --no-capture {testdir}'

    s = subprocess.run(c, shell=True, check=True)
