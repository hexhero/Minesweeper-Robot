
def get_position(x, y):
    if x < 0 or x >= len(map):
        return 0
    else:
        a = map[x]
        if y < 0 or y >= len(a):
            return 0
        else:
            return a[y]


def cover_position(x, y, _x, _y):
    return _x-1+x, _y-1+y

# 寻找地雷
def find_mines(map):
    bm = []
    for i1, m1 in enumerate(map):
        for i2, m2 in enumerate(m1):
            if m2 != '-' and m2 != '*' and int(m2) > 0:
                window = [
                    [get_position(i1-1, i2-1), get_position(i1-1, i2), get_position(i1-1, i2+1)],
                    [get_position(i1, i2-1), get_position(i1, i2), get_position(i1, i2+1)],
                    [get_position(i1+1, i2-1), get_position(i1+1, i2), get_position(i1+1, i2+1)]
                ]

                boom = []
                for _w1, w1 in enumerate(window):
                    for _w2, w2 in enumerate(w1):
                        if w2 == '-' or w2 == '*':
                            boom.append((_w1, _w2))
                if len(boom) == int(m2):
                    for b in boom:
                        x, y = cover_position(b[0], b[1], i1, i2)
                        bm.append((x, y))

    for b in bm:
        map[b[0]][b[1]] = '*'

    return map

# 标记安全区
def flag(map):
    bm = []
    for i1, m1 in enumerate(map):
        for i2, m2 in enumerate(m1):
            if m2 != '-' and m2 != '*' and int(m2) > 0:
                window = [
                    [get_position(i1-1, i2-1), get_position(i1-1, i2), get_position(i1-1, i2+1)],
                    [get_position(i1, i2-1), get_position(i1, i2), get_position(i1, i2+1)],
                    [get_position(i1+1, i2-1), get_position(i1+1, i2), get_position(i1+1, i2+1)]
                ]

                bom = 0
                for _w1, w1 in enumerate(window):
                    for _w2, w2 in enumerate(w1):
                        if w2 == '*':
                            bom = bom + 1
                if bom != 0 and bom == int(m2):
                    for _w3, w3 in enumerate(window):
                        for _w4, w4 in enumerate(w3):
                            if w4 == '-':
                                x,y = cover_position(_w3, _w4, i1, i2)
                                bm.append((x, y))
    for b in bm:
        map[b[0]][b[1]] = '?'

    return map

if __name__ == '__main__':
    map = [
        ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '8', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '5'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    ]
    find_mines(map)
    flag(map)
    for m in map:
        print(m)

