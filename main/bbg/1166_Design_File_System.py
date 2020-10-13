class FileSystem:

    def __init__(self): 
        self.path_map = {"":{}} #{folder: next_folder/value}

    def createPath(self, path: str, value: int) -> bool:
        path_list = path.split("/") # ["leet"]
        current_layer = self.path_map
        for folder in path_list[:-1]:
            current_layer = current_layer.get(folder)
            if current_layer is None:
                return False
        if current_layer.get(path_list[-1]) is None:
            current_layer[path_list[-1]] = {"__value": value}
            return True
        return False

    def get(self, path: str) -> int:
        path_list = path.split("/")
        current_layer = self.path_map
        for folder in path_list:
            current_layer = current_layer.get(folder)
            if current_layer is None:
                return -1
        else:
            return current_layer["__value"]
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)