from game.action import Action

class DrawActorsAction(Action):
    """THis class is responsible for drawing all of the Actors on the screen

    Stereotype:
        Service Provider

    Attributes:
        output_service - an Instance of OutputService
    """

    def __init__(self, output_service):
        """The Class constructor

        Args:
            self - An instance of DrawActorsAction
            output_service - An instance of OutputService
        """

        self._output_service = output_service

    def execute(self, cast):
        """Draws the actors on the screen

        Args:
            self - An instance of DrawActorsAction
            cast - A dictionary of Actor objects
        """
        self._output_service.clear_screen()
        for group in cast.values():
            self._output_service.draw_actors(group)
        self._output_service.flush_buffer()
