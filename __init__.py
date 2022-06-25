import time

from mycroft import MycroftSkill, intent_file_handler
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def inicio_sesion(self):
    # Datos de acceso fijos
    usuario = 'e71180769r'
    contrasena = 'p5irZ9Jm4@9C#6WUaE!z9%@V'

    # Modo headless
    options = Options()
    options.headless = True
    options.add_argument("--windows-size=1920,1200")

    self.speak("Buscando la informacion...")

    # Acceso a pagina
    driver = webdriver.Chrome(options=options)
    driver.get('https://campusvirtual.uva.es/login/index.php')

    # Inicio de sesion
    driver.find_element(by=By.NAME, value='adAS_username').send_keys(usuario)
    driver.find_element(
        by=By.NAME, value='adAS_password').send_keys(contrasena)
    driver.find_element(by=By.NAME, value='adAS_submit').click()

    # Aceptar cookies
    driver.implicitly_wait(10)
    driver.find_element(
        by=By.XPATH, value='/html/body/div[1]/div/a[1]').click()

    return driver


class MensajesSinLeerCampus(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('campus.leer.sin.mensajes.intent')
    def handle_campus_leer_sin_mensajes(self, message):
        driver = inicio_sesion(self)

        # Acceso a la seccion de mensajes
        driver.get('https://campusvirtual.uva.es/message/index.php')

        # Obtencion del numero de mensajes totales sin leer
        driver.implicitly_wait(5)
        numeroMensajes = str(driver.find_element(
            by=By.XPATH, value='/html/body/nav/ul[2]/div[3]/a/div').get_attribute('aria-label').split(' ')[1])

        # Respuesta con el numero de mensajes totales sin leer
        if(numeroMensajes == "0"):
            self.speak("No tienes ningun mensaje sin leer")

        elif(numeroMensajes == "1"):
            self.speak("Tienes un mensaje sin leer")

        else:
            self.speak("Tienes " + numeroMensajes + " mensajes sin leer")

        driver.close()


def create_skill():
    return MensajesSinLeerCampus()
