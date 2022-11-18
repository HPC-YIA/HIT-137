#~~~~~~~Group Info~~~~~~~~~~
# Adriana Pereira Lima      ID: S337632
# George Ibaite Librando    ID: S345658
# Peichun Huang             ID: S341131




import turtle
import random
import math
import os


wn = turtle.Screen()

wn.title('Turtle VS UFO')

wn.bgpic('spacebg4.gif')
wn.addshape('UFO.gif')
wn.addshape('rocket2.gif')
wn.tracer(2)


pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.pendown()
pen.color('purple')

pen1 = turtle.Turtle()
pen1.hideturtle()
pen1.penup()
pen1.pendown()


wait = False

def splash_screen():
    
    wn.update()
    pen.penup()
    pen.goto(-120, 100)
    pen.write('TURTLE', font=('Courier', 55, 'normal'))

    pen.goto(-60, 30)
    pen.write('VS', font=('Courier', 55, 'normal'))

    pen.goto(-80, -50)
    pen.write('UFO', font=('Courier', 55, 'normal'))

    pen.goto((-110, -120))
    pen.write('SPACE BAR - FIRE', font=('Comic Sans Ms', 20, 'normal'))

    pen.goto(-110, -140)
    pen.write('SPEED UP - PRESS W', font=('Comic Sans Ms', 20, 'normal'))

    pen.goto(-110, -160)
    pen.write('SPEED DOWN - PRESS S', font=('Comic Sans Ms', 20, 'normal'))

    pen.goto((-105, -190))
    pen.write('PRESS ENTER TO START', font=('Comic Sans Ms', 15, 'normal'))
    
    pen.goto((-105, -220))
    pen.write('HIT BY ROCKET -50 SCORES', font=('Comic Sans Ms', 13, 'normal'))
    
    pen.goto((-105, -240))
    pen.write('HIT BY UFO -5 SCORES', font=('Comic Sans Ms', 13, 'normal'))
    
    
    pen.goto((-105, -260))
    pen.write('HIT UFO +100 SCORES', font=('Comic Sans Ms', 13, 'normal'))
    
    pen.pendown()

    pen1.penup()
    pen1.shape('triangle')
    pen1.color('yellow')
    pen1.goto(-125, -180)
    pen1.stamp()


splash_screen()
wn.tracer(0)
wn.update()


## create game setting 
class Game():

    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = 'splash'
        self.pen = turtle.Turtle()

    # create the border

    def draw_border(self):
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        self.pen.color('purple')
        self.pen.pensize(2)
        self.pen.speed(0)  # draw the bordor with fastest speed
        for i in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.pendown()

    def draw_player_border(self):
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.goto(-128, 128)
        self.pen.pendown()
        self.pen.color('purple')
        self.pen.pensize(2)
        self.pen.speed(0)
        for i in range(4):
            self.pen.fd(252)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.pendown()

    def show_status(self):
        self.pen.undo()
        self.pen.pendown()
        text = 'Score: %s' % (self.score)
        self.pen.penup()
        self.pen.pencolor('white')
        self.pen.goto(-300, 310)
        self.pen.write(text, font=('Arial', 16, 'normal'))
        self.pen.pendown()
        self.pen.undo()

    def start(self):

        self.state = 'playing'
        os.system('afplay Background.wav&')

    def score_circle(self):
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.goto(-198, 100)
        self.pen.pendown()
        self.pen.pensize(2)
        self.pen.speed(0)
        self.pen.color('purple')
        self.pen.circle(100)

        self.pen.hideturtle()
        self.pen.penup()
        self.pen.goto(198, 100)
        self.pen.pendown()
        self.pen.pensize(2)
        self.pen.speed(0)
        self.pen.color('purple')
        self.pen.circle(100)

        self.pen.hideturtle()
        self.pen.penup()
        self.pen.goto(-198, -295)
        self.pen.pendown()
        self.pen.pensize(2)
        self.pen.speed(0)
        self.pen.color('purple')
        self.pen.circle(100)

        self.pen.hideturtle()
        self.pen.penup()
        self.pen.goto(198, -295)
        self.pen.pendown()
        self.pen.pensize(2)
        self.pen.speed(0)
        self.pen.color('purple')
        self.pen.circle(100)

##player turtle setting
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.goto(0, 0)
        self.shape('turtle')
        self.color('red')
        self.speed = 2

    def jump(self):
        self.goto(0, 0)
        self.setheading(random.randint(0, 360))

    def move(self):
        self.forward(self.speed)
        if self.xcor() > 123 or self.xcor() < -123:
            self.rt(45)
        if self.ycor() > 120 or self.ycor() < -120:
            self.rt(45)

    def turn_left(self):
        self.left(30)

    def turn_right(self):
        self.right(30)

    def go_up(self):
        self.setheading(90)
        self.forward(self.speed)

    def go_down(self):
        self.setheading(-90)
        self.forward(self.speed)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1


