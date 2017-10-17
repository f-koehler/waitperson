import time
from waitperson import waitperson


def test_animation(animation):
    @waitperson(animation, prefix="  ", suffix=" " + animation + " ")
    def sleep():
        time.sleep(2)

    sleep()
    print()


test_animation("asterisk")
test_animation("black_triangle")
test_animation("break_through")
test_animation("circle_building")
test_animation("circle_quarter_square")
test_animation("connected_circles")
test_animation("curve_integral")
test_animation("dice")
test_animation("dots_equal")
test_animation("ellipsis")
test_animation("explosion")
test_animation("finger")
test_animation("floor_and_ceiling")
test_animation("horizontal_progress")
test_animation("integral")
test_animation("four_spoked_asterisk")
test_animation("half_filled_circle")
test_animation("line")
test_animation("quadrant")
test_animation("quadrant_dark")
test_animation("rotating_arrow")
test_animation("rotating_ellipsis")
test_animation("shade")
test_animation("square_cap")
test_animation("square_in_square")
test_animation("vertical_progress")
test_animation("white_triangle")
