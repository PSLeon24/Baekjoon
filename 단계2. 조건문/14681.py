# Step 1. Input x, y
x = int(input())
y = int(input())

# Step 2. Create coordinates list.
coordinates = []
# Step 2_1. Insert coordinate.
coordinates.append(x)
coordinates.append(y)

# Check, print(coordinates)

'''
coordinates[0] == x
coordinates[1] == y
'''
# Step 3. Pick a quadrant
if coordinates[0] > 0 and coordinates[1] > 0:
    print(1)
elif coordinates[0] < 0 and coordinates[1] > 0:
    print(2)
elif coordinates[0] < 0 and coordinates[1] < 0:
    print(3)
elif coordinates[0] > 0 and coordinates[1] < 0:
    print(4)
'''
elif coordinates[0] == 0 and coordinates[1] == 0:
    print(0)
'''
