import time

num_sec = 60

water_goal = int(input("how many ounces of water would you like to drink?"))
time_limit = int(input("In how many minutes?"))
water_bottle = int(input("how many oz does your water bottle hold?"))
last_water = int(input("How many ounces of water do you have now?"))
print("When you refill, always refill exactly %i oz" % water_bottle)
start_time = time.time()
last_check = start_time
water_consumed = 0
while (time.time() - start_time)/num_sec < time_limit and water_consumed < water_goal:
    if time.time() > last_check + 5:
        try:
            new_water = int(input("\nHow many ounces do you have now? "))
            if new_water < 0:
                raise ValueError
        except ValueError:
            print("Invalid value.")
            continue

        last_check = time.time()
        if new_water > last_water: # they refilled
            water_consumed += last_water
            water_consumed += water_bottle - new_water 
            last_water = new_water
        else:
            water_consumed += (last_water - new_water)
            last_water = new_water
        print ("Water goal: %i oz\tWater consumed: %i oz." % (water_goal,water_consumed))
        time_remaining = time_limit - (last_check - start_time)/60
        print ("Time goal: %i min\tTime left:You have %i min." % (time_limit, time_remaining))
        goal_string = "NO"
        if (water_consumed>0 and (time_limit*num_sec)/(last_check - start_time) > water_goal/water_consumed):
            goal_string = "YES"
        print("At this rate will you make your goal?  %s" % goal_string)
        print("Necessary Rate: %i oz/hr\tYour Rate: %i oz/hr." % (water_goal/(time_limit/60), water_consumed/((time_limit-time_remaining)/60)))
        
if ((time.time() - start_time)/num_sec >= time_limit):
    print("Time's up.")
print ("You have consumed %i oz of water." % water_consumed)
if water_consumed>=water_goal:
    print("You met your goal of %i oz." % water_goal)
else:
    print("You missed your goal of %i oz" % water_goal)
