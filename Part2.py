from abc import ABC, abstractmethod


class DoneError(Exception):
    pass


class Webinar(ABC):
    def __init__(self):
        self.on = False

    def on(self):
        if self.on:
            raise DoneError("Webinar is already opened.")
        else:
            self.on = True

    def off(self):
        if not self.on:
            raise DoneError("Webinar is already closed.")
        else:
            self.on = False

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
webinar_type.on


