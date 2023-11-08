class Dog:
    def __init__(self):
        self.angry = False
        self.score = 10
        def __str__(self):
            return self.name + ' ' + str(self.score)
dog = Dog()
Dog.__str__(dog)
