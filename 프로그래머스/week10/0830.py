def solution(line):
    meet = set()
    max_x, max_y = -float('inf'), -float('inf')
    min_x, min_y = float('inf'), float('inf')
    
    for i in range(len(line)):
        a, b, e = line[i]
        for j in range(i + 1, len(line)):
            c, d, f = line[j]
            if ((a * d) - (b * c)) != 0:
                x = ((b * f) - (e * d)) / ((a * d) - (b * c))
                y = ((e * c) - (a * f)) / ((a * d) - (b * c))
                if x.is_integer() and y.is_integer():
                    meet.add((int(x), int(y)))
                    max_x, max_y = max(max_x, int(x)), max(max_y, int(y))
                    min_x, min_y = min(min_x, int(x)), min(min_y, int(y))
    
    meet = sorted(list(meet), key=lambda x:-x[1])
    width = abs(max_x - min_x) + 1
    height = abs(max_y - min_y) + 1
    
    answer = [["."] * width for _ in range(height)]
    
    for x, y in meet:
        idx_y = max_y - y
        idx_x = x - min_x
        answer[idx_y][idx_x] = "*"
    
    
    return list(map("".join, answer))