import csv
from datetime import datetime
import sys  # [NEW] Import sys to use sys.exit() for clean exit

from matplotlib import pyplot as plt

# [MODIFIED] Load both high and low temperature data in one pass
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # [NEW] Added 'lows' list to store low temperatures
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[5])
            low = int(row[6])  # [NEW] Extract low temperature from row
        except ValueError:
            continue  # Skip rows with missing or bad data
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)  # [NEW] Append low to lows list

# [NEW] Define function to display menu options to the user
def show_menu():
    print("\nWeather Data Viewer - Sitka 2018")
    print("Choose an option:")
    print("1. High Temperatures")
    print("2. Low Temperatures")
    print("3. Exit")

# [NEW] Define reusable function to plot either highs or lows
def plot_data(dates, temperatures, title, color):
    """
    Plot temperatures on a graph with a given title and color.
    """
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, c=color)  # Plot with specified color
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()  # Auto-format dates on x-axis
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

# [NEW] Main loop to allow repeated user interaction
while True:
    show_menu()  # [NEW] Show menu options
    choice = input("Enter your choice (1/2/3): ").strip()  # [NEW] Get user input

    if choice == '1':
        # [NEW] User chose to view high temperatures
        plot_data(dates, highs, "Daily High Temperatures - 2018", 'red')
    elif choice == '2':
        # [NEW] User chose to view low temperatures
        plot_data(dates, lows, "Daily Low Temperatures - 2018", 'blue')
    elif choice == '3':
        # [NEW] User chose to exit the program
        print("Exiting the program. Goodbye!")
        sys.exit()  # [NEW] Exit cleanly using sys.exit()
    else:
        # [NEW] Handle invalid menu inputs
        print("Invalid choice. Please enter 1, 2, or 3.")
