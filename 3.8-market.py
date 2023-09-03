def discount_checker(threshold, *purchases):
    s = []
    for i in range(len(purchases)):
        if purchases[i] > threshold:
            s.append(i+1)
    print(s)
    return s




discount_checker(1000, 500, 1500, 800, 1200)