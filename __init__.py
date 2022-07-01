import json

from mycroft import MycroftSkill, intent_file_handler

# Fichero JSON donde almacenar la informacion
ficheroJSON = "/home/serggom/scraping/datos.json"


class MensajesSinLeerCampus(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('campus.leer.sin.mensajes.intent')
    def handle_campus_leer_sin_mensajes(self, message):

        # Lectura de la informacion del fichero JSON
        with open(ficheroJSON) as ficheroMensajes:
            data = json.load(ficheroMensajes)
            if (data['mensajes'][0]['totales_sin_leer'] == "0"):
                self.speak("No tienes ningun mensaje sin leer")

            elif (data['mensajes'][0]['totales_sin_leer'] == "1"):
                self.speak("Tienes un mensaje sin leer")

            else:
                self.speak("Tienes " + data['mensajes'][0]['totales_sin_leer'] + " mensajes sin leer")

        ficheroMensajes.close()


def create_skill():
    return MensajesSinLeerCampus()
