class Car:
    def __init__(self):
        # A dictionary to map the type of car and price per day
        self.carFare = {'Hatchback': 30, 'Sedan': 50, 'SUV': 100}

    def displayFareDetails(self):
        print("Cost per day: ")
        print("Hatchback: $",self.carFare['Hatchback'])
        print("Sedan: $", self.carFare['Sedan'])
        print("SUV: $", self.carFare['SUV'])

    def calculateFare(self, typeOfCar, numberOfDays):
        # Calculate the fare depending upon the type of car and number of days as requested by the user
        return self.carFare[typeOfCar] * numberOfDays


car = Car()
while True:
    print("Enter 1 to display the fare details")
    print("Enter 2 to rent a car")
    print("Enter 3 to exit")
    userChoice = (int(input()))
    if userChoice is 1:
        car.displayFareDetails()
    elif userChoice is 2:
        print("Enter the type of car you would like to borrow")
        typeOfCar = input()
        print("Enter the number of days you would like to borrow the car")
        numberOfDays = int(input())
        fare = car.calculateFare(typeOfCar, numberOfDays)
        print("Total payable amount: $",fare)
        print("Thank you!")
    elif userChoice is 3:
        quit()
