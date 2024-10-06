class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words={}
        new_paragraph = ''.join([c.lower() if c.isalnum() else  ' ' for c in paragraph])
        for word in new_paragraph.split():
            word = word.lower()
            if word not in banned:
                words[word] = words.get(word, 0)+1
        return sorted(words.items(), key=lambda x: x[1], reverse=True)[0][0]