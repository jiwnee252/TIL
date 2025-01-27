# Lambda expressions (람다 표현식)

- 익명 함수를 만드는 데 사용되는 표현식

## 람다 표현식 구조

```python
lambda 매개변수 : 표현식
```

## 람다 표현식 예시

```python
def addition(x, y):
  return x + y
```

```python
lambda x, y: x + y
```

```python
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x**2

# lambda 미사용
squared1 = list(map(square, numbers))
print(squared1)  # [1, 4, 9, 16, 25]

# lambda 사용
squared2 = list(map(lambda x: x**2, numbers))
print(squared2)  # [1, 4, 9, 16, 25]
```

```python
# 일반 함수 사용
def list_mul(x):
    return x * 2

result = list(map(list_mul, [1, 2, 3]))
print(result)  # 출력: [2, 4, 6]

# 람다 표현식 사용
result = list(map(lambda x: x * 2, [1, 2, 3]))
print(result)  # 출력: [2, 4, 6]
```

# List Comprehension

- 리스트를 간결하게 한 줄로 만들 수 있는 문법

```python
[expression for 변수 in iterable]

list(expression for 변수 in iterable)
```

```python
[expression for 변수 in iterable if 조건식]

list(expression for 변수 in iterable if 조건식)
```

```python
#사용 전
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
  squared_numbers.append(num**2)

print(squared_numbers) #[1, 4, 9, 16, 25]
```

```python
#사용 후
numbers = [1, 2, 3, 4, 5]

squared_numbers = [num**2 for num in numbers]

print(squared_numbers) #[1, 4, 9, 16, 25]
```

###### 참고자료

