from toroidal.main import face_point  # noqa: F401
import pymunk.pygame_util
import pytest

ball_moment = pymunk.moment_for_circle(1, 0, 1)
ball_body = pymunk.Body(1, ball_moment)
# face_point()

ball_moment = pymunk.moment_for_circle(1, 0, 1)
ball_body = pymunk.Body(1, ball_moment)


def test_ball_moves_instant_close():
    ball_body.angle = 3
    assert pytest.approx(face_point(ball_body, 0.5, 2.6), 0.05) == 2.6
    ball_body.angle = -3
    assert pytest.approx(face_point(ball_body, 0.5, -2.6), 0.05) == -2.6


def test_ball_moves_instant_close_overlap():
    ball_body.angle = 3
    assert pytest.approx(face_point(ball_body, 0.5, -2.9), 0.05) == -2.9
