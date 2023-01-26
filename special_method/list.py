class MyList:
    """
    클래스 설명
    - append 구현
    - pop 구현
    - 더하기 연산 가능(__add__)
    - 인덱스와 슬라이스 가능(__getitem__)
    - 수정 가능함(__setitem__)
    - 출력시 [1, 2, 3] 형태로 보임.(__str__)
    - 반복 가능
    """

    def __init__(self, array=None):
        self.array = array if array is not None else []

    def append(self, value):
        self.array.append(value)

    def pop(self):
        return self.array.pop()

    def __add__(self, other):
        return MyList(self.array + other.array)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return self.array[key.start : key.stop : key.step]
        return self.array[key]

    def __setitem__(self, key, value):
        self.array[key] = value

    def __str__(self):
        return str(self.array)


# class Test
my_list = MyList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
print("my_list", my_list)  # [1, 2, 3]
print(my_list.pop())  # 3
print(my_list)  # [1, 2]

my_list.append(4)
my_list.append(5)

my_list2 = MyList()
my_list2.append("a")
my_list2.append("b")

my_list3 = my_list + my_list2
print(my_list3)  # [1, 2, 4, 5, 'a', 'b']
print(my_list3[-1])  # 'b'
print(my_list3[3:5])  # [5, 'a']

for i in my_list3:
    print(i, end="")
