# 2018 카카오 블라인드 캐시
def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        return len(cities) * 5
    for i in range(len(cities)):
        cities[i] = cities[i].upper()
    for city in cities:
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            if len(cache) <cacheSize:
                cache.append(city)
            elif len(cache) >= cacheSize:
                cache = cache[1:]
                cache.append(city)
            answer += 5
    return answer
