class Person:
    def __init__(self, name):
        self.name = name

    def __dan__(self):
        vowels = ["a", "e", "i", "o", "u"]
        if self.name[0] in vowels:
            return "Dan" + self.name[1:]
        return "Dan" + self.name[1:2] + self.name[2:]


if __name__ == "__main__":
    p = Person("Anthony")
    print(p.__dan__())

if __name__ == "__main__":
    p = Person("Logan")
    print(p.__dan__())

if __name__ == "__main__":
    p = Person("Sarah")
    print(p.__dan__())
