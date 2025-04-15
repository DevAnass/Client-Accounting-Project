str_length = input("Enter the length of the room:\n")
str_width  = input("Enter the room width:\n")
str_price = input("Enter the customer's fee per square meter(m2):\n")
length = float(str_length)
width = float(str_width)
price = float(str_price)
area = length * width
str_area = str(area)
print("The total area of the room is : " + str_area +"m2")
total_price = str(price)
total_price1 = str(price * area)
print ("The total fee to be paid to the customer is: " + total_price1 + "dh")