#player missile setting
class Missile(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)

        self.penup()
        self.shape('triangle')
        self.color('orange')
        self.shapesize(stretch_wid=0.3, stretch_len=0.5, outline=None)
        self.speed = 40
        self.status = 'ready'
        self.penup()
        self.goto(-900, 900)

    def fire(self):
        if self.status == 'ready':
            os.system('afplay laser.mp3&')
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = 'firing'

    def move(self):

        if self.status == 'ready':
            
            self.hideturtle()

        if self.status == 'firing':
            self.showturtle()
            self.forward(self.speed)

            if self.xcor() > 290 or self.xcor() < -290:
                
                self.hideturtle()
                self.status = 'ready'

            if self.ycor() > 290 or self.xcor() < -290:
                
                self.hideturtle()
                self.status = 'ready'



##create enemy UFO in 4 groups
class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.x = x
        self.y = y
        self.penup()
        self.goto(x, y)
        self.setheading(random.randint(0, 360))
        self.shape('UFO.gif')
        self.speed = 1

    def enemy1_move(self):

        self.forward(self.speed)

        if self.xcor() > -140 or self.xcor() < -250:
            self.goto(random.randint(-240, -135), random.randint(-240, -135))
            self.setheading(random.randint(0, 360))
        if self.ycor() > -140 or self.ycor() < -250:
            self.goto(random.randint(-240, -135), random.randint(-240, -135))
            self.setheading(random.randint(0, 360))

    def enemy2_move(self):

        self.forward(self.speed)

        if self.xcor() > 250 or self.xcor() < 140:
            self.goto(random.randint(135, 240), random.randint(135, 245))
            self.setheading(random.randint(0, 360))
        if self.ycor() > 250 or self.ycor() < 140:
            self.goto(random.randint(135, 240), random.randint(135, 245))
            self.setheading(random.randint(0, 360))

    def enemy3_move(self):

        self.forward(self.speed)

        if self.xcor() > -140 or self.xcor() < -250:
            self.goto(random.randint(-240, -140), random.randint(145, 245))

            self.setheading(random.randint(0, 360))

        if self.ycor() > 250 or self.ycor() < 140:
            self.goto(random.randint(-240, -140), random.randint(145, 245))
            self.setheading(random.randint(0, 360))

    def enemy4_move(self):

        self.forward(self.speed)

        if self.xcor() > 250 or self.xcor() < 130:
            self.goto(random.randint(130, 240), random.randint(-245, -135))

            self.setheading(random.randint(0, 360))
        if self.ycor() > -130 or self.ycor() < -250:
            self.goto(random.randint(130, 240), random.randint(-245, -135))
            self.setheading(random.randint(0, 360))

