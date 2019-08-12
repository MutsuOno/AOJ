import sys
input = sys.stdin.readline

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_first(self, key):
        new = Node(key)
        tmp = self.head
        if tmp == None:
            self.head = new
        else:
            tmp.prev = new
            new.next = tmp
            self.head = new
        self.length += 1
    
    # key=keyである最初の要素を削除
    def delete(self, key):
        tmp = self.head
        if tmp.key == key:
            self.head = None
            if tmp.next:
                tmp.next.prev = None
                self.head = tmp.next
            if self.length > 1:
                self.length -= 1
            else:
                self.length = 0
            return
        
        while tmp:
            if tmp.key == key:
                if tmp.prev:
                    tmp.prev.next = tmp.next
                if tmp.next:
                    tmp.next.prev = tmp.prev
                tmp = None
                self.length -= 1
                return
            tmp = tmp.next

    def deleteFirst(self):
        tmp = self.head
        self.head = None
        if self.length > 1:
            tmp.next.prev = None
            self.head = tmp.next
            self.length -= 1
        else:
            self.length = 0

    def deleteLast(self):
        tmp = self.head
        if tmp.next == None:
            self.head = None
            self.length = 0
            return

        while tmp:
            if tmp.next == None:
                tmp.prev.next = None
                tmp = None
                self.length -= 1
                return
            tmp = tmp.next

    def show_all(self):
        tmp = self.head
        for i in range(self.length):
            if i != self.length - 1:
                print(tmp.key, end=" ")
                tmp = tmp.next
            else:
                print(tmp.key)

def main():
    N = int(input())

    d_list = DoublyLinkedList()

    for _ in range(N):
        com_line = input().split()
        com = com_line[0]
        if com == "deleteFirst":
            d_list.deleteFirst()
        elif com == "deleteLast":
            d_list.deleteLast()
        else:
            key = com_line[1]
            if com == "insert":
                d_list.insert_first(key)
            elif com == "delete":
                d_list.delete(key)

    d_list.show_all()
             
if __name__ == "__main__":
    main()