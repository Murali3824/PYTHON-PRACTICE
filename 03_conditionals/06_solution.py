# 6. Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance
# (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

distance = int(input("enter your transportation distance"))

if distance < 3 :
    print("go for a walk")
elif distance < 15 :
    print("go on a bike")
elif distance > 15 :
    print("go on a car")
    