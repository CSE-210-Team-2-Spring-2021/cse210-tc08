from game import constants
from game.point import Point
from game.actor import Actor

class Bricks(Actor):
    """The responsibility of Bricks class is to renew and destroy them.

    Stereotype:
        Structurer, Information Holder

    Attributes:
        _bricks (List): The list of bricks
    """
    def __init__(self):
        """The class Constructor

        Args:
            self - An instance of Bricks
        
        """
        super().__init__()

    def destroy_bricks(self,brick_position,cast):
        """Deletes the brick where the ball hits (The ball is in the same place as a brick )
        
        Args:
            brick_position(Point):   The ball's position in 2d space.
            cast (dict):             {key: tag, value: list}.
        """ 
        bricks = cast["brick"]
        bricks.remove(brick_position)         #It's going to remove a brick in the ball's position. The remove() method will remove only the first occurrence.
        return cast

    def generate_bricks(self,cast):
        """Generate a new list of items and append it into "cast"
        
        Args:
            cast (dict):            {key: tag, value: list}.
        """ 
        cast['brick'] = []
        
        for x in range(5, 75):
            for y in range(2, 6):
                position = Point(x, y)
                brick = Actor()
                brick.set_text("*")
                brick.set_position(position)
                cast["brick"].append(brick)
