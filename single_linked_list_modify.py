import sys

class employee:
    def __init__(self):
        self.num = 0
        self.salary = 0
        self.name = ""
        self.next = None

def findnode(head, num):
    ptr = head
    while ptr != None:
        if ptr.num == num:
            return ptr
        ptr = ptr.next
    return ptr
def insertnode(head, ptr, num, salary, name):
    InsertNode = employee()
    if not InsertNode:
        return None
    InsertNode.num = num
    InsertNode.salary = salary
    InsertNode.name = name
    InsertNode.next = None
    if ptr == None:
        InsertNode.next = head
        return InsertNode
    else:
        InsertNode.next = ptr.next
        ptr.next = InsertNode
    return head

def del_ptr(head, ptr):
    top = head
    if ptr.num == head.num:
        head = head.next
    else:
        while top.next != ptr:
            top = top.next
        if ptr.next == None:
            top.next = None
        else:
            top.next = ptr.next
    return head

data = [[1001, 32367], [1002, 24388], [1003, 27556], [1007, 31299],
        [1012, 42660], [1014, 25676], [1018, 44145], [1043, 52182],
        [1031, 32769], [1037, 21100], [1041, 32196], [1046, 25776]]
namedata = ["Allen", "scott", "Marry", "John", "Mark", "Ricky",
            "Lisa", "Jasica", "Hanson", "Amy", "Bob", "Jack"]
for i in data:
    print(f"員工編號：{i[0]} 薪水:{i[1]}")

head = employee()
head.next = None

if not head:
    print("Error!_memory failed")
    sys.exit(1)
head.num = data[0][0]
head.name = namedata[0]
head.salary = data[0][1]
head.next = None
ptr = head
for i in range(1,12):
    newnode = employee()
    newnode.next = None
    newnode.num = data[i][0]
    newnode.name = namedata[i]
    newnode.salary = data[i][1]
    ptr.next = newnode
    ptr = ptr.next

position = 0
while True:
    print("""請選擇模式：
    I:插入；D：刪除；E：退出""")
    operation = input()
    if operation == "E":
        break
    elif operation == "I":
        while True:
            print("請輸入要插入的員工編號，若編號不存在則放在串列首，輸入-1退出插入模式")
            position = int(input())
            if position == -1:
                break
            else:
                ptr = findnode(head, position)
                new_num = int(input("員工編號："))
                new_salary = int(input("薪水："))
                new_name = input("員工姓名：")
                head = insertnode(head, ptr, new_num, new_salary, new_name)
    elif operation == "D":
        while True:
            print("請輸入要刪除的員工編號，輸入-1退出刪除模式")
            position = int(input())
            if position == -1:
                break
            else:
                ptr = head
                count = -1
                while ptr != None:
                    if ptr.num == position:
                        ptr = del_ptr(head, ptr)
                        count += 1
                        head = ptr
                    ptr = ptr.next
                if count == -1:
                    print("無該員工編號")

ptr = head
while ptr != None:
    print(f"編號：{ptr.num} 姓名：{ptr.name} 薪水：{ptr.salary}")
    ptr = ptr.next