class DoneError(Exception):
    pass


class Webinar:
    def __init__(self):
        self.webinar = False

    def on(self):
        if self.webinar:
            raise DoneError("Webinar is already opened.")
        self.webinar = True


    def off(self):
        if not self.webinar:
            raise DoneError("Webinar is already closed.")
        self.webinar = False
webinar = Webinar()
webinar.on()


