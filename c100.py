
class Car():
    def __init__(self, color, Speed, model, company):
        self.color= color
        self.Speed=Speed
        self.model=model
        self.company=company
    

                        
    def Startthecar(self):
        print("carstarted")

    def stopthecar(self):
        print("carstoped")

car1=Car("blue", "350km/h,", "A6", "Audi")
print(car1.Startthecar())
print(car1.color)

      
    
  

