import turtle

#screen 생성
s = turtle.getscreen()

#Turtle 변수 지정
t = turtle.Turtle()

t.shape("turtle")

#장애물 만들기
for i in range(4):
    t.fd(100)
    t.rt(90)


#도착점 만들기
t.penup()
t.goto(300,100)
t.pendown()
t.circle(60)
t.penup()

#시작점 만들기
t.goto(-300,-300)
t.pendown()
t.circle(60)
t.penup
t.setheading(40)
t.fd(750)

