class Solution:
    def simplifyPath(self, path: str) -> str:

        path = path.split("/")
        stack = []

        for p in path:
            if p == "" or p == " " or p == ".":
                continue
            if p == "..":
                if len(stack):
                    stack.pop()
                continue
            stack.append(p)
        print(stack)
        out= "/" + "/".join(stack)
        return out
    