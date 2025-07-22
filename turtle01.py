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


'''

거리 계산 함수

시작점이 (x1, y1) / 종점이 (x2, y2)라 하고, 직선 거리를 x3라고 하면

(x3)^2 = (x2 - x1)^2 + (y2 - y1)^2

x3 = √(x2-x1)^2 + (y2 - y1)^2

x3 = √(300 - -300)^2 + (100 - -250)^2

x3 = √(600)^2 + (350)^2

x3 = √(360000)+(122550)

x3 = √482500 = 694.6 (직선거리)

실제 이동거리
t.fd(330) + t.fd(70) + t.fd(150) + t.fd(230)
= t.fd(780)


'''