##create obstacle rockets
class Rocket(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape('rocket2.gif')
        self.speed = 2
        self.goto(random.randint(-250, 170), random.randint(-150, 130))

    def jump(self):
        self.goto(random.randint(-250, 170), random.randint(-150, 130))
        self.setheading(random.randint(0, 360))

    def move(self):
        self.forward(self.speed)
        if self.xcor() > 290 or self.xcor() < -290:
            self.jump()
        if self.ycor() > 150 or self.ycor() < -150:
            self.jump()


# Collision  checking
def isCollision(t1, t2):
    a = t1.xcor() - t2.xcor()
    b = t1.ycor() - t2.ycor()
    distance = math.sqrt((a ** 2) + (b ** 2))

    if distance < 25:
        return True
    else:
        return False

##create game pause function

def pause():
    global wait
    if wait == True:
        wait = False
    else:
        wait = True
        pen.penup()
        pen.goto(-115,20)
        pen.pendown()
        pen.write('Press P to Resume Game', font=('Arial', 20, 'normal'))
 
##create UFO missile       
class ufomissile(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.x=x
        self.y=y
        self.shape ("triangle")
        self.color ('orange')
        self.shapesize (1, 0.1, 1)
        self.setheading(random.randint(0, 90))
        self.penup()
        self.setpos(x, y)
        
        self.speed=5
    
    def move1(self):
        self.forward(self.speed)
        self.setheading(random.randint(0, 90))
        if self.xcor() > 290 or self.xcor() < -290:
            self.goto(-150,-150)
        if self.ycor() > 290 or self.ycor() < -290:
            self.goto(-150,-150)
            
    def move2(self):
        
        self.forward(self.speed)
        self.setheading(random.randint(180,270))
        
        if self.xcor() > 290 or self.xcor() < -290:
            self.goto(160,160)
        if self.ycor() > 290 or self.ycor() < -290:
            self.goto(160,160)
            
    def move3(self):
        self.forward(self.speed)
        self.setheading(random.randint(280,360))
        if self.xcor() > 290 or self.xcor() < -290:
            self.goto(-140,140)
        if self.ycor() > 290 or self.ycor() < -290:
            self.goto(-140,140)

    def move4(self):
            self.forward(self.speed)
            self.setheading(random.randint(90,180))
            if self.xcor() > 290 or self.xcor() < -290:
                self.goto(170,-180)
            if self.ycor() > 290 or self.ycor() < -290:
                self.goto(170,-180)
game = Game()

player = Player()
player.hideturtle()

missile = Missile()
missile.hideturtle()

# create rocket instance
rockets = []
for count in range(4):
    count = Rocket()
    count.hideturtle()
    rockets.append(count)

# create enemy instances
enemies1 = []
for i in range(3):
    i = Enemy(-140, -140)
    enemies1.append(i)

enemies2 = []
for x in range(3):
    x = Enemy(150, 150)
    enemies2.append(x)

enemies3 = []
for j in range(3):
    j = Enemy(-150, 150)
    enemies3.append(j)

enemies4 = []
for a in range(3):
    a = Enemy(180, -190)
    enemies4.append(a)

##create ufo missile instances
ufo_missile1=[]
for b in range(3):
    b=ufomissile(-150,-150)
    ufo_missile1.append(b)
    

ufo_missile2=[]
for x in range(3):
    x=ufomissile(160,160)
    ufo_missile2.append(x)  
    
ufo_missile3=[]
for y in range(3):
    y=ufomissile(-140,140)
    ufo_missile3.append(y)

ufo_missile4=[]
for p in range(3):
    p=ufomissile(170,-180)
    ufo_missile4.append(p)
##main game control

def mainGame():
    game.score_circle()
    game.draw_border()
    game.draw_player_border()
    game.show_status()
    game.start()
    

    while True:
        if not wait:
            
            wn.update()

            pen.clear()
            pen1.clear()

            player.showturtle()
            player.move()
            missile.showturtle()
            missile.move()
            
            for ufomissile in ufo_missile1:
                ufomissile.move1()
                if isCollision(player, ufomissile):
                   
                    game.score -= 5
                    game.show_status()
                
                
            
            for ufomissile in ufo_missile2:
                ufomissile.move2()
                if isCollision(player, ufomissile):
                   
                    game.score -= 5
                    game.show_status()
               
               
            for ufomissile in ufo_missile3:
                ufomissile.move3() 
                if isCollision(player, ufomissile):
                   
                    game.score -= 5
                    game.show_status()
                
                
            for ufomissile in ufo_missile4:
                ufomissile.move4() 
                if isCollision(player, ufomissile):
                   
                    game.score -= 5
                    game.show_status()
                

            for enemy in enemies1:
                enemy.showturtle()
                enemy.enemy1_move()
                
                if isCollision(missile, enemy):
                    enemy.hideturtle()
                    game.score += 100

                    game.show_status()


            for enemy in enemies2:
                enemy.showturtle()
                enemy.enemy2_move()
                if isCollision(missile, enemy):
                    
                    enemy.hideturtle()
                    game.score += 100

                    game.show_status()

            for enemy in enemies3:
                enemy.showturtle()
                enemy.enemy3_move()

                if isCollision(missile, enemy):
                    
                    enemy.hideturtle()
                    game.score += 100
                    game.show_status()

            for enemy in enemies4:
                enemy.showturtle()
                enemy.enemy4_move()

                if isCollision(missile, enemy):
                    
                    enemy.hideturtle()
                    game.score += 100
                    game.show_status()

            for rocket in rockets:
                rocket.showturtle()
                rocket.move()
                if isCollision(player, rocket):
                    rocket.jump()
                    game.score -= 50
                    game.show_status()

            wn.update()
        else: 
            
            wn.update()
       

#keyboard binding 

turtle.onkey(player.turn_left, 'Left')
turtle.onkey(player.turn_right, 'Right')
turtle.onkey(player.go_up, 'Up')
turtle.onkey(player.go_down, 'Down')
turtle.onkey(player.accelerate, 'w')
turtle.onkey(player.decelerate, 's')
turtle.onkey(missile.fire, 'space')
turtle.onkeypress(mainGame, 'Return')
turtle.onkeypress(pause,'p')
turtle.listen()

wn.exitonclick()


