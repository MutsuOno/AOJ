import sys
input = sys.stdin.readline

NEXT = 2
DATA = 1
PREV = 0

def dll_processor(operations):

    front = None
    end = None

    for o in operations:
        if o[0] == "insert":
            front, end = insert(front, end, o[1])
        elif o[0] == "delete":
            front, end = delete(front, end, o[1])
        elif o[0] == "deleteFirst":
            front, end = delete_first(front, end)
        elif o[0] == "deleteLast":
            front, end = delete_last(front, end)

    return get_list(front)

def get_list(front):
    if not front:
        return []

    l = []
    target = front
    while True:
        l.append(target[DATA])
        if not target[NEXT]:
            break
        target = target[NEXT]
    return l

def insert(front, end, target):
    node = [None, target, None]
    if front:
        front[PREV] = node
        node[NEXT] = front
        return node, end
    else:
        return node, node

def delete(front, end, target):

    delete_node = front
    while not delete_node[DATA] == target:
        delete_node = delete_node[NEXT]
        if delete_node == None:
            return front, end

    if delete_node[PREV] == None:
        delete_node[NEXT][PREV] = None
        return delete_node[NEXT], end
    elif delete_node[NEXT] == None:
        delete_node[PREV][NEXT] = None
        return front, delete_node[PREV]
    else:
        delete_node[NEXT][PREV] = delete_node[PREV]
        delete_node[PREV][NEXT] = delete_node[NEXT]
        return front, end

def delete_last(front, end):

    if not end[PREV]:
        return None, None
    else:
        end[PREV][NEXT] = None
        return front, end[PREV]

def delete_first(front, end):

    if not front[NEXT]:
        return None, None
    else:
        front[NEXT][PREV] = None
        return front[NEXT], end

def main():
    n_list = int(input())
    target_list = [input().split() for i in range(n_list)]
    print(*dll_processor(target_list))

if __name__ == "__main__":
    main()