#UP&DOWN

import random #random 모듈 불러오기
q=random.randrange(1,100) #(1~100까지 랜덤값 생성)
num=int(0) #num 변수값 지정
print('랜덤 값:', q)
while num !=q: # 조건은 입력된 num이 생성된 랜덤값이 아닐경우. 계속 루프된다.
    num=int(input('예상 숫자를 입력하세요'))
    print('당신은',num,'를(을) 입력하였습니다.')

    if int(num)>q:
        print('UP!')
    elif int(num)<q:
        print('DOWN!')
    elif int(num)==q:
        print('숫자를 맞혔습니다. GOOD!')

