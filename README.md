# Turtle01
### 무인이동체 알고리즘 수업

```
# Turtle 기본 틀 생성 / 시작점과 종점 생성
import turtle

s = turtle.getscreen()

# Turtle 변수 지정
t = turtle.Turtle()

t.shape("turtle")
t.penup()
t.goto(300,100)
t.pendown()
t.circle(60)
t.penup()
t.goto(-300,-300)
t.pendown()
t.circle(60)
t.penup
t.setheading(40)
t.fd(750)
```
- t.shape("~~"): 이동체의 모양 설정
- t.penup(): 이동체의 선을 제거
- t.goto(x,y): 이동체를 (x,y)좌표로 이동
- t.pendown(): 이동체의 선을 생성
- t.circle(x): 둘레 x만큼 원 생성
- t.setheading(y): y각도로 위치 조정
- t.fd(z): z만큼 앞으로 이동

```
# 장애물 만들기
for i in range(4):
    t.fd(100)
    t.rt(90)
```
- for i in range(4): 4번 반복
- f.rt(90): rt는 right의 약자, 90도만큼 오른쪽으로 회전

```
# 장애물 피하기 + 이동거리 계산
t.fd(330)
t.setheading(90)
t.fd(70)
t.setheading(0)
t.fd(150)
t.setheading(33)
t.fd(230)

# 실제 이동거리
# t.fd(330) + t.fd(70) + t.fd(150) + t.fd(230) = t.fd(780)
```
- 실제 이동거리는 장애물을 피해서 가기 때문에 직선 거리보다 길다.
```
#목표 지점 도달 확인 함수
import math

def is_arrived(t, target_x, target_y, tolerance=100):
    """
    t: 거북이 객체
    target_x, target_y: 목표 좌표
    tolerance: 허용 오차 (픽셀)
    """
    current_x, current_y = t.position()
    distance = math.sqrt((target_x - current_x) ** 2 + (target_y - current_y) ** 2)
    return distance <= tolerance

# 예시 실행:
# 거북이가 이동을 끝낸 뒤 호출하면 됨.
if is_arrived(t, 300, 100):
    print("목표 지점에 도착했습니다!")
else:
    print("아직 목표 지점에 도달하지 못했습니다.")
```
- 현재 위치인 current_x, current_y를 이용해 목표 좌표에 도달했는지 확인
- tolerance: 허용 오차 

```
# 거북이 충돌 감지 함수
def is_collided_with_obstacle(t, obs_x1, obs_y1, obs_x2, obs_y2):
    """
    t: 거북이 객체
    obs_x1, obs_y1: 사각형 왼쪽 아래 꼭짓점
    obs_x2, obs_y2: 사각형 오른쪽 위 꼭짓점
    """
    x, y = t.position()
    if obs_x1 <= x <= obs_x2 and obs_y1 <= y <= obs_y2:
        return True
    else:
        return False
    
# 장애물 충돌 여부 출력
if is_collided_with_obstacle(t, 0, -100, 100, 0):
    print("장애물에 충돌했습니다!")
else:
    print("장애물 피하기 성공!")
```
- obs_x1,y1,x2,y2로 장애물의 꼭짓점을 설정하고 이동체가 장애물에 충돌했는지 판별
- is_collided_with_obstacle 정의

```
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
    
    
    print("장애물 충돌! 회피 시작...")
    t.backward(40)  # 충분히 후진
    
    # 장애물 주위를 돌면서 완전히 벗어날 때까지 반복
    turn_angle = 45  # 45도씩 회전하며 빙글빙글
    while is_collided_with_obstacle(t, obs_x1, obs_y1, obs_x2, obs_y2):
        t.right(turn_angle)
        t.forward(15)
        time.sleep(0.02)
    print("장애물 벗어남!")

#메인 이동 루프: 시작점에서 종점까지 이동하며 회피
    
#목표 좌표와 장애물 좌표
goal_x, goal_y = 300, 150
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
```
- t.backward(30): 장애물과 부딪혔을때 뒤로 후진하기 위함
- turn_angle = random.randint(90,180): 장애물을 감지했을 때 90~180도 사이 랜덤 회전
- while not is_arrived(t, goal_x, goal_y): 목표지점인 goal_x, goal_y에 도달하기 전까지 반복되는 함수
- angle = math.degrees(math.atan2(dy, dx): 장애물을 벗어나서 목표 지점까지 가기 위한 방향을 재설정

