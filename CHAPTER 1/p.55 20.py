#202110674 서강찬
#Chapter 1
#문제 20_두 개의 리스트를 입력받아 리스트에 같은 항목이 있으면 True를 없으면 False를 반환하는 함수.
list1 = input("첫 번째 리스트(쉼표로 구분): ").split(',')
list2 = input("두 번째 리스트(쉼표로 구분): ").split(',')

# 두 리스트의 교집합 찾기
if set(list1) & set(list2):
    print(True)
else:
    print(False)

