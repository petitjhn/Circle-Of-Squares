import turtle 

square = turtle.Turtle()
square.speed(10)
for i in range(100):
	square.right(25)
	for i in range (1):
		square.forward(100)
		square.right(90)
		square.forward(100)
		square.right(90)
		square.forward(100)
		square.right(90)
		square.forward(100)
