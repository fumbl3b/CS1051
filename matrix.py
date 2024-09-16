import curses
import random
import time
import string

def matrix_stream(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Don't wait for user input
    stdscr.timeout(50)  # Refresh every 50 milliseconds

    # Get the screen height and width
    height, width = stdscr.getmaxyx()

    # Initialize a list to store the position and delay for each column
    columns = [{'y': random.randint(0, height - 1), 'delay': random.randint(1, 10), 'trail': []} for _ in range(width)]
    tick_count = 0

    while True:
        # Re-fetch screen dimensions in case the terminal was resized
        height, width = stdscr.getmaxyx()

        stdscr.clear()

        for i, column in enumerate(columns):
            # Ensure column index is within current terminal width
            if i >= width:
                continue

            if tick_count % column['delay'] == 0:
                # Move the column position down
                if column['y'] < height - 1:
                    column['y'] += 1

                # Randomly choose a character from the set of alphanumeric characters and symbols
                char = random.choice(string.ascii_letters + string.digits + string.punctuation)

                # Add the character and its position to the trail list
                column['trail'].insert(0, {'char': char, 'y': column['y']})

                # Limit the length of the trail
                if len(column['trail']) > 10:  # You can adjust the trail length here
                    column['trail'].pop()

                # Draw the current character in bright green if within bounds
                if 0 <= column['y'] < height:
                    stdscr.addstr(column['y'], i, char, curses.color_pair(1))

            # Draw the trailing characters with decreasing brightness
            for j, trail_char in enumerate(column['trail'][1:], start=1):
                if 0 <= trail_char['y'] < height:
                    stdscr.addstr(trail_char['y'], i, trail_char['char'], curses.color_pair(min(4, j)))

            # If the column reaches the bottom, reset to top
            if column['y'] >= height:
                column['y'] = 0
                column['trail'].clear()

        stdscr.refresh()

        # Break the loop if a key is pressed
        if stdscr.getch() != -1:
            break

        tick_count += 1
        time.sleep(0.05)

def main():
    curses.wrapper(init_curses)

def init_curses(stdscr):
    curses.start_color()
    # Initialize color pairs for different brightness levels
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Bright green
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Slightly dimmer
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Even dimmer
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Dim green

    matrix_stream(stdscr)

if __name__ == "__main__":
    main()
