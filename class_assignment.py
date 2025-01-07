class Plant:
    def __init__(self, speices, height, colour, fruit):
        self.speices = speices
        self.height = height
        self.colour = colour
        self.fruit = fruit

    def do_something(self):
        print(f'{self.speices}')
        print(f'{self.height}')
        print(f'{self.colour}')
        print(f'{self.fruit}')



p = Plant("oak tree", 35, "green", "acorn")
p.do_something()
