# 1,000이하의 소수 나열하기
# n이 소수일 때 for 문은 마지막 까지 실행 -> else문을 실행하여 n값을 출력한다.
# n이 합성수일 때: for 문은 중단


counter = 0 #나눗셈 횟수를 카운트

for n in range(2,1001):
    for i in range(2,n):
        counter += 1   # 나눗셈 횟수 증가
        if n % 1 == 0: #나누었는데 떨어지면 소수가 아님 4 6 8...
            break  #반복 불필요하여 중단
    else :  #끝까지 나누어 떨어지지 않으면 다음을 수행
        print(n)

print(f"나눗셈을 실행한 횟수 : {counter}")