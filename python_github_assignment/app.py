print("Welcome to my Python program!")

# Ask the user for input (daily study hours)

hours = input("How many hours did you study today? ")

# Add simple error handling: ensure the user enters a numeric value
try:
	hours = float(hours)
except ValueError:
	print("Please enter a valid number for hours (for example: 2.5).")
	exit()

# Perform the calculation (estimate weekly hours from daily input)
weekly_hours = hours * 7

# Display the result in a clear, readable format
print(f"You are on track to study {weekly_hours:.2f} hours this week.")

