import turtle

speed = float(input('Please Enter the speed you want !!! '))

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800 , height=600)
wn.tracer(0)

# Paddle A
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape('square')
pad_a.color('white')
pad_a.penup()
pad_a.goto(-380, 0 )
pad_a.shapesize(stretch_wid=5 , stretch_len=1)



# Paddle B
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape('square')
pad_b.color('white')
pad_b.penup()
pad_b.goto(370 , 0)
pad_b.shapesize(stretch_wid=5 , stretch_len=1)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0 , 0 )
ball.px = speed
ball.py = -0.1

#Functoins

def pad_a_up():
	y = pad_a.ycor()
	y = y + 20
	pad_a.sety(y)

def pad_a_down():
	y = pad_a.ycor()
	y = y - 20
	pad_a.sety(y)


def pad_b_up():
	y = pad_b.ycor()
	y = y + 20
	pad_b.sety(y)

def pad_b_down():
	y = pad_b.ycor()
	y = y - 20
	pad_b.sety(y)


#Listinging the keys and moving (running the functions)

wn.listen()
wn.onkeypress(pad_a_up ,  'w')
wn.onkeypress(pad_a_down , 's')
wn.onkeypress(pad_b_up , 'Up')
wn.onkeypress(pad_b_down , 'Down')


#Main Game process
while True:
	wn.update()


	#Move the Ball
	ball.sety(ball.ycor() + ball.py)
	ball.setx(ball.xcor() + ball.px)

	#Border Check
	if ball.ycor() > 290 :
		#Bounce the ball
		ball.sety(290)
		ball.py = ball.py * -1
	elif ball.ycor() < -280 :
		#Bounce the ball
		ball.sety(-280)
		ball.py = ball.py * -1
	elif ball.xcor() > 390:
		#Go to The middle of the screen
		ball.setx(0)
		ball.sety(0)
		ball.px = ball.px * -1
	elif ball.xcor() < -390:
		ball.setx(0)
		ball.sety(0)
		ball.px = ball.px * -1


	#Pad and Ball Collisions
	if ball.xcor() > 340 and ball.xcor < 350:
		if ball.ycor() < pad_b.ycor() + 2.5:
			if ball.ycor() > pad_b.ycor() - 2.5:
				ball.px *= -1