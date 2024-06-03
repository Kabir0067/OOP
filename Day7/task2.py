class Computer:
    def __init__(self, brand, os):
        self.brand = brand
        self.__os = os
    
    def install_os(self, os):
        self.__os = os
        print(f"{os} Dar compyteri {self.brand} nasb sudaast.")

my_computer = Computer("HP", "Windows 10")
my_computer.install_os("Linux")