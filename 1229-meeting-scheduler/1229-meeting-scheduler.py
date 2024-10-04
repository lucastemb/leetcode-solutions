class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        pointer1 = pointer2 = 0
        while pointer1 < len(slots1) and pointer2 < len(slots2):
            intersection_right=min(slots1[pointer1][1], slots2[pointer2][1])
            intersection_left=max(slots1[pointer1][0], slots2[pointer2][0])
            if intersection_right - intersection_left >= duration: 
                return [intersection_left, intersection_left + duration]
            
            if slots1[pointer1][1] < slots2[pointer2][1]:
                pointer1+=1
            else:
                pointer2+=1
       
        return []