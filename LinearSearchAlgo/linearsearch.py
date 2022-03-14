car = [1,8,3,5,4,9]
CarNo = int(input("Enter the car no. to search: "))
def mycarsearch_algo(cars, carno):
    for i in list(range(len(cars))):
        if cars[i] == carno:
            print("found at position", i)
            break
       
mycarsearch_algo(car, CarNo)
