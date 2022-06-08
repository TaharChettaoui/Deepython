
from dataclasses import dataclass
from typing import Callable
import functools


@dataclass #(slots=True) for python > 3.10
class Person:
    name: str
    surname: str
    adress: str


class Dog:
    def __init__(self, name, owner: Person, breed):
        self._name = name
        self.owner = owner
        self.__breed = breed

    @staticmethod
    def bark():
        print("Wof Wof!")


class Robot:
    _robots = []
    __slots__ = "id", "_name", "owner","year", "color"
    
    def __init__(self, id, name, owner: Person, year, color="Black"):
        try:
            assert id >= 0
            self.id = id
            self.owner = owner
            self._name = name
            self.year = year
            self.color = color
            Robot._robots.append(self)
            
        except AssertionError:
            print("The robot ID must be greater or equal to 0!")
        
    def _get_name(self):
        return self._name
    
    def _set_name(self, name):
        self._name = name
    
    @classmethod
    def constructed_robots(cls):
        return cls._robots
    
    name = property(_get_name, _set_name)


class RobotDog(Robot, Dog):
    def __init__(self, id, name, owner: Person, year, color="Black", breed="Unknown"):
        Robot.__init__(self, id, name, owner, year, color) # super()__init__()
        Dog.__init__(self, name, owner, breed) # super(Robot, self)__init__()


if __name__ == "__main__":
    # create persons
    person_0 = Person("Thomas", "Müller", "76131 Karlsruhe")

    # create dogs
    def make_dog(c: str) -> Callable[[str], Dog]:
        return lambda a,b: Dog(a, b, c)

    make_german_shepherd = make_dog("german_shepherd") # approach 1
    make_french_bulldog = functools.partial(Dog, breed="french_bulldog") # approach 2
    dog_0 = make_german_shepherd("Flash", person_0)
    dog_1 = make_french_bulldog("Iggy", person_0)
    print(dog_1.__dict__)

    # create robots (add "_" for large numbers to increase readability)
    Robot.constructed_robots = classmethod(Robot.constructed_robots)
    robot_0 = Robot(20_120_000, "Spot", person_0, 1995, "Green")
    robot_1 = Robot(10_100_000, "Tops", person_0, 1987, "Red")
    robot_2 = Robot(20_130_000, "Robocop", person_0, 1987, "Grey")
    robot_3 = RobotDog(10_250_000, "Spip", person_0, 1990, "Black", "French bulldog" )

    _, *desc, color = robot_0.__slots__
    print("Some of Robot 0 properties: " + str(desc))

    # Lambda function
    newer_robot = lambda x, y: x if (x.year > y.year) else y
    print("Newest robot is : " + newer_robot(robot_0, robot_1).name)

    # Zip(), enumerate() and List comprehension
    # I learned about "zip" when I worked with Haskell. I tend to forget about this awesome funtion!
    robots = Robot.constructed_robots()
    num_robots = len(Robot.constructed_robots())
    print([(num, robot.name) for num, robot in enumerate(robots)])
    print([(num, robot.name) for num, robot in zip(range(0, num_robots, 1), robots)])

    # Map(), any() and all()
    def paint_robot(rbt: Robot, color):
        rbt.color = color
        return rbt

    robots = Robot.constructed_robots()
    is_red_painted = [rbt.color == "Red" for rbt in robots]
    print("At least one robot is painted in red: " + str(any(is_red_painted)))
    print("All robots are painted in red: " + str(all(is_red_painted)) + "\nLets paint them all in red!\n")


    list(map(paint_robot, robots, ["Red"]*len(robots)))
    is_red_painted = [rbt.color == "Red" for rbt in robots]
    print("At least one robot is painted in red: " + str(any(is_red_painted)))
    print("All robots are painted in red: " + str(all(is_red_painted)))


    # Multiple inheritance, name mangling and static methods
    is_robot = isinstance(robot_3, Robot)
    print(is_robot)

    is_robot_dog = isinstance(robot_3, RobotDog)
    if (is_robot_dog):
        robot_3.bark() # RobotDog.bark() also works ==> static method
