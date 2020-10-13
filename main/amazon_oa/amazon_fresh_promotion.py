def promotion(codeList, shoppingCart):
    # greedy
    def eqal(list1, list2):
        for i in range(len(list1)):
            if list1[i] != list2[i] and list2[i] != "anything":
                return False
        return True

    code_idx, fruit_idx = 0, 0
    while code_idx < len(codeList) and fruit_idx + len(codeList[code_idx]) <= len(shoppingCart):
        if eqal(shoppingCart[fruit_idx:fruit_idx + len(codeList[code_idx])], codeList[code_idx]):
            fruit_idx += len(codeList[code_idx])
            code_idx += 1
        else:
            fruit_idx += 1
    if code_idx == len(codeList):
        return 1
    else: 
        return 0
#codeList, shoppingCart, ans = [["apple", "apple"], ["banana", "anything", "banana"]], ["orange", "apple", "apple", "banana", "orange", "banana"], 1
#codeList, shoppingCart, ans = [["apple", "apple"], ["banana", "anything", "banana"]], ["banana", "orange", "banana", "apple", "apple"], 0
#codeList, shoppingCart, ans = [["apple", "apple"], ["banana", "anything", "banana"]], ["apple", "banana", "apple", "banana", "orange", "banana"], 0
codeList, shoppingCart, ans = [["apple", "apple"], ["apple", "apple", "banana"]], ["apple", "apple", "apple", "banana"], 0
print(promotion(codeList, shoppingCart) == ans)

