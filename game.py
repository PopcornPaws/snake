import curses
import time
from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
from random import randint
from .snake import Snake


ESCAPE = 27
ROWS = 25
COLUMNS = 47
stdscr = curses.initscr()

def main(stdscr):
	# Initialize snake and food
	snake = Snake([COLUMNS//2, ROWS//2], [1, 0])
	# Draw new curses window
	win = curses.newwin(ROWS, COLUMNS)
	curses.noecho()
	curses.cbreak()
	win.keypad(True)
	curses.curs_set(False)
	# Initialize color pairs
	curses.start_color()
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_GREEN)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_RED, curses.COLOR_CYAN)
	# Display welcome screen and wait for user input
	win.clear()
	win.border()
	win.addstr(ROWS//2, COLUMNS//2 - 10, "Press any key to start!", curses.color_pair(3))
	win.refresh()
	q = win.getch()
	win.nodelay(True)

	# food has been eaten so regenerate at first run
	regenerate_food = True
	while True:
		# start with checking whether food has to be regenerated
		if regenerate_food:
			food_x = randint(1, COLUMNS - 2) 
			food_y = randint(1, ROWS - 2) 
			regenerate_food = False
		# draw snake and food
		win.clear()
		win.border()
		snake.draw(win)
		win.addch(food_y, food_x, '*', curses.color_pair(2))
		key = win.getch()
		# move snake based on user input
		if key == ESCAPE or key == ord('q'):
			break
		elif key == curses.KEY_UP:
			snake.move(-1)
		elif key == curses.KEY_DOWN:
			snake.move(1)
		elif key == curses.KEY_LEFT:
			snake.move(-2)
		elif key == curses.KEY_RIGHT:
			snake.move(2)
		else:
			snake.move(0)
		# check if the snake crashed into wall or itself
		if snake.check_if_crashed(ROWS, COLUMNS):
			win.addstr(ROWS//2, COLUMNS//2, "You lost!", curses.color_pair(3))
			time.sleep(2)
			break
		# check if food was eaten
		if snake.head_pos()[0] == food_x and snake.head_pos()[1] == food_y:
			snake.increase_length()
			regenerate_food = True
		# refresh window
		win.refresh()
		time.sleep(.2)

	curses.nocbreak()
	stdscr.keypad(False)
	curses.echo()
	curses.endwin()

if __name__ == '__main__':
	curses.wrapper(main)
