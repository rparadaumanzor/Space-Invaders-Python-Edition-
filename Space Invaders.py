#SPACE INVADERS PROJECT
import math
import turtle
import random
import os

#Screen Setup
window = turtle.Screen()
window.bgcolor('black')
window.title('Space Invaders')
#window.bgpic('source.gif')

#Registering Shapes
#turtle.register_shape("(Fill in the blank).gif")

#Creating Border
border = turtle.Turtle()
border.speed(0)
border.color('white')
border.pensize(3)
border.penup()
border.setpos(-300, -300)
border.pendown()

for side in range(4):
    border.forward(600)
    border.left(90)

border.hideturtle()

#Set Score
score = 0
#Creating Score
scoreSet = turtle.Turtle()
scoreSet.speed(0)
scoreSet.color('white')
scoreSet.penup()
scoreSet.setpos(-290, 280)
scoreSetString = "Score: %s" %score 
scoreSet.write(scoreSetString, False, align='left', font=('Arial', 14, "normal"))
scoreSet.hideturtle()

#Creating Player
player = turtle.Turtle()
player.color('blue')
player.shape('triangle')
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#Creating Player Bullet
bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

#Declaring Bullet state (ready and fire)
bulletstate = 'ready'

#Moving the player left/right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

#Firing bullets
def fire_bullet():
    #declare bulletstate as global if needs change
    global bulletstate
    
    if bulletstate == 'ready':
        bulletstate = 'fire'
        #moving bullet above player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

#Testing collision between bullet and enemy
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2) + math.pow(t1.ycor() - t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

    
#Keyboard Bindings
turtle.listen()
turtle.onkey(move_left, 'Left')
turtle.onkey(move_right, 'Right')
turtle.onkey(fire_bullet, 'space')




#Creating Enemy
#Number of Enemies
numOfEnemies = int(input("Set Number of Enemies: "))
#Empty List of Enemies
enemies = []

#Add enemies to list
for i in range(numOfEnemies):
    #creating enemies
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color('red')
    enemy.shape('circle')
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2




#MAIN GAME LOOP
while True:

    for enemy in enemies:
        
        #Moving enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #Moving enemy forward and back
        if enemy.xcor() > 280:
            #Moves All Enemies Down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Change enemy direction
            enemyspeed *= -1

        if enemy.xcor() < -280:
            #Moves All Enemies Down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Change enemy direction
            enemyspeed *= -1

        #Collision Checks
        if isCollision(bullet, enemy):
            #reset bullet
            bullet.hideturtle()
            bulletstate = 'ready'
            bullet.setpos(0, -400)

            #reset enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)

            #Update Score
            score += 10
            scoreSetString = "Score: %s" %score
            scoreSet.clear()
            scoreSet.write(scoreSetString, False, align='left', font=('Arial', 14, "normal"))

        if isCollision(player, enemy):
            player.hideturtle()
            print('Game Over')
            break

    #Move bullet
    if bulletstate == 'fire':
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #Border Checking for Bullet
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = 'ready'
