from abc import ABC, abstractmethod


class DoneError(Exception):
    pass


class Webinar(ABC):
    def __init__(self):
        self.webinar = False

    def on(self):
        if self.webinar:
            raise DoneError("Webinar is already opened.")
        self.webinar = True
        print("Webinar is offically on.")


    def off(self):
        if not self.webinar:
            raise DoneError("Webinar is already closed.")
        self.webinar = False
        print("Webinar is officially closed.")
   

@abstractmethod
def webinar_is(self):
    pass


class LiveWebinar(Webinar):
    def webinar_is(self):
        print("Webinar is Live.")


class RecordedWebinar(Webinar):
    def webinar_is(self):
        print("Webinar is Recorded.")


class AlltypeWebiner(Webinar):
    pass


webinar_type = Webinar()
webinar_type.on()
