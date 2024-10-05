class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        deltaY = coordinates[1][1] - coordinates[0][1]
        deltaX = coordinates[1][0] - coordinates[0][0]
        for i in range(2, len(coordinates)):
            x2,y2 = coordinates[i][0], coordinates[i][1]
            x1,y1 = coordinates[i-1][0], coordinates[i-1][1]
            
            rise = y2-y1
            run = x2 - x1
            
            if (deltaY * run) != deltaX * rise: 
                return False
        return True


