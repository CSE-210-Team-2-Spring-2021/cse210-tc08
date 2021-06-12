from game.actor import Actor
from game import constants
from game.point import Point

class Ball(Actor):
    """ This class is to move the ball actor and to also reset the ball if the floor is hit.
    Stereotype:
        Service Provider
    Attributes:
        cast (dict list) - dictionary of the Actors
        _floor
    """
    pass

    def __init__(self):
        """ The constructor inheriting from parent Actor class.
        Args:
            self - An instance of Ball
        """
        super().__init__()
        self._floor = False

    def reset(self, cast):
        """ Responsible for resetting the Ball on the Paddle with new random direction.
        Args:
            self - an instance of Ball
            cast (dict list) - dictionary of the Actors
        """
        ball = cast["ball"][0] # there's only one in the cast
        
        x = int(constants.MAX_X / 2) # middle of screen left to right
        y = int(constants.MAX_Y - 2) # move starting ball position just above Paddle
        position = Point(x, y)
        velocity = Point(0, 0) 
        ball.set_text("@")
        ball.set_position(position)
        ball.set_velocity(velocity)
        

    def move_ball(self, actor):
        """Moves the given actor to its next position according to its 
        velocity. 
        
        Args:
            actor (Actor): The actor to move.
        """
        # limit the Ball moving on every other "frame"
        frame = True
        if frame == True:
            position = actor.get_position()
            velocity = actor.get_velocity()
            x1 = position.get_x()
            y1 = position.get_y()
            x2 = velocity.get_x()
            y2 = velocity.get_y()
            x = 1 + (x1 + x2 - 1) % (constants.MAX_X - 1)
            y = 1 + (y1 + y2 - 1) % (constants.MAX_Y - 1)
            position = Point(x, y)
            actor.set_position(position)
            frame = False
        else:
            frame = True

    def set_floor(self):
        """Sets floor to True, this will happen when the ball hits the floor

        Args:
            self - An instance of Ball
        """
        self._floor = True
    
    def reset_floor(self):
        """Sets floor to False, this will happen when play continues with start_game_action

        Args:
            self - An instance of Ball
        """
        self._floor = False
    
    def get_floor(self):
        """Returns current value of floor

        Args:
            self -  An instance of Ball
        """
        return self._floor
