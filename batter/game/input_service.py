import sys
from game.point import Point
from asciimatics.event import KeyboardEvent


class InputService:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
        _keys (list): Points for up, dn, lt, rt.
    """

    def __init__(self, screen):
        """The class constructor."""
        self._screen = screen
        self._keys = {}
        self._keys[-205] = Point(1, 0)  # ->
        self._keys[-203] = Point(-1, 0)  # <-
        self._keys[97] = Point(-1, 0)  # a
        self._keys[100] = Point(1, 0)  # d
        self._keys[32] = 'Space'  # Space

    def get_direction(self):
        """Gets the selected direction for the given player.

        Returns:
            Point: The selected direction.
        """
        direction = Point(0, 0)
        event = self._screen.get_event()
        if isinstance(event, KeyboardEvent):
            if event.key_code == -1:
                sys.exit()
            # elif event.key_code == 32: #This will be modified when we figure out 'space' to start game
            direction = self._keys.get(event.key_code, Point(0, 0))
        return direction

    def space_pressed(self):
        """Checks if space was pressed

        Returns:
            True if space was pressed.
        """
        event = self._screen.get_event()
        if isinstance(event, KeyboardEvent):
            if event.key_code == -1:
                sys.exit()
            elif event.key_code == 32:  # Spacebar
                return True
            else:
                return False
