class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_of_occurrences = {}
        frequencies = set()

        #add to num_of_occurrences
        for num in arr: 
            num_of_occurrences[num] = num_of_occurrences.get(num, 0)+1 
        
        for n, f in num_of_occurrences.items(): 
            print(n, f)
            if f in frequencies: 
                return False
            frequencies.add(f)
        
        #time: O(N)
        #space: O(N)
        return True
