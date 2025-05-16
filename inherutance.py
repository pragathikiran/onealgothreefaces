
class Person(object):

    
    
    def __init__(self,name,idnumber):
      self.name = name
      self.idnumber = idnumber
    
    def display(self):
       print(self.name )
       print(self.idnumber)

class employee(Person):
   def __init__(self,name,idnumber,salary,post):
        self.salary = salary
        self.post = post
        Person.__init__(self,name,idnumber)

a = employee('PRAGATHI',90901234,9000000,"CEO")
b = employee('RIYA',90901233,8000000,"MANAGER")
c = employee('TANVI',90901232,7000000,"TEAN LEAD")

a.display()
b.display()
c.display()



   

    