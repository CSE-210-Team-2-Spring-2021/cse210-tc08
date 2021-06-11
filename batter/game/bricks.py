from game import constants
from game.point import Point

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

    def destroyBricks(self,bricks,ball_position):
        """Deletes the brick where the ball hits (The ball is in the same place as a brick )
        
        Args:
            bricks (list):          The list with all the bricks
            ball_position(Point):   The balll's position in 2d space.
        """ 
        if bricks.count(ball_position) == 1:      #Validates if the ball is in the same place as a brick
            bricks.remove(ball_position)        #If is true, it's going to remove a brick in the ball_position. The remove() method will remove only the first occurrence of thing.
        return bricks

    def generateBricks(self,cast):
        """Generate a new list of items and append it into "cast"
        
        Args:
            bricks (list):          The list with all the bricks
            ball_position(Point):   The balll's position in 2d space.
        """ 
        if len(cast["brick"]) == 0:             #Check if the Brick's list it empty
            cast["brick"] = []
            for x in range(5, 75):
                for y in range(2, 6):
                    position = Point(x, y)
                    self.set_text("*")
                    self.set_position(position)
                    cast["brick"].append(self)
        return cast
