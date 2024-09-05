def jing(matrix):
    n = len(matrix)
    m = len(matrix[0])
    minx = 0
    miny = 0
    maxy = n - 1
    maxx = m - 1
    a = (n * m + 1) % 2
    count = 0
    while True:
        #down
        minx += 1
        count+=1
        if minx == maxx:

            return matrix[maxy - a][minx-1]
        #right
        maxy -= 1
        count+=1
        if miny == maxy:

            return matrix[maxy + 1][maxx - a]
        #up
        maxx -= 1
        count+=1
        if minx == maxx:

            return matrix[miny + a][maxx + 1]
        #left
        miny += 1
        count+=1
        if miny == maxy:
            return matrix[miny - 1][minx + a]
print(jing([[1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15]]))