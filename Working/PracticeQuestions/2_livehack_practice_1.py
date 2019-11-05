triangle_side_length_1 = int(input("Enter the first side length: "))
triangle_side_length_2 = int(input("Enter the second side length: "))
triangle_side_length_3 = int(input("Enter the last side length: "))
if (triangle_side_length_1 ** 2 + triangle_side_length_2 ** 2 == 
        triangle_side_length_3 ** 2 or triangle_side_length_2 ** 
        2 + triangle_side_length_3 ** 2 == triangle_side_length_1 or 
        triangle_side_length_3 ** 2 + triangle_side_length_1 ** 2 == 
        triangle_side_length_2 ** 2):
    print("This is a right angle triangle.")
else: 
    print("This is not a right angle triangle.")