# app.py

from Conversions import Length, Time, NumberSystem
# Other modules can be added later:
# from Area import Area
# from Volume import Volume
# from Interest import Interest
# from Trignometry import Trignometry
# from Statistics import Statistics
# from Vector import Vector


def main():
    while True:
        print("\n=== Conversion Application ===")
        print("1. Length Conversions")
        print("2. Time Conversions")
        print("3. Number System Conversions")
        print("4. Area (Coming Soon)")
        print("5. Volume (Coming Soon)")
        print("6. Interest (Coming Soon)")
        print("7. Trigonometry (Coming Soon)")
        print("8. Statistics (Coming Soon)")
        print("9. Vector Operations (Coming Soon)")
        print("0. Exit")
        
        choice = input("Enter your choice: ")

        # ---------------- Length ----------------
        if choice == "1":
            print("\nLength Conversions:")
            print("a. Meters to Feet")
            print("b. Feet to Meters")
            print("c. Kilometers to Miles")
            print("d. Miles to Kilometers")
            sub_choice = input("Select an option: ")

            if sub_choice == "a":
                meters = float(input("Enter meters: "))
                print("Feet:", Length.meters_to_feet(meters))
            elif sub_choice == "b":
                feet = float(input("Enter feet: "))
                print("Meters:", Length.feet_to_meters(feet))
            elif sub_choice == "c":
                km = float(input("Enter kilometers: "))
                print("Miles:", Length.kilometers_to_miles(km))
            elif sub_choice == "d":
                miles = float(input("Enter miles: "))
                print("Kilometers:", Length.miles_to_kilometers(miles))
            else:
                print("Invalid option.")

        # ---------------- Time ----------------
        elif choice == "2":
            print("\nTime Conversions:")
            print("a. Hours to Minutes")
            print("b. Minutes to Hours")
            print("c. Seconds to Minutes")
            print("d. Minutes to Seconds")
            sub_choice = input("Select an option: ")

            if sub_choice == "a":
                hours = float(input("Enter hours: "))
                print("Minutes:", Time.hours_to_minutes(hours))
            elif sub_choice == "b":
                minutes = float(input("Enter minutes: "))
                print("Hours:", Time.minutes_to_hours(minutes))
            elif sub_choice == "c":
                seconds = float(input("Enter seconds: "))
                print("Minutes:", Time.seconds_to_minutes(seconds))
            elif sub_choice == "d":
                minutes = float(input("Enter minutes: "))
                print("Seconds:", Time.minutes_to_seconds(minutes))
            else:
                print("Invalid option.")

        # ---------------- Number System ----------------
        elif choice == "3":
            print("\nNumber System Conversions:")
            print("a. Decimal to Binary")
            print("b. Binary to Decimal")
            print("c. Binary to Hexadecimal")
            sub_choice = input("Select an option: ")

            if sub_choice == "a":
                number = int(input("Enter decimal number: "))
                print("Binary:", NumberSystem.decimal_to_binary(number))
            elif sub_choice == "b":
                binary_str = input("Enter binary number: ")
                print("Decimal:", NumberSystem.binary_to_decimal(binary_str))
            elif sub_choice == "c":
                binary_str = input("Enter binary number: ")
                print("Hexadecimal:", NumberSystem.binary_to_hex(binary_str))
            else:
                print("Invalid option.")

        # ---------------- Placeholders ----------------
        elif choice in ["4", "5", "6", "7", "8", "9"]:
            print("This module is under development. Please check back later.")

        # ---------------- Exit ----------------
        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
