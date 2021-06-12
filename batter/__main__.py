from game import start_game_action
import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.ball import Ball
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.start_game_action import StartGameAction
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen


def main(screen):

    # create the cast {key: tag, value: list}
    cast = {}

    text = Actor()
    text.set_text("")
    text.set_position(Point(1, 0))
    cast["text"] = [text]

    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y - 2)
    position = Point(x, y)
    paddle = Actor()
    paddle.set_text("===========")
    paddle.set_position(position)
    cast["paddle"] = [paddle]

    cast["brick"] = []
    for x in range(5, 75):
        for y in range(2, 6):
            position = Point(x, y)
            brick = Actor()
            brick.set_text("*")
            brick.set_position(position)
            cast["brick"].append(brick)

    cast["floor"] = []
    for x in range(1, constants.MAX_X - 1):
        y = constants.MAX_Y
        position = Point(x, y)
        floor = Actor()
        floor.set_text("_")
        floor.set_position(position)
        cast["floor"].append(floor)

    cast["ceiling"] = []
    for x in range(1, constants.MAX_X - 1):
        y = 0
        position = Point(x, y)
        ceiling = Actor()
        ceiling.set_text("_")
        ceiling.set_position(position)
        cast["ceiling"].append(ceiling)

    cast["wall"] = []
    for y in range(0, constants.MAX_Y):
        x = 0
        position = Point(x, y)
        wall = Actor()
        wall.set_text("|")
        wall.set_position(position)
        cast["wall"].append(wall)
    for y in range(0, constants.MAX_Y):
        x = constants.MAX_X
        position = Point(x, y)
        wall = Actor()
        wall.set_text("|")
        wall.set_position(position)
        cast["wall"].append(wall)

    x = int(constants.MAX_X / 2) # middle of screen left to right
    y = int(constants.MAX_Y - 3) # move starting ball position just above Paddle
    position = Point(x, y)
    velocity = Point(0, 0) # Kyle is a little confused on setting upward velocity. replaced (1,-1) with (1,1)
    ball = Actor()
    ball.set_text("@")
    ball.set_position(position)
    ball.set_velocity(velocity)
    cast["ball"] = [ball]

    # create the script {key: tag, value: list}
    script = {}

    input_service = InputService(screen)
    output_service = OutputService(screen)
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_acition = HandleCollisionsAction()
    start_game_action = StartGameAction()
    draw_actors_action = DrawActorsAction(output_service)
    

    script['pause'] = [start_game_action]
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_acition]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script)
    director.start_game()


Screen.wrapper(main)
