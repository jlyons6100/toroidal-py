import pygame as pg
import pymunk.pygame_util
import math


RES = WIDTH, HEIGHT = 800, 800
FPS = 5


def init_game():
    pg.init()
    surface = pg.display.set_mode(RES)
    clock = pg.time.Clock()
    draw_options = pymunk.pygame_util.DrawOptions(surface)

    space = pymunk.Space()
    # space.gravity = 0, 1
    return surface, space, clock, draw_options


def create_ball(mass, radius, position):
    ball_mass, ball_radius = mass, radius
    ball_moment = pymunk.moment_for_circle(ball_mass, 0, ball_radius)
    ball_body = pymunk.Body(ball_mass, ball_moment)
    ball_body.position = position
    ball_shape = pymunk.Circle(ball_body, ball_radius)
    space.add(ball_body, ball_shape)
    return ball_body


def get_radians(point, other_point):
    x, y = point[0] - other_point[0], point[1] - other_point[1]
    return math.atan2(y, x)


def face_point(body, max_change, radians):
    print(body.angle)
    if radians == body.angle:
        return body.angle
    # close to overlap between 3.14 and -3.14
    if abs(body.angle) + abs(radians) > math.pi and \
       ((body.angle < 0 or radians < 0) and
           not (body.angle < 0 and radians < 0)):
        # overlap difference or normal difference less than max change
        if math.pi*2 - (abs(body.angle) + abs(radians)) < max_change or \
           abs(radians - body.angle) < max_change:
            return radians
        # move towards left side of x axis
        elif body.angle < 0:
            return body.angle - max_change
        else:
            return body.angle + max_change
    if abs(radians - body.angle) < max_change:
        return radians
    # move towards x axis
    if radians > body.angle:
        return body.angle + max_change
    else:
        return body.angle - max_change


if __name__ == "__main__":
    surface, space, clock, draw_options = init_game()
    ball_body = create_ball(1, 60, (WIDTH // 2, HEIGHT // 2))
    ball_body.angle = 2.9
    while True:
        surface.fill(pg.Color('black'))
        for i in pg.event.get():
            if i.type == pg.QUIT:
                exit()

        if pg.mouse.get_pressed()[0]:
            ball_body.angle = face_point(
                ball_body,
                0.5,
                get_radians(pg.mouse.get_pos(), ball_body.position)
                )
        space.step(1 / FPS)
        space.debug_draw(draw_options)

        pg.display.flip()
        clock.tick(FPS)
