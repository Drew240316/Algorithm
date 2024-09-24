# enumerate 함수는 인덱스와 원소를 짝지어 튜플로 꺼내는 내장 함수이다.
# enumerate(리스트 형태의 변수명)


## 리스트의 모든 원소들을 enumerate()함수로 짝지어서 튜플로 꺼내기

name = ['John','George','Paul','Ringo']

for i, name in enumerate(name):
    print(f'x[{i}] = {name}이다.')