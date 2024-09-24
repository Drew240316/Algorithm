from typing import Any, MutableSequence  #typing 모듈, Any 함수(어떤 자료형이든 괜찮다

def reverse_array(a:MutableSequence) -> None:
    n = len(a)
    for i in range(n//2):
        a[i],a[n-i-1] = a[n-i-1],a[i]

if __name__ == '__main__':
    print("배열 원소를 역순으로 바꿔봅시다.")
    nx = int(input("원소 수를 입력하세요.: "))
    x = [None] * nx  #원소 수가 nx인 리스트 생성

    for i in range(nx):
        x[i] = int(input(f'x[{i}]값을 입력하세요.: '))

    reverse_array(x)

    print("배열 원소를 역순으로 정리했습니다.")
    for i in range(nx):
        print(f'x[{i}] = {x[i]}입니다.')



