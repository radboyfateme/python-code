from collections import UserString

class MyString(UserString):
    def reverse(self):
        return self.data[::-1]

    def insert(self, index, substr):
        return self.data[:index] + substr + self.data[index:]


my_str1 = MyString("Hello")
my_str2 = MyString("Python")


print("Original:", my_str1)
print("Reversed:", my_str1.reverse())
print("After Insert:", my_str1.insert(2, "XX"))

print("Original:", my_str2)
print("Reversed:", my_str2.reverse())
print("After Insert:", my_str2.insert(3, "YY"))

