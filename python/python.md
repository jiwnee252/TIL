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
