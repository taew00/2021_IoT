import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4
segments =  [10,11,12,13,14,15,16]
test_pin = 17 
digits = [18,19,20,21]
switches = [23,24] # 각각의 핀 정의

GPIO.setmode(GPIO.BCM) # BCM 모드로 변경

GPIO.setup(BUZZER_PIN,GPIO.OUT)

for segment in segments:
    GPIO.setup(segment,GPIO.OUT)
    GPIO.output(segment,GPIO.LOW)

GPIO.setup(17,GPIO.OUT)
GPIO.output(17,GPIO.LOW)

for switch in switches:
    GPIO.setup(switch,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

for digit in digits:
    GPIO.setup(digit,GPIO.OUT)
    GPIO.output(segment,GPIO.HIGH) # 각각 기본 세팅

pwm = GPIO.PWM(BUZZER_PIN,1) # 부저 설정

num =[[1,1,1,1,1,1,0],
    [0,1,1,0,0,0,0],
    [1,1,0,1,1,0,1],
    [1,1,1,1,0,0,1],
    [0,1,1,0,0,1,1],
    [1,0,1,1,0,1,1],
    [1,0,1,1,1,1,1],
    [1,1,1,0,0,0,0],
    [1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1],
    [0,0,0,0,0,0,0]] # 세그먼트 사용성을 높이기 위한 리스트 설정

def display(a,b):
    for i in range(len(digits)):
        if i + 1 == a:
            GPIO.output(digits[i],GPIO.LOW)
        else:
            GPIO.output(digits[i],GPIO.HIGH) 

    if a == 2:
        GPIO.output(17,1)
    else:
        GPIO.output(17,0)

    for j in range(len(segments)):
        GPIO.output(segments[j],num[b][j]) # 세그먼트에 숫자를 표시하는 함수
    time.sleep(0.001)

def timeset(a):
    display(1,int(a/1000))
    display(2,int(a/100)%10)
    display(3,int(a/10)%10)
    display(4,a%10) # 세그먼트 4칸을 각각 원하는 수로 설정

set = 0
ti = 0.0
start = 0 
val = [0,0]
stack = 0.0 # 필요한 함수들 정의

try :
    while True:
        for i in range(len(switches)):
            val[i] = GPIO.input(switches[i]) # 각 스위치의 눌린 상태 저장

        timeset(int(ti)) # 4-digit 숫자 표시

        if start == 0 and stack >= 1: # 스톱워치가 대기 상태일 때
            if val[0] == 1: # 1번 스위치가 눌렸을 때 버튼이 눌렸으니 부저 소리를 잠시 내고 스톱워치를 시작
                pwm.start(30)
                start = 1 - start
                stack = 0.8
            if val[1] == 1: # 2번 스위치가 눌렸을 때 버튼이 눌렸으니 부저 소리를 잠시 내고 스톱워치를 리셋
                pwm.start(30) 
                ti = 0
                stack = 0
                start = 0

        if start == 1 and stack >= 1: # 스톱워치가 작동 중 일때
            ti = ti + 0.5 # 시간이 올라가는 단위를 조정
            if val[0] == 1: # 1번 스위치가 눌렸을때 소리를 내고 스위치를 대기 상태로 전환
                pwm.start(30)
                start = 1 - start
                stack = 0
        
        if stack < 1: # 텀을 조절하기 위한 변수값 조정
            stack = stack + 0.003
        
        if val[0] == 0 and val[1] == 0: # 부저가 잠시만 울리기 위한 조건
            pwm.stop()
            
finally:
    GPIO.cleanup()
    print ('cleanup and exit')