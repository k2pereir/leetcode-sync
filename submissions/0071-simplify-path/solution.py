class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = [item for item in path.split('/') if item]
        print(split_path)
        simplified = []
        for item in split_path:
            if item == ".":
                continue
            elif item == "..":
                if simplified:
                    simplified.pop()
            else:
                simplified.append(item)
        return "/" + "/".join(simplified)
