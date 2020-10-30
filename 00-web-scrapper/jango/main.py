class Car():

  def __init__(self, *args, **kwargs):
    self.wheels = 4
    self.doors = 4
    self.windows = 4
    self.seats = 4
    self.color = kwargs.get("color","black")
    self.price = kwargs.get("price","$20")


  def __str__(self):
    return f"Car with {self.wheels} wheels"
  # 클래스 안의 함수 : 매서드

class Convertible(Car):

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.time = kwargs.get("time",10 )
  # __init__을 확장 
  # super() : 부모클래스를 의미

  def take_off(self):
    return "taking off"

  def __str__(self):
    return f"Car with no roof"



porche = Convertible(color="green",price="$40")
print(porche)
porche.take_off()
porche.wheels