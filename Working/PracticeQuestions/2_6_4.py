start_dist = int(input("Starting distance: "))
end_dist = int(input("Target distance: "))
i = 1 
while start_dist < end_dist:
    start_dist = start_dist * 1.1
    i += 1
print("You will be ready to run", end_dist, "km", "in", i, "days")