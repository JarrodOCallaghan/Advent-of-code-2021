import dataset
import datasetTest

a = dataset.main()

starting_state = {}
growth_list = {}
# Part A, set to 80

# Solution for A and B as code is scalable
max_days = 256

# Setup initial data
# Creates a key based on how many days each item has to spawn
for timing in a:
    try:
        starting_state[str(timing)]["Total"] += 1
    except (KeyError):
        starting_state[str(timing)] = {"Total": 1, "Timing": timing}

for day in range(1, max_days + 1):
    # Create empty day
    growth_list[str(day)] = {"Total": 0, "Timing": 8}
    print(f"Day: {day}")
    for item in starting_state:
        print(starting_state[item])
        starting_state[item]["Timing"] -= 1
        if starting_state[item]["Timing"] == -1:
            growth_list[str(day)]["Total"] += starting_state[item]["Total"]
            print(f"Spawning for: {item}")
            starting_state[item]["Timing"] = 6
        # else:
        #    starting_state[item]["Timing"] -= 1
    for item in growth_list:
        print(growth_list[item])
        if item != str(day):
            growth_list[item]["Timing"] -= 1
            if growth_list[item]["Timing"] == -1:
                print(f"Spawning for: {item}")
                growth_list[str(day)]["Total"] += growth_list[item]["Total"]
                growth_list[item]["Timing"] = 6
    # Setting to 8 days as increment was occurring for same day
    # growth_list[str(day)]["Timing"] = 8

    # else:
    #    growth_list[item]["Timing"] -= 1

counter = 0
for key in starting_state:
    counter += starting_state[key]["Total"]
    print(f"{key}:{starting_state[key]}")
for key in growth_list:
    counter += growth_list[key]["Total"]
    print(f"{key}:{growth_list[key]}")


print(f"Final total: {counter}")
