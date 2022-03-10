car = [1,8,3,5,4,9]
CarNo = int(input("Enter the car no. to search: "))
def mycarsearch_algo(cars, carno):
    for i in cars:
        if i == carno:
            print("found")
            break
        else:
            print("notfound")
mycarsearch_algo(car, CarNo)
