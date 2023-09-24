class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res=[] #array that will contain the strings
        line, length= [], 0 #the number of characters belonging to words
        i=0
        while i < len(words):
            if length + len(line) + len(words[i]) > maxWidth:
                extra_space = maxWidth - length
                
                spaces = extra_space // max(1,len(line)-1)
                remainder = extra_space % max(1, len(line)-1)

                for j in range(max(1, len(line)-1)):
                    line[j] += " " * spaces
                    if remainder: 
                        line[j] += " "
                        remainder -= 1
                res.append("".join(line))
                line, length = [], 0
            line.append(words[i])
            length += len(words[i])
            i+=1
        last_line = " ".join(line)
        trail_space = maxWidth - len(last_line)
        res.append(last_line + " " * trail_space)

        return res

   #O(N) time
    #O(N) space if you count the solution as part of the space complexity