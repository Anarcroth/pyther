#!bin/python3

import time
import curses
from curses import wrapper

def main(stdscr):
    # Make stdscr.getch non-blocking
    stdscr.nodelay(True)
    stdscr.clear()
    width = 4
    count = 0
    direction = 1
    while True:
        c = stdscr.getch()
        # Clear out anything else the user has typed in
        curses.flushinp()
        stdscr.clear()
        # If the user presses p, increase the width of the springy bar
        if c == ord('p'):
            width += 1
        # Draw a springy bar
        stdscr.addstr("#" * count)
        count += direction
        if count == width:
            direction = -1
        elif count == 0:
            direction = 1
        # Wait 1/10 of a second. Read below to learn about how to avoid
        # problems with using time.sleep with getch!
        time.sleep(0.1)

# wrapper is a function that does all of the setup and teardown, and makes sure
# your program cleans up properly if it errors!
wrapper(main)