[list comprehension](https://shoark7.github.io/programming/python/about-list-comprehension-python)

# enumerate(iterable, start = 0)

- iterable 객체의 각 요소를 순회하면서 각 요소의 인덱스와 값을 순서쌍으로 반환하는 내장함수

###### 참고자료

[파이썬의 enumerate() 내장 함수로 for 루프 돌리기] (https://www.daleseo.com/python-enumerate/)

# 메서드

- 클래스 내부에 정의되는 함수
- 클래스란 파이썬에서 타입을 표현하는 방법
- 각 데이터 타입별로 다양한 기능을 가진 메서드 존재

```python
def add(a, b):
  return a + b
```

```python
class Calculator:
  def add(self, a, b):
    return a + b
```

```python
# 함수 호출
add(1, 2)
```

```python
# 메서드 호출
a = Calculator()
a.add(1, 2)
```

## 문자열 조회/탐색 및 검증 메서드

- s.find(x) : x의 첫 번째 위치를 반환, 없으면 -1을 반환
- s.index(x) : x의 첫 번째 위치를 반환, 없으면 오류 발생
- s.isupper() : 문자열 내의 모든 문자가 대문자인지 확인
- s.islower() : 문자열 내의 모든 문자가 소문자인지 확인
- s.isalpha() : 문자열 내의 모든 문자가 알파벳인지 확인 / 단순 알파벳이 아닌 유니코드상 letter (한국어 포함)

- 메서드, 함수 이름이 is로 시작할 경우 반환값은 대부분 Boolean

## 문자열 조작 메서드 (새 문자열 반환)

- s. replace(old, new[,count]) : 바꿀 대상 글자를 새로운 글자로 바꿔서 반환 / 대괄호[] 내부는 선택적 인자, 기술문서에 사용
- s.strip([chars]) : 공백이나 특정 문자를 제거
- s.split(sep=None, maxsplit=-1) : sep을 구분자 문자열로 사용하여 문자열에 있는 단어들의 리스트를 반환
- 'separator'.join(iterable) : 구분자로 iterable의 문자열을 연결한 문자열을 반환

- s.capitalize() : 가장 첫 번째 글자를 대문자로 변경
- s.title() : 문자열 내 띄어쓰기 기준으로 각 단어의 첫 글자는 대문자로, 나머지는 소문자로 변환
- s.upper() : 모두 대문자로 변경
- s.lower() : 모두 소문자로 변경
- s.swapcase() : 대소문자 서로 변경

```python
# replace
text = 'Hello, world! world world'
new_text1 = text.replace('world', 'Python')
new_text2 = text.replace('world', 'Python', 1)
print(new_text1)  # Hello, Python! Python Python
print(new_text2)  # Hello, Python! world world

text = 'Hello, world! world world world world'
new_text3 = text.replace('world', 'Python', 2)
new_text4 = text.replace('world', 'Python', 3)
print(new_text3) # Hello, Python! Python world world world
print(new_text4) # Hello, Python! Python Python world world
```

```python
# strip
text = '  Hello, world!  '
new_text = text.strip()
print(new_text) # Hello, world!
```

```python
# split # 리스트를 반환
text = 'Hello, world!'
words1 = text.split(',')
words2 = text.split()
print(words1)  # ['Hello', ' world!']
print(words2)  # ['Hello,', 'world!']
```

```python
# join
words = ['Hello', 'world!']
new_text = '-'.join(words)
new_text2 = ''.join(words)
words2 = ['Hello', 'world!', 3, 100]
new_text3 = ''.join(words2)
print(new_text)  # Hello-world!
print(new_text2) # Helloworld!
print(new_text3) # TypeError: expected str instance, int found
```

## 리스트 값 추가 및 삭제 메서드

- L.append(x) : 리스트 마지막에 항목 x를 추가 / append 자체의 반환값은 없음에 주의
- L.extend(m) : Iterable m의 모든 항목들을 리스트 끝에 추가 (+=과 같은 기능) / 반복 가능한 객체가 아니면 추가 불가
- L.insert(i, x) : 리스트 인덱스 i에 항목 x를 삽입
- L.remove(x) : 리스트 가장 왼쪽에 있는 항목(첫 번째) x를 제거 / 항목이 존재하지 않을 경우 ValueError
- L.pop() : 리스트 가장 오른쪽에 있는 항목(마지막)을 제거
- L.pop(i) : 리스트의 인덱스 i에 있는 항목을 반환 후 제거
- L.clear() : 리스트의 모든 항목 삭제 (리스트 초기화)

- 리스트는 가변이므로 원본이 바뀜에 주의

```python
# append
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]
print(my_list.append(4))  # None # append함수는 리턴이 없음 # 원본을 수정하는 메서드
```

```python
# extend
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  # [1, 2, 3, 4, 5, 6]
# [1, 2, 3] += [4, 5, 6]
my_list.extend(5) # TypeError: 'int' object is not iterable
```

```python
# append와 extend의 비교
my_list.append([4, 5, 6])
print(my_list) # [1, 2, 3, 4, 5, 6, [4, 5, 6]]
```

```python
# insert
my_list = [1, 2, 3]
my_list.insert(1, 5) # 인덱스 1 위치에 항목 5를 삽입입
print(my_list)  # [1, 5, 2, 3]
```

```python
# remove
my_list = [1, 2, 3, 2, 2, 2]
my_list.remove(2)
print(my_list)  # [1, 3, 2, 2, 2]
```

```python
# pop
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()
item2 = my_list.pop(0)

print(item1)  # 5
print(item2)  # 1
print(my_list)  # [2, 3, 4]
```

```python
# clear
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # []
print(my_list.clear()) # None
```

## 리스트 탐색 및 정렬 메서드

- L.index(x) : 리스트에서 첫 번째로 일치하는 항목 x의 인덱스를 반환
- L.count(x) : 리스트에서 항목 x의 개수를 반환
- L.reverse(x) : 리스트의 순서를 역순으로 변경(정렬 x)
- L.sort(x) : 리스트를 정렬(매개변수 이용가능)

```python
# index
my_list = [1, 2, 3]
index = my_list.index(2)
print(index)  # 1
```

```python
# count
my_list = [1, 2, 2, 3, 3, 3]
counting_number = my_list.count(3)
print(counting_number)  # 3
```

```python
# reverse
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse() # 반환이 없으므로 이 자체를 프린트하면 None
# print(my_list.reverse())  # None
print(my_list)  #[9, 1, 8, 2, 3, 1]  # 정렬 x
```

```python
# sort
my_list = [3, 2, 100, 1]
my_list.sort()
print(my_list)  # [1, 2, 3, 100]
print(my_list.sort()) # None

# sort(내림차순 정렬)
my_list.sort(reverse=True)
print(my_list)  # [100, 3, 2, 1]
```

## 딕셔너리 메서드

## 세트 메서드

### 메서드 체이닝

- 여러 메서드를 연속해서 호출하는 방식

- 모든 메서드가 체이닝을 지원하는 것은 아님

  - 메서드가 객체를 반환할 때만 체이닝이 가능

- None을 반환하는 메서드는 메서드 체이닝이 불가능

  - 리스트의 append(), sort()

- 메서드 체이닝을 사용할 때는 각 메서드의 반환 값을 잘 이해하고 있어야 함

```python
# 문자열 메서드 체이닝
text = 'heLLo, woRld!'
new_text = text.swapcase().replace('l', 'z')
print(new_text)  # HEzzO, WOrLD!

# 1. 단계별로 실행하기
text = 'heLLo, woRld!'
step1 = text.swapcase()
print('1단계 결과:', step1)  # HEllO, WOrLD!

step2 = step1.replace('l', 'z')
print('2단계 결과:', step2)  # HEzzO, WOrLD!

# 2. 한 줄로 실행하기 (위와 동일한 결과)
new_text = text.swapcase().replace('l', 'z')
print('최종 결과:', new_text)  # HEzzO, WOrLD!
```

```python
# 리스트에서의 메서드 체이닝 예시
# copy()로 리스트를 복사한 후, sorted()함수로 정렬

# 잘못된 체이닝 방식 1
numbers = [3, 1, 4, 1, 5, 9, 2]
result = numbers.copy().sort() # copy는 반환이 있음
print(result)  # None (sort()는 None을 반환하므로 체이닝이 중단됨)
print(numbers)  # [3, 1, 4, 1, 5, 9, 2] (원본은 변경되지 않음)

# 잘못된 체이닝 방식 2
result = numbers.append(7).extend([8, 9])  # AttributeError # numbers.append(7)의 결과는 None이므로 끝나버린다 (None.extend와 같아지므로) # 따라서 이 경우 메서드 체이닝 안됨

# 개선된 방식
# 리스트 조작에서 메서드 체이닝을 사용할 때는 각 메서드가 적절한 값을 반환하는지 확인하고,
# 필요한 경우 새로운 리스트 객체를 반환하는 함수를 사용하는 것이 좋음
sorted_numbers = sorted(numbers.copy())
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 9]
```

## 문자 유형 판별 메서드

- isdecimal() : 문자열이 모두 숫자 문자(0~9)로만 이루어져 있어야 True
- isdigit() : isdecimal()과 비슷하지만, 유니코드 숫자도 인식('①'도 숫자로 인식)
- isnumeric() : isdigit()과 유사하지만, 몇 가지 추가적인 유니코드 문자들을 인식 (분수, 지수, 루트 기호도 숫자로 인식)

###### 참고

```python
help()
# print(help(list))
```

---

# 복사

## 객체와 참조

- 가변 객체 (mutable): 생성 후 내용 변경 가능 / list, dict, set
  - 객체의 내용이 변경되어도 같은 메모리 주소를 유지
- 불변 객체 (immutable): 생성 후 내용 변경 불가 / int, float, str, tuple
  - 새로운 값을 할당하면 새로운 객체가 생성되고, 변수는 새 객체를 참조하게 됨

```python
# mutable  # list
a = [1, 2, 3, 4]
b = a # 복사가 아니다! # 값을 할당 x, 주소를 할당 o
b[0] = 100

print(a) # [100, 2, 3, 4]
print(b) # [100, 2, 3, 4]
print(a is b) #True
```

```python
# immutable  # int
a = 20
b = a
b = 10

print(a)  # 20
print(b)  # 10
print(a is b)  # False
```

```python
print('\n메모리 주소 확인')
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(f'x의 id: {id(x)}') # 2771879759360
print(f'y의 id: {id(y)}') # 2771879759360
print(f'z의 id: {id(z)}') # 2771879766272
print(f'x와 y는 같은 객체인가? {x is y}') # True
print(f'x와 z는 같은 객체인가? {x is z}') # False
```

- 변수 할당이란 객체에 대한 참조를 생성하는 과정
- 변수는 객체의 메모리 주소를 가리키는 label 역할을 함
- '=' 연산자를 사용하여 변수에 값을 할당
- 할당 시 새로운 객체가 생성되거나 기존 객체에 대한 참조가 생성됨

- 변수는 객체의 '메모리 주소'를 저장, 여러 변수가 동일한 객체를 참조할 수 있음
- id() 함수를 사용하여 객체의 메모리 주소 확인 가능
- is 연산자를 통해 두 변수가 같은 객체를 참조하는지 확인 가능

### 이러한 동작의 이유?

- 성능 최적화

  - 불변 객체는 변경이 불가능하므로, 여러 변수가 동일한 객체를 안전하게 공유할 수 있음
  - 가변 객체는 내용 수정이 빈번한 경우 새 객체를 생성하지 않고 직접 수정하여 성능을 향상시킴

- 메모리 효율성
  - 불변 객체는 동일한 값을 가진 여러 객체가 메모리를 공유할 수 있어 효율적
  - 가변 객체는 크기가 큰 데이터를 효율적으로 수정할 수 있음

## 얕은 복사 shallow copy

- 객체의 최상위 요소만 새로운 메모리에 복사하는 방법
- 내부에 중첩된 객체가 있다면 그 객체의 참조만 복사됨
- 리스트 슬라이싱, copy() 메서드, list() 함수

```python
# 1차원 리스트
a = [1, 2, 3]
b = a[:]  # 슬라이싱 (처음부터 끝까지)
c = a.copy()  # copy() 메서드
d = list(a)  # list() 함수

print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3]
print(c)  # [1, 2, 3]

b[0] = 100
c[0] = 999
d[0] = 8080

print(a)  # [1, 2, 3] # 원본은 그대로
print(b)  # [100, 2, 3]
print(c)  # [999, 2, 3]
print(d)  # [8080, 2, 3]
```

- 얕은 복사의 한계

  - 다차원 리스트와 같이 변경 가능한 객체 안에 변경 가능한 객체가 있는 경우

- 1차원 리스트와 다차원 리스트에서의 차이점
  - 1차원 리스트 : 얕은 복사로 충분히 독립적인 복사본을 만들 수 있음
  - 다차원 리스트 : 최상위 리스트만 복사되고, 내부 리스트는 여전히 원본과 같은 객체를 참조

```python
a = [1, 2, [3, 4, 5]]
b = a[:]

b[0] = 999
print(a)  # [1, 2, [3, 4, 5]]
print(b)  # [999, 2, [3, 4, 5]]

b[2][1] = 100
print(a)  # [1, 2, [3, 100, 5]]
print(b)  # [999, 2, [3, 100, 5]]
print(f'a[2]와 b[2]가 같은 객체인가? {a[2] is b[2]}')  # True
```

## 깊은 복사 deep copy

- 객체의 모든 수준의 요소를 새로운 메모리에 복사하는 방법
- 중첩된 객체까지 모두 새로운 객체로 생성됨
- copy모듈에서 제공하는 deepcopy() 함수를 사용

```python
import copy

new_object = copy.deepcopy(original_object)
```

```python
import copy

a = [1, 2, [3, 4, 5]]
b = copy.deepcopy(a)

b[2][1] = 100
print(a)  # [1, 2, [3, 4, 5]]
print(b)  # [1, 2, [3, 100, 5]]
print(f'a[2]와 b[2]가 같은 객체인가? {a[2] is b[2]}')  # False
```

```python
# 복잡한 중첩 객체 예시
import copy

original = {
    'a': [1, 2, 3],
    'b': {
        'c': 4,
        'd': [5, 6],
    },
}
copied = copy.deepcopy(original)

copied['a'][1] = 100
copied['b']['d'][0] = 500

print(f'원본: {original}')  # {'a': [1, 2, 3], 'b': {'c': 4, 'd': [5, 6]}}
print(f'복사본: {copied}')  # {'a': [1, 100, 3], 'b': {'c': 4, 'd': [500, 6]}}
print(
    f'original["b"]와 copied["b"]가 같은 객체인가? {original["b"] is copied["b"]}'
)  # False
```

###### 참고자료

[할당, 얕은 복사와 깊은 복사](https://www.youtube.com/watch?v=RJqvaj8MI_o&ab_channel=%EB%84%90%EB%84%90%ED%95%9C%EA%B5%90%EC%88%98%EC%9D%98%EC%BD%94%EB%94%A9%ED%81%B4%EB%9E%98%EC%8A%A4)

# 해시 테이블

- 해시 함수를 사용하여 변환한 값을 인덱스로 삼아 키key와 데이터value를 저장하는 자료구조
- 데이터를 빠르게 저장하고 검색하기 위해 사용
