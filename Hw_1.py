lower_level_seats = int(input("Enter the number of lower-level seats: "))
mid_level_seats = int(input("Enter the number of mid-level seats: "))
upper_level_seats = int(input("Enter the number of upper-level seats: "))


lower_level_cost = lower_level_seats * 25
mid_level_cost = mid_level_seats * 15
upper_level_cost = upper_level_seats * 10


grand_total = lower_level_cost + mid_level_cost + upper_level_cost


print("\nSeat Pricing Chart:")
print(f"Lower-level seats total cost: ${lower_level_cost}")
print(f"Mid-level seats total cost: ${mid_level_cost}")
print(f"Upper-level seats total cost: ${upper_level_cost}")
print(f"Grand Total: ${grand_total}")
