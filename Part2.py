from abc import ABC, abstractmathod, abstractmethod


class DoneError(Exception):
    pass


class Webinar(ABC):
    def __init__(self):
        self.open = False

    def on(self):
        if self.open:
            raise DoneError("Webinar is already opened.")
        else:
            self.open = True

    def off(self):
        if not self.open:
            raise DoneError("Webinar is already closed.")
        else:
            self.open = False

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
webinar_type.open

