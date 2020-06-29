class FileSystem:
    # 18:30 - 18:55
    def __init__(self):
        self.directory = {}

    def ls(self, path: str) -> List[str]:
        path_list = path.split("/")[1:]
        tmp = self.directory
        for dic in path_list:
            if dic == "":
                continue
            tmp = tmp[dic]
        if isinstance(tmp, dict):
            return sorted(list(tmp.keys()))
        return [dic]
        
            

    def mkdir(self, path: str) -> None:
        path_list = path.split("/")[1:]
        tmp = self.directory
        for dic in path_list:
            if not dic in tmp:
                tmp[dic] = {}
            tmp = tmp[dic]

    def addContentToFile(self, filePath: str, content: str) -> None:
        path_list = filePath.split("/")[1:]
        tmp = self.directory
        for dic in path_list[:-1]:
            tmp = tmp[dic]
        tmp[path_list[-1]] = tmp.get(path_list[-1], "") + content

    def readContentFromFile(self, filePath: str) -> str:
        path_list = filePath.split("/")[1:]
        tmp = self.directory
        for dic in path_list[:]:
            tmp = tmp[dic]
        return tmp

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)