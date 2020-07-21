class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        stack = []
        for folder in path_list:
            if folder == "." or folder == "":
                continue
            elif folder == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(folder)
        return "/" + "/".join(stack)
        