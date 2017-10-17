import threading
import time

animations = {
    "asterisk": ["✶", "✷", "✸", "✹", "✺"],
    "black_triangle": ["◢", "◣", "◤", "◥"],
    "break_through": ["☰", "☱", "☳", "☷", "☳", "☱"],
    "circle_building": ["◜", "◠", "◝", "◞", "◡", "◟"],
    "circle_quarter_square": ["◴", "◷", "◶", "◵"],
    "connected_circles": ["⚬", "⚭", "⚮", "⚯", "⚮", "⚭"],
    "curve_integral": ["∮", "∯", "∰", "∯"],
    "dice": ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"],
    "dots_equal": ["≑", "≒", "≑", "≓"],
    "ellipsis": ["․", "‥", "…", "‥"],
    "explosion": ["·", "⁘", "⁛", "⁜"],
    "finger": ["☜", "☝", "☞", "☟"],
    "four_spoked_asterisk": ["✢", "✣", "✤", "✥"],
    "half_filled_circle": ["◐", "◓", "◑", "◓"],
    "floor_and_ceiling": ["⌈", "⌉", "⌋", "⌊"],
    "horizontal_progress":
    [" ", "▏", "▎", "▍", "▌", "▋", "▊", "█", "▊", "▋", "▌", "▍", "▎"],
    "integral": ["∫", "∬", "∭", "⨌", "∭", "∬"],
    "line": ["|", "/", "-", "\\"],
    "quadrant": ["▖", "▘", "▝", "▗"],
    "quadrant_dark": ["▙", "▛", "▜", "▟"],
    "rotating_arrow": ["↑", "↗", "→", "↘", "↓", "↙", "←", "↖"],
    "rotating_ellipsis": ["⋮", "⋰", "⋯", "⋱"],
    "shade": ["░", "▒", "▓", "█", "▓", "▒"],
    "square_cap": ["⊔", "⊏", "⊓", "⊐"],
    "square_in_square": ["◰", "◳", "◲", "◱"],
    "vertical_progress": [
        " ", "▁", "▂", "▃", "▄", "▅", "▆", "▇", "█", "▇", "▆", "▅", "▄", "▃",
        "▂", "▁"
    ],
    "white_triangle": ["◸", "◹", "◿", "◺"],
}


def waitperson(animation, dt=0.1, prefix="", suffix=" "):
    animation = animations[animation]
    length = len(animation)

    def waitperson_decorator(function):
        def decorated_func(*args, **kwargs):
            thread = threading.Thread(target=function)
            thread.start()
            position = 0

            print(prefix + animation[position] + suffix, end="")
            time.sleep(dt)

            while thread.isAlive():
                print("\r" + prefix + animation[position] + suffix, end="")
                time.sleep(dt)
                position = (position + 1) % length

        return decorated_func

    return waitperson_decorator
