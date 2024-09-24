## 함수 정의
# 최댓값 구하는 것은 스캔 형식을 쓴다. 스캔은 돌고 돌아서 가장 큰 값을 가져오는 것
# 변수는 maximum


from typing import Any, Sequence # 만약 코드를 적는데,Unused import statement 'from typing import Any, Sequence' 같이 나온다면, 코드에서 실행되지 않았음을 의미.계속 작성하면 됨.

def max_of(a :Sequence) -> Any:
    maximum = a[0] #초기 최댓값을 0번째로 만든단 얘기임.

    for i in range(1,len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum



## 함수 호출
# 입력 : 문자형태 입력>정수변환>담을 리스트 만들기
# 과정 : 리스트안에 정수 변환된 수 넣기
# 출력 : max_of함수를 써서 리스트에서 가장 큰 값 출력

if __name__ == '__main__' :
    print("배열의 최댓값을 구합시다!")
    num = int(input('원소 수를 입력하시오.: '))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요.'))
    print(f'최댓값은 {max_of(x)}입니다.')
        