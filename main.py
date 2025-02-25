from typing import Union

from fastapi import FastAPI

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

    result = [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

    return {"result": result}

from fastapi import FastAPI
import time
import random

@app.get("/add-large-arrays")
def add_large_arrays():
    N = 10**6  # 100만 개 요소

    # Python 리스트로 랜덤한 1차원 배열 생성
    list_a = [random.randint(0, 100) for _ in range(N)]
    list_b = [random.randint(0, 100) for _ in range(N)]

    # 실행 시간 측정 (리스트 컴프리헨션 사용)
    start_time = time.time()
    result1 = [list_a[i] + list_b[i] for i in range(N)]
    
    end_time = time.time()

    return {"execution_time": end_time - start_time}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
