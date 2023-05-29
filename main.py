class Parent:
    def parent(self):
        print("Fruits:")

class Child:
    def child(self):
        print("Apple, peach, banana, apricot…")

class Food(Child, Parent):
    pass

fruits = Food()
fruits.parent()
fruits.child()