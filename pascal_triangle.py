import copy
def pascal(num):
    res = []
    current = [1]
    print(current)
    for _ in range(1,num+1):
        current.append(1)
        print(current)
        res.append(1)
        [res.append(current[i]+current[i+1]) for i in range(len(current)-1)]
        current = res.copy()
        res = []
pascal(int(input()))
