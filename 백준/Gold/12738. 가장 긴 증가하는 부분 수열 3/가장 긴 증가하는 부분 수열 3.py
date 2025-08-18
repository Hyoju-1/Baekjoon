import sys
import bisect #정렬된 리스트에서 이진탐색을 쉽게해주는 라이브러리

input = sys.stdin.readline  # 빠른 입력 (N이 최대 1,000,000이므로 필요)
N = int(input().strip())  # 수열 크기
A = list(map(int, input().split()))  # 수열

lis = []  # 가장 긴 증가하는 부분 수열의 후보를 저장할 리스트

for x in A:
    # bisect_left: lis에서 x가 들어갈 가장 왼쪽 위치를 찾음. 이미 같은 값이 있으면, 그 값앞에 삽입할 위치를 반환
    pos = bisect.bisect_left(lis, x)

    # 만약 x가 lis의 모든 원소보다 크면 append
    if pos == len(lis):
        lis.append(x)
    else:
        # 그렇지 않으면 해당 위치의 원소를 x로 교체
        lis[pos] = x

print(len(lis))  # 가장 긴 증가하는 부분 수열의 길이 출력