class Super():
    def hello(self):
        print("Hello, I am a Super class")

class Sub(Super):
    def hello(self):
        print("Hello, I am a Sub class")

Super().hello()