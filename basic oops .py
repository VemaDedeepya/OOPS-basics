class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print('Name: ' , self.name)
        print('Marks: ' , self.marks)
        
    def grade(self):
        
        if self.marks >= 90:
            grade = 'A'
        
        elif self.marks >= 75:
            grade = 'B'
            
        elif self.marks >= 50:
            grade = 'C'
            
        else:
            grade = 'F'
            
        return grade    
        
s1 = Student('a' , 56 )        
s2 = Student('b', 48)

s1.display()
print('Grade : ', s1.grade())    
s2.display()
print('Grade : ', s2.grade())    




'''

class Car:  
    def __init__(self,colour,milage):
        self.colour = colour
        self.milage = milage
        
    def __str__(self):
        return f"the {self.colour} has {self.milage} miles"
  
        
c1 = Car('blue', 20000)
c2 = Car('red', 30000)
   
for car in (c1,c2):
       print(car)
    


'''