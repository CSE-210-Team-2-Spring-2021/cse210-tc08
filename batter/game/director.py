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
        self._first_run = True

    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        self._keep_playing()
        while True:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")

            if self._cast['ball'][0].get_floor():
                self._keep_playing()
            elif self._cast['brick'] == []:
                self._keep_playing()

            sleep(constants.FRAME_LENGTH)

    def _cue_action(self, tag):
        """Executes the actions with the given tag.

        Args:
            tag (string): The given tag.
        """
        for action in self._script[tag]:
            action.execute(self._cast)

    def _keep_playing(self):
        """Asks the user if they would like to play again and restarts the game"""
        actor = self._cast['text'][0]
        if self._first_run:
            actor.set_text("Press Spacebar to start game, Press Esc to quit:")
            self._first_run = False
        else:
            actor.set_text("You Lost! Press Spacebar to try again, Press Esc to quit:")
        self._cue_action('output')
        self._cue_action("pause")
        actor.set_text("")
        self._cue_action('output')
