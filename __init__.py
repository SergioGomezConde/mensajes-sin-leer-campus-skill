from mycroft import MycroftSkill, intent_file_handler


class MensajesSinLeerCampus(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('campus.leer.sin.mensajes.intent')
    def handle_campus_leer_sin_mensajes(self, message):
        self.speak_dialog('campus.leer.sin.mensajes')


def create_skill():
    return MensajesSinLeerCampus()

