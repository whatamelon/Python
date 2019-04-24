#sys1.py
import sys

args = sys.argv[1:]
for i in args:
    print(i)
    
# import sys 모듈을 사용하기 위해 아래와 같은 import 라는 명령어를 사용해야 함

# for문을 이용해 차례대로 하나씩 출력하는 예시임

# sys 모듈의 argv는 명령어 창에서 입력한 인수를 의미함

# 아래와 같이 입력한다면 argv[0]은 파일이름인 sys1.py 가 되고
# argv[n] 차례대로 요소가 됨