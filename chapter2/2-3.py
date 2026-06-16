# 리스트 자료형
# 터미널 구분선 함수
def print_border(char="=", length=50):
  print(char * length)

# 리스트 출력
# a = [1, 2, ['Life', 'is']]
# print(a[2][0])

# a = [1, 2, 3, 4, 5]
# print(a[0::2])

# a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
# print(a[3][:2])

# 리스트 병합
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c[-1])

# 리스트 타입 형변환
# a = [1, 2, 3]
# print(str(a[2]) + "hi")

# 리스트 삭제 del
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# del c[2:]
# print(c)

# 리스트 추가 append
# a = [1, 2, 3]
# a.append(4)
# a.append([5,6])
# print(a)

# 리스트 정렬
# a = [1, 4, 3, 2]
# a.sort(reverse=True) # sort는 기본적으로 오름차순 정렬. 내림차순 시 reverse변수 지정 필요
# print(a)

# 리스트 인덱스
# a = [1, 4, 3, 2, 'hi']
# print(a.index('hi')) # index의 소괄호값은 리스트의 값을 추적함. 

# 리스트 요소 삽입 insert
# a = [1, 2, 3]
# a.insert(0, 4)
# print(a)

# 리스트 요소 제거 remove
# a = [1, 2, 3, 3, 2, 1]
# a.remove(3)
# print(a)

# 리스트 요소 제거 pop
# a = [1, 2, 3]
# print(a.pop(1))

# 리스트 요소 세기
# a = [1, 2, 3, 1, 2, 3]
# print(a.count(2))

# 리스트 확장
a = [1, 2, 3]
a.extend([4, 5]) # append 사용 시 [4, 5] 리스트 자체가 a 리스트에 들어감
print(a)