import turtle

window = turtle.Screen ()
window.title ("Pong")
window.bgcolor ("white")
window.setup (width = 800, height = 600)
window.tracer = 0

# score
score_1 = 0
score_2 = 0

#platform A
platform_a = turtle.Turtle ()
platform_a.speed (0)
platform_a.shape ("square")
platform_a.color ("black")
platform_a.penup ()
platform_a.goto (-350, 0)
platform_a.shapesize (stretch_wid = 5, stretch_len = 1)

#platform B
platform_b = turtle.Turtle ()
platform_b.speed (0)
platform_b.shape ("square")
platform_b.color ("black")
platform_b.penup ()
platform_b.goto (350, 0)
platform_b.shapesize (stretch_wid = 5, stretch_len = 1)

# ball
ball = turtle.Turtle ()
ball.speed (0)
ball.shape ("circle")
ball.color ("black")
ball.penup ()
ball.goto (0, 0)
ball.xp = 2
ball.yp = -2

# pen
pen = turtle.Turtle ()
pen.speed (0)
pen.color ("black")
pen.penup ()
pen.hideturtle ()
pen.goto  (0, 260)
pen.write ("Player 1: 0   Player 2: 0", align = "center", font = ("Courier", 16, "normal"))

# functions to move
def platform_a_up ():
	y = platform_a.ycor ()
	y += 20
	platform_a.sety (y)

def platform_a_down ():
	y = platform_a.ycor ()
	y -= 20
	platform_a.sety (y)

def platform_b_up ():
	y = platform_b.ycor ()
	y += 20
	platform_b.sety (y)

def platform_b_down ():
	y = platform_b.ycor ()
	y -= 20
	platform_b.sety (y)

# keyboard input
window.listen ()
window.onkeypress (platform_a_up, "w")
window.onkeypress (platform_a_down, "s")
window.onkeypress (platform_b_up, "Up")
window.onkeypress (platform_b_down, "Down")

# main game loop
while True:
	window.update () # udpates the screen every time when loop runs
	
	# move the ball
	ball.setx (ball.xcor () + ball.xp)
	ball.sety (ball.ycor () + ball.yp)

	#setting up borders
	if ball.ycor () > 290:
		ball.sety (290)
		ball.yp *= -1

	if ball.ycor () < -290:
		ball.sety (-290)
		ball.yp *= -1

	if ball.xcor () > 390:
		ball.goto (0, 0)
		ball.xp *= -1
		score_1 += 1
		pen.clear ()
		pen.write ("Player 1: {}   Player 2: {}".format (score_1, score_2), align = "center", font = ("Courier", 16, "normal"))

	if ball.xcor () < -390:
		ball.goto (0, 0)
		ball.xp *= -1
		score_2 += 1
		pen.clear ()
		pen.write ("Player 1: {}   Player 2: {}".format (score_1, score_2), align = "center", font = ("Courier", 16, "normal"))

	#collison 
	if (ball.xcor () > 340 and ball.xcor () < 350) and (ball.ycor () < platform_b.ycor () + 40 and ball.ycor () > platform_b.ycor () - 40):
		ball.setx (340)
		ball.xp *= -1

	if (ball.xcor () < -340 and ball.xcor () > -350) and (ball.ycor () < platform_a.ycor () + 40 and ball.ycor () > platform_a.ycor () - 40):
		ball.setx (-340)
		ball.xp *= -1




