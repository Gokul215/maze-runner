from maze import maze

triggers=[(1,2),(3,2)]
ma=maze(6,6,triggers)
ma.puttreasure(5,4)
ma.putmonster(0,2)
ma.putmonster(1,2)
ma.putmonster(2,2)
ma.putmonster(3,2)
ma.putmonster(4,2)
ma.putmonster(5,2)

ma.printmaze()
short=ma.shortestpath(5,1)
print("The shortest path is",short)