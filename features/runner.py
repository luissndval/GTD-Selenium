import argparse
import subprocess

if __name__ == '__main__':
    p = argparse.ArgumentParser()

    # --testdir command line argument added

    p.add_argument('--testdir', required=False, help="File path")

    a = p.parse_args()

    t01 = ""
    t02 = ""
    t03 = ""

    # testdir = f"C:\\proyectos\\Turnera\\turnera-backend-administracion\\TestAutomation\\features\\{t03}"  # PUEDES INDICAR EL SCRIPT A EJECUTAR

    testdir = f"..\\features\\{t01}"  # PUEDES INDICAR EL SCRIPT A EJECUTAR

    # complete command

    c = f'behave --no-capture {testdir}'

    s = subprocess.run(c, shell=True, check=True)
