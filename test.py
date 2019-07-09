from .snake import Snake

def main():
	snake = Snake([3, 2], [1, 0])
	snake.increase_length()
	snake.increase_length()
	print("(x, y)\t(vx, vy)")
	for i in range(3):
		print(str(snake.pos(i)) + "\t" + str(snake.vel(i)))
	snake.move(0)
	for i in range(3):
		print(str(snake.pos(i)) + "\t" + str(snake.vel(i)))
	snake.move(-1)
	for i in range(3):
		print(str(snake.pos(i)) + "\t" + str(snake.vel(i)))
	snake.move(0)
	for i in range(3):
		print(str(snake.pos(i)) + "\t" + str(snake.vel(i)))
	

if __name__ == '__main__':
	main()
