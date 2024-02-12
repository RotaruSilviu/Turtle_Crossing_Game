from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
SPEED_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        ### Ascundem testoasa care se creaza in mijlocul ecranului.
        self.hideturtle()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    # Functie ca sa cream masinilie.
    def create_car(self):
        ### IN felul acesta am creat o sansa aleatorie, asa ca e o sansa 1/6 ca sa se faca o masina,
        # astfel aparand mai rar pe ecran.
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.speed(0)
            new_car.setheading(180)
            new_car.goto(300, random.randint(-250, 250))
            self.cars.append(new_car)

    ### Functie ca sa mutam masinile.
    def move_cars(self,):
        for car in self.cars:
            car.forward(self.car_speed)
            ### Aici dispare masina odata ce ajunge la final si e scoasa din lista de masini.
            # Deoarece masinile se regenereaza continuu , lista cu masini nu se termina niciodata.
            if car.xcor() < -300:
                car.hideturtle()
                self.cars.remove(car)

    def level_up(self):
        self.car_speed += SPEED_INCREMENT
