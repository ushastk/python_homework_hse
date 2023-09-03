weather_now = input()
p = float(input())
q = float(input())
day = int(input())
res = 1
for i in range(day):
    if weather_now == 'ясно':
        weather = {p: 'ясно', 1-p : 'пасмурно'}
        local_max = max(weather)
        res *= local_max
        weather_now = weather.get(local_max) # значение по максимальному ключу

    elif weather_now == 'пасмурно':
        weather = {1-q : 'ясно', q : 'пасмурно'}
        local_max = max(weather)
        res *= local_max
        weather_now = weather.get(local_max)  # значение по максимальному ключу

print(weather_now, res, sep='\n')