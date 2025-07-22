import turtle
import math
import time
import random

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

#목표 지점 도달 확인 함수
def is_arrived(t, target_x, target_y, tolerance=100):
    """
    target_x, target_y: 목표 좌표
    tolerance: 허용 오차 (픽셀)
    """
    x, y = t.position()
    return math.dist([x, y], [target_x, target_y]) <= tolerance


# 거북이 충돌 감지 함수
def is_collided_with_obstacle(t, obs_x1, obs_y1, obs_x2, obs_y2):
    """
    obs_x1, obs_y1: 사각형 왼쪽 아래 꼭짓점
    obs_x2, obs_y2: 사각형 오른쪽 위 꼭짓점
    """
    x, y = t.position()
    return (obs_x1 <= x <= obs_x2) and (obs_y1 <= y <= obs_y2)
    

# 장애물 회피 함수 구현
def avoid_obstacle(t, obs_x1, obs_y1, obs_x2, obs_y2):
    print("장애물 감지! 우회 시작...")
    t.backward(30)
    # 무작위 각도: 90도~180도 사이 랜덤 회전 (반대 방향으로 확실히 틀기)
    turn_angle = random.randint(90, 180)
    t.right(turn_angle)
    
    # 회피 이동 거리
    moved_distance = 0
    while is_collided_with_obstacle(t, obs_x1, obs_y1, obs_x2, obs_y2):
        t.forward(10)
        moved_distance += 10
        time.sleep(0.02)
        # 안전장치: 너무 오래 회피하면 탈출 시도
        if moved_distance > 300:
            break
    print("장애물 벗어남!")
    
#메인 이동 루프: 시작점에서 종점까지 이동하며 회피
    
#목표 좌표와 장애물 좌표
goal_x, goal_y = 300, 100
obs_x1, obs_y1 = 0, -100
obs_x2, obs_y2 = 100, 0

#시작 각도
t.setheading(35)

while not is_arrived(t, goal_x, goal_y):
    t.forward(10)
    if is_collided_with_obstacle(t, obs_x1, obs_y1, obs_x2, obs_y2):
        avoid_obstacle(t, obs_x1, obs_y1, obs_x2, obs_y2)
        # 장애물 벗어나면 목표 방향 재설정
        x, y = t.position()
        dx = goal_x - x
        dy = goal_y - y
        angle = math.degrees(math.atan2(dy, dx))
        t.setheading(angle)
    time.sleep(0.05)

print("목표 지점에 도착했습니다!")
    
    
# 도착 여부 출력
if is_arrived(t, 300, 100):
    print("목표 지점에 도착했습니다!")
else:
    print("아직 목표 지점에 도달하지 못했습니다.")
    
# 장애물 충돌 여부 출력
if is_collided_with_obstacle(t, 0, -100, 100, 0):
    print("장애물에 충돌했습니다!")
else:
    print("장애물 피하기 성공!")
    

#시작점에서 종점까지 장애물 피하기
'''
t.setheading(40)
t.fd(330)
t.setheading(90)
t.fd(70)
t.setheading(0)
t.fd(150)
t.setheading(33)
t.fd(230)
'''

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


    
