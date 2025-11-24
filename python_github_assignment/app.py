
"""
Study-hours estimator

This simple script asks for how many hours you studied today,
estimates the total for a week, and prints the result. It includes
basic error handling to avoid crashing on invalid input.
"""

print("Welcome to my Python program!")

# --- Input ---------------------------------------------------------
hours = input("How many hours did you study today? ")

# --- Validation & Calculation ------------------------------------
try:
	# Convert the user input to a float (may raise ValueError)
	hours = float(hours)
except ValueError:
	print("Please enter a valid number for hours (for example: 2.5).")
	exit()

# Estimate weekly study hours from the daily number
weekly_hours = hours * 7

# --- Output --------------------------------------------------------
print(f"You are on track to study {weekly_hours:.2f} hours this week based on {hours:.2f} hours/day.")

