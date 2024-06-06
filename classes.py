class animal:
    def __init__(self):
        print('there are many animals')
    
class lion(animal):
    def __init__(self):
        print('lion roars')
        animal.__init__(self=lion)
obj1=lion()
        
        