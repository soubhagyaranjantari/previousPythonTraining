class one:
    def on(self):
        print(f'is a')


class two(one):
    def on(self):
        print('Hello')

class three(two):
    def on(self):
        one.on(self)
        two.on(self)
        print('hy')

a=three()
a.on()