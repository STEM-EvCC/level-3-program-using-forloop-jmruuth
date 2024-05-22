# FOR LOOPS
mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13'] 
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970] 
mission_success = [True, False, True, True, True, True, False] 

# Count the totals for missions and mission success.
total_missions = len(mission_names)
total_success = sum(mission_success)

# Calculate the success rate of the missions
success_rate = (total_success / total_missions) * 100

# Identify and list all missions launched before the 2000.
missions_pre2000 = [mission_names[i] for i in range (total_missions) if mission_years[i] < 2000]

# Print the total number of missions and successful missions. 
print("Total number of Space Missions:", total_missions)
print("Total number of Successful Missions:", total_success)

# Print the success rate percentage
print(f"This is the value of {success_rate:.2f}%")

# Print the missions launched before year 2000
print("The missions launched prior to 2000 were: ")

for missions in missions_pre2000:
  print(missions)
