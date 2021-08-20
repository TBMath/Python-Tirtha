from abc import ABC, abstractmethod
class Paper(ABC):
    @abstractmethod
    def cross(self):
        pass
class Straight:
    def cross(self): 
        print("Straight line.")
class NonStraight:
    def cross(self): 
        print("Slanted line.")
def type_line(line_object):
    line_object.cross()
straight = Straight()
non_straight = NonStraight()
type_line(straight)