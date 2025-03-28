from typing import Union
from fastapi import FastAPI
import time
import random
import numpy  as np

app = FastAPI()

@app.get("/")
def read_root():
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])
    return {"Hello": result}

@app.get("/two-dimensional-array")
def two_dimensional_array():
    a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    b = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    result=[[a[i][j] + b[i][j] for j in range(len(a[0]))]for i in range(len(a))]

    return {"result": result}

# @app.get("/add-large-arrays")
# def add_large_arrays():
#     N = 10**6  # 100만 개 요소

#     # Python 리스트로 랜덤한 1차원 배열 생성
#     start_creation_time = time.time()
#     list_a = [random.randint(0, 100) for _ in range(N)]
#     list_b = [random.randint(0, 100) for _ in range(N)]
#     end_creation_time = time.time()

#     # 실행 시간 측정 (리스트 컴프리헨션 사용)
#     add_start_time = time.time()
#     result = [list_a[i] + list_b[i] for i in range(N)]
#     add_end_time = time.time()

#     return {
#         "array_creation_time": end_creation_time - start_creation_time,
#         "addition_time": add_end_time - add_start_time
#         }

# @app.get("/add-large-arrays-choices")
# def add_large_arrays_choices():
#     N = 10**6  # 100만 개 요소

#     # Python 리스트로 랜덤한 1차원 배열 생성
#     start_creation_time = time.time()
#     list_a = [random.choice(range(101)) for _ in range(N)]
#     list_b = [random.choice(range(101)) for _ in range(N)]
#     end_creation_time = time.time()

#     # 실행 시간 측정 (리스트 컴프리헨션 사용)
#     add_start_time = time.time()
#     result = [list_a[i] + list_b[i] for i in range(N)]
#     add_end_time = time.time()

#     return {
#         "array_creation_time": end_creation_time - start_creation_time,
#         "addition_time": add_end_time - add_start_time
#         }

# 상수
N = 10**5

@app.get("/add-large-arrays-pandas")
def add_large_arrays():

    start_creation_time = time.time()
    a, b = gen_r_array_choices(N)
    end_creation_time = time.time()
    
    add_start_time = time.time()
    plus_py(a, b)
    add_end_time = time.time()
    
    array_creation_time = end_creation_time - start_creation_time
    addition_time = add_end_time - add_start_time
    return array_creation_time, addition_time

@app.get("/add-large-arrays-numpy")
def add_large_arrays_choices():
    start_creation_time = time.time()
    a,b = gen_r_array_numpy(N)
    end_creation_time = time.time()

    add_start_time = time.time()
    plus_numpy(a, b)
    add_end_time = time.time()
    
    array_creation_time = end_creation_time - start_creation_time
    addition_time = add_end_time - add_start_time
    return array_creation_time, addition_time

def add_arrays(N, fun):
    # 랜덤한 1차원 배열 2개 생성
    start_creation_time = time.time()
    a, b = fun(N)
    end_creation_time = time.time()
    
    # 실행 시간 측정 시작
    add_start_time = time.time()
    # 요소별 덧셈
    result = []
    for x, y in zip(a, b):
        result.append(x + y)
     
    # 실행 시간 측정 종료
    add_end_time = time.time()
    
    # 수행 시간 리턴
    # 리턴값: 배열 생성 시간(array_creation_time)과 덧셈 수행(addition_time) 시간을 각각 리턴
    array_creation_time = end_creation_time - start_creation_time
    addition_time = add_end_time - add_start_time
    return array_creation_time, addition_time

def gen_r_array_choices(N):
    a = random.choices(range(101), k=N)
    b = random.choices(range(101), k=N)
    return a,b

def gen_r_array_numpy(N):
    a = np.random.randint(1, 101, size=N)  # 1 이상 100 이하의 정수
    b = np.random.randint(1, 101, size=N)
    return a,b

def plus_py(a, b):
    result = []
    for x, y in zip(a, b):
        result.append(x + y)
    return result

def plus_numpy(a, b):
    return a + b


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


