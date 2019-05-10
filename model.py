import arcade.key
from PIL import Image
from random import randint
list_hero=[]
class Model:
    def __init__(self,x,y,cost,specy,image):
        self.x=x
        self.y=y
        self.cost = cost
        self.specy=specy
        self.image=image
class Box(Model):
    def __init__(self,cost,specy,image):
        super().__init__(self,cost,specy,image)
        self.x=x
        self.y=y
        self.cost = cost
        self.specy=specy
        self.image=image
        
class Hero(Model):
    def __init__(self,cost,specy,image):
        super().__init__(self,cost,specy,image)
        self.cost = cost
        self.specy=specy
        self.image=image

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.ship = Ship(self,100, 100)
        self.gold = Gold(self, 400, 400)

list_hero.append(Hero(1,1,Image.open("1.png")))
list_hero.append(Hero(2,1,Image.open("2.png")))
list_hero.append(Hero(3,1,Image.open("3.png")))
list_hero.append(Hero(4,1,Image.open("4.png")))
list_hero.append(Hero(1,2,Image.open("5.jpg")))
list_hero.append(Hero(2,2,Image.open("6.png")))
list_hero.append(Hero(3,2,Image.open("7.png")))
list_hero.append(Hero(4,2,Image.open("8.jpg")))