#hieudinh
print("Welcome to the first day of 100 days of code - band name generator")
# initialize the variables to empty string

city = ""
pet = ""

# simpple check to make sure the user enter the name of city and pet

while True:
    city = input("What's name of the city you grew up in?\n")
    if city == "":
        print("Please enter your city")
    else:
        break
while True:
    pet = input("What's your pet's name?\n")
    if pet == "":
        print("Please enter your pet's name")
    else:
        break

print("Your band name could be " + city + " " + pet)
print("Thank you for using the band name generator")

