def domain_name(url):
    url = url.replace('http://', '')
    url = url.replace('https://', '')
    url = url.replace('www.', '')
    point = url.find('.')
    return url[0:point]


def int32_to_ip(int32):
    a1=int32//(256**3)
    a2=(int32%(256**3))//(256**2)
    a3=(int32%(256**2))//256
    a4=(int32%256)
    return f'{a1}.{a2}.{a3}.{a4}'


def zeros(n): 
    count_zero = 0
    while n:
        n = n // 5
        count_zero += n
    return count_zero


def bananas(s):
    result = set()
    def f(string, m, n):
        if n > 5:
            result.add(string + '-'*(len(s)-m))
        elif m < len(s):
            for i in range(m, len(s)):
                if s[i] == 'banana'[n]:
                    f(string+'-'*(i-m)+s[i], i+1, n+1)
        return
    f('', 0, 0)
    return result


def count_find_num(primesL, limit):
    t = eval('*'.join(map(str, primesL)))
    if t > limit:
        return []

    result = [t]
    for i in primesL:
        for n in result:
            num = n * i
            while (num <= limit) and (num not in result):
                result.append(num)
                num *= i

    return [len(result), max(result)]
