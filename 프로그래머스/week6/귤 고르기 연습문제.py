def solution(k, tangerine):
    d = {}
    for t in tangerine:
        d[t] = d.get(t, 0) + 1
    li = sorted(list(dict.values(d)), reverse=True)
    ans = 0
    while k > 0:
        if li[ans] < k:
            k -= li[ans]
            ans += 1
        else:
            break
    return ans + 1
