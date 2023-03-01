import time

water_goal = int(input("how many ounces of water would you like to drink?"))
time_limit = int(input("In how many minutes?"))
water_bottle = int(input("how many oz does your water bottle hold?"))
last_water = int(input("How many ounces of water do you have now?"))
print("When you refill, always refill exactly %i oz" % water_bottle)
start_time = time.time()
last_check = start_time
water_consumed = 0
while (time.time() - start_time)/60 < time_limit and water_consumed < water_goal:
    if time.time() > last_check + 60:
        new_water = int(input("How many ounces now?"))
        last_check = time.time()
        if new_water > last_water: # they refilled
            water_consumed += last_water
            water_consumed += water_bottle - new_water 
            last_water = new_water
        else:
            water_consumed += (last_water - new_water)
            last_water = new_water
        print ("You have consumed %i oz of water." % water_consumed)
if ((time.time() - start_time)/60 >= time_limit):
    print("Time's up.")
print ("You have consumed %i oz of water." % water_consumed)
if water_consumed>water_goal:
    print("You met your goal of %i oz." % water_goal)
else:
    print("You missed your goal of %i oz" % water_goal)
