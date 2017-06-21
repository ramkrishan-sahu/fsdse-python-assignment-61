# x = [1, 2, 3, 4, 9, 10, 20, 30, 40, 1, 2, -8, -2, 0, 2, 3, 5, 8, 13, 21, 34]
x = [1, 2, 3, 5, 8, 9]

def solution(lis):
    dic = {"ODD": 0, "EVEN": 0}
    for i in range(0, len(lis)):
        if (lis[i]%2 == 0):
            dic["EVEN"] = dic["EVEN"] +1
        else:
            dic["ODD"] = dic["ODD"] +1
    return dic

solution(x)
