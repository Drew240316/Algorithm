## 리스트들의 동일성 확인 : 같은 곳에 참조가 되는가?
list1 = [1,2,3]
list2 = [1,2,3]

print(list1 is list2) #False로 나옴. 참조번호 다름, ip()로 확인 가능. why? 리스트는 리터럴(litaral) 고정값이 아님.


## 리스트에 리스트를 대입하면, 리스트는 리스트를 참조한다.
list1 = [1,2,3]
lsit2 = [1,2,3]
list1 = list2

print(list1 is list2) #True로 나옴  # list1은 list2를 참조한다. ( 실제로 list1과 lst2는 같은 실체(리스트)를 참조하는 것이다.

list1[2] = 9  # 따라서 원소값을 바꾸면, list2의 원소값도 달라진다.
print(list1)

