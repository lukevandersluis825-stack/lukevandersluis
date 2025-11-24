print("Welcome to my Python program!")

# Ask the user for input (daily study hours)
hours = input("How many hours did you study today? ")

# Convert the input into a numeric type and perform a calculation
hours = float(hours)
weekly_hours = hours * 7

# Display the result in a clear, readable format
print(f"You are on track to study {weekly_hours:.2f} hours this week.")

