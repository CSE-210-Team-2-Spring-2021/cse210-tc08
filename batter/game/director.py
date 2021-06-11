from time import sleep
from game import constants


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.

    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """

    def __init__(self, cast, script):
        """The class constructor.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        self._cast = cast
        self._script = script

    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        while True:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")
            sleep(constants.FRAME_LENGTH)

    def _cue_action(self, tag):
        """Executes the actions with the given tag.

        Args:
            tag (string): The given tag.
        """
        for action in self._script[tag]:
            action.execute(self._cast)

    def _keep_playing(self, cast):
        """Asks the user if they would like to play again and restarts the game"""
        if self.handle_collisions.execute(self._cast.floor):
            for actor in self._cast["text"][0]:
                actor.get_text("Too play again, press the \"Space\" key.")
                self._cue_action("pause")
                actor.set_text("")
