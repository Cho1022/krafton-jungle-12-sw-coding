# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914
def hanoi(n, start, end, assistant):
    # 원판이 1개일 때는 시작 기둥에서 목표 기둥으로 바로 이동
    if n == 1:
        print(f"원판 1: {start} -> {end}")
        return

    # 1단계: 맨 아래 원판을 제외한 n-1개를 보조 기둥으로 이동
    hanoi(n - 1, start, assistant, end)

    # 2단계: 맨 아래 원판을 목표 기둥으로 이동
    print(f"원판 {n}: {start} -> {end}")

    # 3단계: 보조 기둥에 있던 n-1개를 목표 기둥으로 이동
    hanoi(n - 1, assistant, end, start)

# 실행 예시 (원판 3개)
n = 3
print(f"총 이동 횟수: {2**n - 1}")
hanoi(n, 'A', 'C', 'B')