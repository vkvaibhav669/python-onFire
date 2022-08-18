if __name__ == '__main__': 
    d = {}    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        d[name] = score
    v = d.values()
    second = sorted(list(set(v)))[1]
    second_lowest = []
    for key,value in d.items():
        if value==second:
            second_lowest.append(key)
    second_lowest.sort()
    for name in second_lowest:
        print(name)
            