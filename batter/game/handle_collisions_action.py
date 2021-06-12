import random
from game import constants
from game.action import Action
from game.point import Point


class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.

    Stereotype:
        Controller

    Attributes:
        _check - bool to make sure it checks collisions only on movement frames
    """
    def __init__(self):
        """ Class Constructor
        
        Args:
            self - AN instance of HandleCOllisionAction
        """
        self._check = True

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        
        if self._check:
            wall = cast["wall"]
            floor = cast["floor"]
            ceiling = cast["ceiling"]
            paddle = cast["paddle"]
            ball = cast["ball"][0]
            bricks = cast["brick"]
            speed_level = 1
            speed_list = [-speed_level, speed_level]
            for i, brick in enumerate(bricks):
                if ball.get_position().equals(brick.get_position()):
                    bricks.pop(i)
                    x = random.choice(speed_list)
                    old_y = ball.get_velocity().get_y()

                    if old_y > 0:
                        y = random.randint(-speed_level, -1)
                    else:
                        y = random.randint(1, speed_level)

                    velocity = Point(x, y)
                    ball.set_velocity(velocity)
                    
                    self._check = False
                    return

            for unit in wall:
                if ball.get_position().equals(unit.get_position()):
                    old_x = ball.get_velocity().get_x()
                    #if old_x > 0:
                    #    x = random.randint(-speed_level, -1)
                    #else:
                    #    x = random.randint(1, speed_level)
                    x = -old_x
                    y = random.choice(speed_list)
                    velocity = Point(x, y)

                    ball.set_velocity(velocity)

                    self._check = False
                    return

            for unit in floor:
                if ball.get_position().equals(unit.get_position()):
                    ball.set_floor()

                    self._check = False
                    return

            for unit in ceiling:
                if ball.get_position().equals(unit.get_position()):
                    x = random.randint(-speed_level, speed_level)
                    y = random.randint(1, speed_level)
                    velocity = Point(x, y)
                    ball.set_velocity(velocity)

                    self._check = False
                    return

            for pad in paddle:
                if ball.get_position().equals(pad.get_position()):
                    x = random.choice(speed_list)
                    y = random.randint(-speed_level, -1)
                    velocity = Point(x, y)
                    ball.set_velocity(velocity)

                    self._check = False
                    return
            
            self._check = False
        
        else:
            self._check = True