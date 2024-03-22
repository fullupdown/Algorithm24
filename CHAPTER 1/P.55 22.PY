#202110674 서강찬
#Chapter 1
#문제 22_사용자로부터 문자열을 입력받고 이것을 역순으로 출력하는 프로그램을 작성, 단 스택구조를 사용
a = input("문자열 입력: ")

stack=list(a)

while stack:
    print(stack.pop(),end='')
