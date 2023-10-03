class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y=0,0
        dx,dy=0,1
        '''
         N = 0,1
         E = 1,0
         S = 0,-1
         ^
         |
        (.). (.) dy=-1 dx=0
              |
              x
        '''
        for struct in instructions: 
            if struct=="G":
                x+=dx
                y+=dy
            elif struct=="L":
                if dy == 0:
                    temp=dy
                    dy=dx
                    dx=temp
                else:
                    temp=dy
                    dy=-dx
                    dx=-temp
            else: 
                if dx == 0:
                    temp=dy
                    dy=dx
                    dx=temp
                else:
                    temp=dy
                    dy=-dx
                    dx=-temp
        return (x,y)==(0,0) or (dx,dy) != (0,1)
            
