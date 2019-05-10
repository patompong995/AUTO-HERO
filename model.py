import arcade.key
from PIL import Image
from random import randint
list_hero=[]
class Model:
    def __init__(self,world,x,y,cost,specy,image):
        self.x=x
        self.y=y
        self.cost = cost
        self.specy=specy
        self.image=image
class Box(Model):
    def __init__(self,world,cost,specy,image):
        super().__init__(world,cost,specy,image)
        self.x=x
        self.y=y
        self.cost = cost
        self.specy=specy
        self.image=image

    def tranform(self):
        None

class Cursor(Model):
    def __init__(self,world,x,y,cost,specy,image):
        super().__init__(world,cost,specy)
        self.world=world
        self.x=x
        self.y=y
        self.cost=0
        self.specy=0
        self.image=Image.open("cursor.png")
        
class Hero(Model):
    def __init__(self,world,cost,specy,image):
        super().__init__(world,cost,specy,image)
        self.cost = cost
        self.specy=specy
        self.image=Image

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.box = Box
        
list_hero.append(Hero(1,1,Image.open("1.png")))
list_hero.append(Hero(2,1,Image.open("2.png")))
list_hero.append(Hero(3,1,Image.open("3.png")))
list_hero.append(Hero(4,1,Image.open("4.png")))
list_hero.append(Hero(1,2,Image.open("5.jpg")))
list_hero.append(Hero(2,2,Image.open("6.png")))
list_hero.append(Hero(3,2,Image.open("7.png")))
list_hero.append(Hero(4,2,Image.open("8.jpg")))