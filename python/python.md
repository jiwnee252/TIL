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
- L.extend(m) : Iterable m의 모든 항목들을 리스트 끝에 추가 (+=과 같은 기능)  
- L.insert(i, x) : 리스트 인덱스 i에 항목 x를 삽입  
- L.remove(x) : 리스트 가장 왼쪽에 있는 항목(첫 번째) x를 제거 / 항목이 존재하지 않을 경우 ValueError  
- L.pop() : 리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거  
- L.pop(i) : 리스트의 인덱스 i에 있는 항목을 반환 후 제거  
- L.clear() : 리스트의 모든 항목 삭제  

- 리스트는 가변이므로 원본이 바뀜에 주의  

```python
# append
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]
print(my_list.append(4))  # None # append함수는 리턴이 없음 # 원본을 수정하는 메서드
```

```python

```

```python

```

```python

```

```python

```

```python

```