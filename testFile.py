from Car import Car
from CarInventoryNode import CarInventoryNode
from CarInventory import CarInventory

def test_Car():
    c = Car("Honda", "CRV", 2007, 8000)
    assert str(c) =="Make: HONDA, Model: CRV, Year: 2007, Price: $8000"

def test_CarInventory():
    bst = CarInventory()

    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    assert bst.getBestCar("Nissan", "Leaf") == car1
    assert bst.getBestCar("Mercedes", "Sprinter") == car3
    assert bst.getBestCar("Honda", "Accord") == None

    assert bst.getWorstCar("Nissan", "Leaf") == car1
    assert bst.getWorstCar("Mercedes", "Sprinter") == car4
    assert bst.getBestCar("Honda", "Accord") == None

    assert bst.getTotalInventoryPrice() == 158000

def test_remove():
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    bst.removeCar("BMW", "X5", 2020, 58000)
    assert bst.inOrder() == "Make: AUDI, Model: A3, Year: 2021, Price: $25000\nMake: BMW, Model: X5, Year: 2022, Price: $60000\nMake: MAZDA, Model: CX-5, Year: 2022, Price: $25000\nMake: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n"
