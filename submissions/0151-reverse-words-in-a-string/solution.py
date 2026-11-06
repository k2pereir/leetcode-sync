class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.strip().split()
        print(s_list)
        s_list.reverse()
        return " ".join(s_list)
