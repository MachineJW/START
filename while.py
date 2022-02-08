#UP&DOWN

import random #random 모듈 불러오기
import time # 지연시키 위해 time 모듈을 불러온다.
q=random.randrange(1,100) #(1~100까지 랜덤값 생성)
num=int(0) #num 변수값 지정
print('랜덤 값:', q)
while num !=q: # 조건은 입력된 num이 생성된 랜덤값이 아닐경우. 계속 루프된다.
    #예외처리 int(정수형이 아닌 문자형이나 실수형이 들어왔을때)
    try:
        num=int(input('1~99까지의 예상 숫자를 입력하세요: '))
    except:
        print('주의: 1~99까지의 예상 숫자만 입력하세요!!')
        continue #형의 오류가 났다면 메세지를 출력하고 다음 구문을 실행한다. break는 while문을 빠져나갈때.

    print('당신은',num,'를(을) 입력하였습니다.')

    if int(num)<q:
        print('UP!')
    elif int(num)>q:
        print('DOWN!')
    elif int(num)==q:
        print('숫자를 맞혔습니다. GOOD!')

time.sleep(3) # 3초뒤에 프로그램 종료


