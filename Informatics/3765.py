countries = {}
c = int(input())
for _ in range(c):
    country, *cities = input().split()
    countries[country] = frozenset(cities)

c = int(input())
for _ in range(c):
    city = input().strip()
    for k, v in countries.items():
        if city in v: 
            print(k)
            break
