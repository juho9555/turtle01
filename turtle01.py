import turtle

#screen 생성
s = turtle.getscreen()

#Turtle 변수 지정
t = turtle.Turtle()

t.shape("turtle")
t.speed(5)

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
t.penup()
t.goto(-300,-250)
t.pendown()

#시작점에서 종점까지 장애물 피하기
t.setheading(40)
t.fd(330)
t.setheading(90)
t.fd(70)
t.setheading(0)
t.fd(150)
t.setheading(33)
t.fd(230)


