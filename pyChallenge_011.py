input_big = int(input('100이 넘는 숫자를 입력하세요. : '))
input_small = int(input('위 보다, 작은 수를 입력하세요. : '))
answer = input_big / input_small
import math
print(math.floor(answer),'번 들어갈 수 있습니다.')

#내가 한 방식은 math module을 불러와서 내림을 한 상태,
#더 간단한 방법을 사용하기 위해서는 input_big // input_small을 사용하면 된다.
