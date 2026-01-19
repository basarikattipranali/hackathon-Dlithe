import os
from datetime import date

# ----------------------------------
# User Defined Data Structure
# ----------------------------------
class Production:
    def __init__(self, prod_date, shift, units_produced, target):
        self.prod_date = prod_date
        self.shift = shift
        self.units_produced = units_produced
        self.target = target

    def __str__(self):
        return f"{self.prod_date},{self.shift},{self.units_produced},{self.target}"


# ----------------------------------
# File Name
# ----------------------------------
FILE_NAME = "production_data.txt"


# ----------------------------------
# Load Production Data from File
# ----------------------------------
def load_production_data():
    records = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                if line.strip() == "":
                    continue
                try:
                    prod_date, shift, units, target = line.strip().split(",")
                    records.append(
                        Production(prod_date, shift, int(units), int(target))
                    )
                except ValueError:
                    continue

    return records


# ----------------------------------
# Save Production Data to File
# ----------------------------------
def save_production_data(records):
    with open(FILE_NAME, "w") as file:
        for record in records:
            file.write(str(record) + "\n")


# ----------------------------------
# Add Shift Output (Using Dictionary Draft)
# ----------------------------------
def add_shift_output(records):
    # Draft dictionary
    draft = {
        "prod_date": str(date.today()),
        "shift": "",
        "units_produced": 0,
        "target": 0
    }

    draft["shift"] = input("Enter Shift (Morning/Evening/Night): ")

    try:
        draft["units_produced"] = int(input("Enter Units Produced: "))
        draft["target"] = int(input("Enter Production Target: "))
    except ValueError:
        print("Invalid input! Units and Target must be numbers.")
        return

    print("\n--- Draft Production Entry ---")
    print(f"Date           : {draft['prod_date']}")
    print(f"Shift          : {draft['shift']}")
    print(f"Units Produced : {draft['units_produced']}")
    print(f"Target         : {draft['target']}")

    confirm = input("\nSave this record? (y/n): ").lower()

    if confirm == "y":
        records.append(
            Production(
                draft["prod_date"],
                draft["shift"],
                draft["units_produced"],
                draft["target"]
            )
        )
        save_production_data(records)
        print("Production data saved successfully.")
    else:
        print("Draft entry discarded.")


# ----------------------------------
# Daily Production Report
# ----------------------------------
def daily_production_report(records):
    report_date = input("Enter date (YYYY-MM-DD): ")

    total_units = 0
    total_target = 0
    found = False

    print("\nShift\tUnits\tTarget\tStatus")
    print("-" * 40)

    for r in records:
        if r.prod_date == report_date:
            found = True
            status = "Achieved" if r.units_produced >= r.target else "Not Achieved"
            print(f"{r.shift}\t{r.units_produced}\t{r.target}\t{status}")
            total_units += r.units_produced
            total_target += r.target

    if not found:
        print("No production data found for this date.")
        return

    overall_status = "Achieved" if total_units >= total_target else "Not Achieved"

    print("-" * 40)
    print(f"Total\t{total_units}\t{total_target}\t{overall_status}")


# ----------------------------------
# Display All Records
# ----------------------------------
def display_all_records(records):
    if not records:
        print("No production records available.")
        return

    print("\nDate\t\tShift\tUnits\tTarget")
    print("-" * 45)

    for r in records:
        print(f"{r.prod_date}\t{r.shift}\t{r.units_produced}\t{r.target}")


# ----------------------------------
# Main Menu
# ----------------------------------
def main():
    records = load_production_data()

    while True:
        print("\n--- Manufacturing Production Tracking System ---")
        print("1. Add Shift Output")
        print("2. Generate Daily Production Report")
        print("3. Display All Production Records")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_shift_output(records)
        elif choice == "2":
            daily_production_report(records)
        elif choice == "3":
            display_all_records(records)
        elif choice == "4":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Please try again.")


# ----------------------------------
# Program Execution Starts Here
# ----------------------------------
if __name__ == "__main__":
    main()
