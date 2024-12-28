def solution(arr, queries):
    for i in range(len(queries)):
        a = queries[i][0]
        b = queries[i][1]
        arr[a],arr[b] = arr[b],arr[a]
    return arr