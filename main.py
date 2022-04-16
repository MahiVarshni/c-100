""" 
OBJECT ORIENTED PROGRAMMING - OOP

Object - properties & functions

Class - group of functions that defines an object - DESIGN/BLUEPRINT


class Student {
    constructor(name, age, gender, level){
        this.name = name
    }
}

john = new Student()

 """

class Chair(object):
    def __init__(self,height,width,material,color):
        self.height=height
        self.width=width
        self.color=color
        self.material=material
    
    def change_color(self,new_color):
        self.color=new_color
        print("the color has been changed to "+self.color)
    
    def renew_cushion(self):
        print("the cushion has been renewed")
    

chair1=Chair(5,3,"wood","brown")
chair2=Chair(5,3,"plastic","black")
chair1.renew_cushion()
chair2.change_color("blue")
