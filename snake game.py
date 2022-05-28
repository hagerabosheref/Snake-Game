import turtle, os
import random
#############
#screen
sc=turtle.Screen()
sc.title("Snake Game")
sc.setup(700,700)

sc.bgcolor("#000428")
sc.bgpic("snakegamepic.png")


def setbackground(): # to set background
    sc.bgpic("1.png")
    #############
    #head 
    head=turtle.Turtle()
    sc.addshape(os.path.expanduser("~/Desktop/Snake Game/snake.gif"))
    head.shape(os.path.expanduser("~/Desktop/Snake Game/snake.gif"))
    head.speed(0) 
    head.pu()

    #############
    #food
    food=turtle.Turtle("circle")
    sc.addshape(os.path.expanduser("~/Desktop/Snake Game/frog.gif"))
    food.shape(os.path.expanduser("~/Desktop/Snake Game/frog.gif"))
    food.pu()
    food.goto(0,100)
    food.speed(0)

    #############
    #score
    score=turtle.Turtle("square")
    score.speed(0)
    score.color("#000428")
    score.penup()
    score.setpos(-200,-280)
    xscoreclone=-140
    scorebar=[]
    for i in range(20):
        scoreclone=score.clone()
        scorebar.append(scoreclone)


    count=0 # counter for score 

    #############
    #update screen
    while True:
        sc.update()

        #############
        #functions
        def up():
            ycurrent=head.ycor()
            head.sety(ycurrent+20)
        def down():
            ycurrent=head.ycor()
            head.sety(ycurrent-20)    
        def right():
            head.fd(20) 
        def left():
            head.bk(20)    
        
        #############
        #events
        sc.listen()
        sc.onkey(up,"Up")
        sc.onkey(down,"Down")
        sc.onkey(right,"Right")
        sc.onkey(left,"Left")

        #############
        #conditions
        
        if (head.distance(food)<=60):     #get food
            xfood=random.randint(-260,260)
            yfood=random.randint(-260,260)
            food.goto(xfood,yfood) 
            count+=1   
            scorebar[count-1].goto(xscoreclone+(count*10),-280)
            scorebar[count-1].color("#8E0E00")

        if(head.xcor()>=280 or head.xcor()<=-280 or head.ycor()>=250 or head.ycor()<=-250):
            sc.clear()
            sc.bgpic("gameover.png")
            break;

        if(count==20):  #to end game 
            sc.clear()
            sc.bgpic("Congratulation.png")
            break;
           
turtle.ontimer(setbackground,3000) 

turtle.done()