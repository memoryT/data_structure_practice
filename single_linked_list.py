class Student:
    def __init__(self):
        self.name=""
        self.score=0
        self.next=None

head = Student()
head.next = None
ptr = head
select = 0
while select != 2:
    print("(1)新增 (2)離開 =>")
    try:
        select = int(input("請輸入一個選項:"))
    except ValueError:
        print("輸入錯誤\n請重新輸入\n")
    if select == 1:
        new_data = Student()
        new_data.name = input("姓名")
        new_data.no = input("學號")
        new_data.Math = float(input("數學成績"))
        ptr.next = new_data
        new_data.next = None
        ptr = ptr.next
ptr = head.next
while ptr != None:
    print(ptr.name, ptr.no, ptr.Math)
    ptr = ptr.next