# 튜플, 딕셔너리, 집합
# t1 = (1, 2, 'a', 'b')
# t2 = (3, 4)
# t3 = t1 + t2
# print(len(t3))

# dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'} # 'key': 'value'
# print(dic.keys()) # 딕셔너리의 key값을 dict_keys 객체로 변환
# print(dic.values()) # 딕셔너리의 value값을 dict_keys 객체로 변환
# print(dic.items()) # 딕셔너리의 key, value값을 dict_keys 객체로 변환
# dic.clear() # 딕셔너리 제거 {} 빈 딕셔너리 출력

# print(dic['hi'])
# print(dic.get('hi', '값이 없습니다.'))

# 반복문
# for i in dic.keys():
#   print(i)

# print('name' in dic)

s1 = set("hello") # 집합은 별도의 순서가 없고(index 사용 불가), 중복값이 없음. list의 중복값을 제거할 때 사용
# print(list(s1))

a1 = set([1, 2, 3, 4, 5, 6])
a2 = set([4, 5, 6, 7, 8, 9])
print(a1 & a2) # 교집합(intersection도 사용 가능)
print(a1 | a2) # 합집합(union도 사용 가능)
print(a2 - a1) # 차집합(difference도 사용 가능)

a1.add(10) # 1개의 값을 추가할 때
a1.update([11, 12, 13]) # 여러개의 값을 추가할 때
print(a1)

a1.remove(12)
print(a1)