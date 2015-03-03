class pet:
    number_of_legs = 0
    
    def sleep(self):
        print "zzzz"
        
    def count_legs(self):
        print "I have %s legs." % self.number_of_legs 
        
class  dog(pet):
    def bark(self):
        print "Wufff"
        
doug = dog()
doug.bark()
doug.count_legs()

    