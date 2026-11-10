class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        indices = []
        if not s or not words:
            return indices
        
        wlen = len(words[0])
        word_count = Counter(words)

        for i in range(wlen):
            left = i
            right = i
            seen = defaultdict(int)
            used = 0

            while right + wlen <= len(s):
                word = s[right:right+wlen]
                right += wlen

                if word in word_count:
                    seen[word] += 1
                    used += 1

                    while seen[word] > word_count[word]:
                        leftmost = s[left:left+wlen]
                        seen[leftmost] -= 1
                        if seen[leftmost] == 0:
                            del seen[leftmost]
                        used -= 1
                        left += wlen
                    
                    if used == len(words):
                        indices.append(left)
                else:
                    seen.clear()
                    used = 0
                    left = right
        return indices

