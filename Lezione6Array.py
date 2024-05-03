def visit_tree(tree: dict[int, list[int]], node: int):
    print(node)
    left_child, right_child = tree.get(node, [None,None])
    if left_child:
        visit_tree(tree, left_child)
    if right_child:
        visit_tree(tree, right_child)


tree = {4: [3,5], 3: [2,None], 5:[4.5,6], 2:[None,None], 4.5:[None,None], 6:[None,None]}
visit_tree(tree, 4)



'''
def __binary_search_recursive(array: list[int], x:int, low:int, high:int) -> int:
    return __binary_search_recursive(array, x, )

def __binary_search_recursive(array: list[int], x:int, low:int, high:int) -> int:
    if low > high:
        return None

    mid = (low + high) // 2
    if x == array[mid]:
        return mid
    elif x > array[mid]:
        return __binary_search_recursive(array, x, mid + 1, high)
    else:
        return __binary_search_recursive(array, x, low, mid - 1)
'''