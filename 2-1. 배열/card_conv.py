 #10진수 정숫값을 입력받아, 2~36진수로 변환하여 출력하기 #들여쓰기 4칸 주의해서 적용
def card_conv(x: int, r: int) -> str:
    d = ''  # 변환된 값을 저장할 문자열
    dchar = '0123456789abcdefghijklmnopqrstuvwxyz'  # 진수에 따라 사용할 문자

    while x > 0:
        d += dchar[x % r]  # x를 r로 나눈 나머지를 해당 진법의 문자로 변환
        x //= r  # x를 r로 나눈 몫으로 업데이트

    return d[::-1]  # 문자열을 역순으로 변환해서 반환

if __name__ == '__main__':
    print('10진수를 n진수로 반환합니다.')

    while True:
            while True : #음이 아닌 정수를 입력받음
                no = int(input('변환할 값으로 음이 아닌 정수를 입력하세요.: '))
                if no > 0:
                    break

            while True: #2~36진수의 정숫값을 입력받음
                cd = int(input('어떤 진수로 변환할까요?: ex)36'))
                if 2 <= cd <= 36:
                    break
            print(f'{cd}진수로는 {card_conv(no,cd)}입니다.')

            retry = input("한 번 더 변환할까요?(Y ... 예 . N... 아니요): ")
            if retry in {'N','n'}:
                break
