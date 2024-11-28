from collections import deque
from pathnode import pathnode

class maze:
      #(row,col,steps)
    def __init__(self,row,col,triggers) -> None:
        self.mazerow=row
        self.mazecol=col
        self.triggers=triggers
        self.mazeboard=[[0]*col for i in range(row)]
        
        
    def printmaze(self):
        for i in range(self.mazerow):
            for j in range(self.mazecol):
                print(self.mazeboard[i][j],end='  ')
            print()
        
    def puttreasure(self,row,col):
        if row>self.mazerow or row <0 or col>self.mazecol or col<0: return False
        self.mazeboard[row][col]='T'
    
    def putmonster(self,row,col):
        if row>self.mazerow or row <0 or col>self.mazecol or col<0: return False
        self.mazeboard[row][col]='M'
        
    def istriggere(self,row,col):
        # print(self.triggers)
        for r,c in self.triggers:
            if row==r and col==c:
                # print(trigger[0],row,trigger[1],col)
                
                return True
        return False 
    def printpathamze(self,lastpath):
        cur=lastpath
        while cur:
            r,c=cur.row,cur.col 
            if self.mazeboard[r][c]!='A' and self.mazeboard !='T':
                self.mazeboard[r][c]='P'
            cur=cur.previous
        print("path to treasure from adventure")
        self.printmaze()
        
    def shortestpath(self,row,col):
        if row>len(self.mazeboard)-1 or row <0 or col>len(self.mazeboard[0])-1 or col<0: return False
        self.mazeboard[row][col]='A'
        visited=[[False]*(self.mazecol) for i in range(self.mazerow)]
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        mpath=deque()
        path=pathnode(row,col,0,None)
        mpath.append(path)
        visited[row][col]=True
        while len(mpath)>=1:
            # print(len(mpath))
            lastpath= mpath.popleft()
        
            # print(r)
            for dr,dc in directions:
                # print(r)
                r=lastpath.row+dr
                c=lastpath.col+dc
                # print(r,c)
                # print(self.mazeboard[r][c] =='M')
                if (r<(self.mazerow) and r >=0 and c<(self.mazecol) and c>=0 and not visited[r][c] and ( (self.mazeboard[r][c] =='M' and self.istriggere(r,c)) or self.mazeboard[r][c] !='M')) : 
                    # print(self.istriggere(row,col))
                    if  self.mazeboard[r][c] == "T"  :
                        self.printpathamze(lastpath)
                        return lastpath.steps+1
                        
                    # elif  self.mazeboard[r][c] !='M' or(self.mazeboard[r][c] =='M' and self.istriggere(row,col)) :
                    
                    newpath=pathnode(r,c,lastpath.steps+1,lastpath)
                    visited[r][c]=True
                
                    mpath.append(newpath)
    
                        
        return -1
        
    # def shortestpath(self,row,col):
    #     if row>len(self.mazeboard)-1 or row <0 or col>len(self.mazeboard[0])-1 or col<0: return False
    #     self.mazeboard[row][col]='A'
    #     path=set()
    #     r=float("inf")
    #     def short(r,c,s):
    #         if r<0 or r>=len(self.mazeboard) or c<0 or c>=len(self.mazeboard)  or (r,c) in path:
    #             return s
    #         if  self.mazeboard[row][col]=='M':
    #             return 0
    #         if self.mazeboard[r][c]=='T':
    #             return s+1
    #         print((r,c))
    #         path.add((r,c))
            
    #         right=short(r,c+1,s+1) 
    #         left=short(r,c-1,s+1) 
    #         bot=short(r+1,c,s+1) 
    #         top=short(r-1,c,s+1) 
    #         res=min(left,right,top,bot) 
    #         path.remove((r,c))
            
    #         r=min(res,r)
    #         return r
            
    #     return short(row,col,0)
    # def shortestpath(self, row, col):
    #     if row >= len(self.mazeboard) or row < 0 or col >= len(self.mazeboard[0]) or col < 0:
    #         return False

    #     # Mark the starting position on the maze
    #     self.mazeboard[row][col] = 'A'
        
    #     # Initialize visited grid
    #     visited = [[False] * len(self.mazeboard[0]) for _ in range(len(self.mazeboard))]
        
    #     # Possible movement directions (up, down, left, right)
    #     directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
    #     # Initialize queue for BFS
    #     mpath = deque()
    #     path = pathnode(row, col, 0)
    #     mpath.append(path)
    #     visited[row][col] = True
        
    #     while mpath:
    #         lastpath = mpath.popleft()
            
    #         for dr, dc in directions:
    #             r, c = lastpath.row + dr, lastpath.col + dc
                
    #             # Check if the position is within bounds and not visited
    #             if 0 <= r < self.mazerow and 0 <= c < self.mazecol and not visited[r][c]:
    #                 # Check if we've reached the target without hitting an obstacle
    #                 if self.mazeboard[r][c] == "T":
    #                     return lastpath.steps + 1
    #                 elif self.mazeboard[r][c] != "M":
    #                     # Continue exploring this path
    #                     newpath = pathnode(r, c, lastpath.steps + 1)
    #                     visited[r][c] = True
    #                     mpath.append(newpath)
        
    #     # Return -1 if no path is found
    #     return -1
    
    
        
                    
                
        
        