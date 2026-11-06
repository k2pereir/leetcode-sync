class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        justified = []
        line = []
        length = 0
        i = 0

        while i < len(words):
            # if the line is complete
            if length + len(line) + len(words[i]) > maxWidth:
                spaces = maxWidth - length
                space = spaces // max(1, len(line) - 1)
                rem = spaces % max(1, len(line) - 1)
                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * space
                    if rem:
                        line[j] += " "
                        rem -= 1
                justified.append("".join(line))
                line = []
                length = 0
            line.append(words[i])
            length += len(words[i])
            i += 1
        # need to add the last line
        last_line = " ".join(line)
        trailing = maxWidth - len(last_line)
        last_line += " " * trailing
        justified.append(last_line)
        return justified
