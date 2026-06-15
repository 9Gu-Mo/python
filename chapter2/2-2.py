# 문자열 인덱스, 슬라이스, 포매팅, 함수
# head = "Life is too short"
# tail = "You need python"
# print(head + tail)

# multiply = "python"
# print(multiply * 3)

# 터미널 구분선
# contour = "="
# print(contour * 50)
# print(head + tail)
# print(contour * 50)

# 터미널 구분선 함수
def print_border(char="=", length=50):
  print(char * length)


# print(len(multiply))
# print_border()

# print(multiply[3])
# print(multiply[-1]) # 음수는 인덱스의 마지막값 부터 출력
# print_border()

# print(multiply[0:]) # print(multiply[이상:미만:간격])
# print(multiply[0:3])
# print(multiply[::-1]) # 문자열 리버스
# print_border()

# dummy="20260615sunny"
# date=dummy[:8]
# weather=dummy[8:]
# print(date)
# print(weather)
# print_border()

# formatDec = "I eat %d apples" % 3
# print(formatDec)
# print_border()

# formatStr = "I eat %s apples" % "three"
# print(formatStr)
# print_border()

# number = 3
# day = 'three'
# formatVar = "I ate %d apples. so I was sick %s days." % (number, day) #변수 타입에 따라 포맷팅 변경
# print(formatVar)

# deciaml = "%.2f" % 3.141592
# print(deciaml)
# print_border()

# format = "I ate {0} apples. so I was sick {1} days." .format(number, day)
# print(format)
# print_border()

# a="{0:<10}" .format("hi")
# print(a)
# a="{0:>10}" .format("hi")
# print(a)
# a="{0:^10}" .format("hi")
# print(a)
# a="{0:=^10}" .format("hi")
# print(a)

# name = "홍길동"
# age = 30
# info = f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
# print(info)

a='hobby'
print(a.index('b')); # find 사용 시 결과값이 -1이 나오면 없는값 / index 사용 시 결과값이 오류라면 없는값
print_border()

a=", ".join(['a', 'b', 'c', 'd'])
print(a)
print_border()

a=" hi  "
print(a.strip())
print_border()

a='life is too short'
print(a.replace('life', 'money'))
print_border()

a='life is too short'
print(a.split())
print_border()

a="a:b:c:d"
print(a.split(":"))