def solve1(a, b, c):
    if a == 0:
        return 'y = '+str(-c/b)+'\nx = 0'
    if b == 0:
        return 'x = '+str(-c/a)+'\ny = 0'
    return 'x = ('+str(-c)+'-'+str(b)+'y)/'+str(a)+'\ny = ('+str(-c)+str(-a)+'x)/'+str(b)

print solve1(3,1,2)