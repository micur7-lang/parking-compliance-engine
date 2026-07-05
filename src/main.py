"""
One-Way Parking Decision Support System
Author: Michael Stephen Curbeam Jr.
Description: An automated rule-based compliance engine evaluating real-time 
             situational variables to determine street parking eligibility.
"""

def parse_time(time_str):
    """Parses a time string (e.g., '10:00 AM') into hour, minutes, and period."""
    try:
        hour_part, remaining = time_str.split(":")
        hour = int(hour_part)
        remaining = remaining.strip().upper()
        minutes_str, period = remaining.split(" ")
        return hour, int(minutes_str), period
    except (ValueError, IndexError):
        return None, None, None

def check_overnight_restriction(hour, minutes, period):
    """Enforces standard 12:00 AM - 3:00 AM daily restriction."""
    if period == "AM":
        if (hour >= 1 and hour <= 3) or hour == 12:
            if hour == 3 and minutes >= 1:
                return False  # Grace period after 3:00 AM
            return True
    return False

def evaluate_compliance():
    print("=== Parking Compliance Engine Initialized ===")
    
    # 1. Ingest Data Inputs
    day = input("Enter day of the week (e.g., Wednesday): ").strip().lower()
    time_input = input("Enter time of day (e.g., 10:00 AM): ").strip().lower()
    permit = input("Do you have a permit? (yes/no): ").strip().lower()
    street_side = input("Which side of the street? (left/right): ").strip().lower()
    try:
        duration = int(input("Enter parking duration (hours): "))
    except ValueError:
        print("Invalid duration value entered.")
        return

    valid_days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    if day not in valid_days:
        print("Invalid Response!")
        return

    sure = input("Are you sure you want to park here? (yes/no): ").strip().lower()
    is_rebel = (sure == "yes")

    # 2. Parse Temporal Variables
    hour, minutes, period = parse_time(time_input)
    if hour is None:
        print("Invalid time format. Please use 'HH:MM AM/PM'.")
        return

    # 3. State Trackers
    ticket_amount = 0
    bool_park = True
    
    # Base daily rates
    overnight_rate = 80 if day == "sunday" else 40

    # 4. Core Rule Matrix Execution
    # Rule A: Daily Universal Overnight Restrictions (12AM - 3AM)
    if check_overnight_restriction(hour, minutes, period):
        print("Parking is not allowed at this time.")
        if is_rebel:
            print("WOW! You are a rebel!!!")
            bool_park = False
            ticket_amount += 40

    # Rule B: Weekday Orientation Restrictions
    if day in ["monday", "tuesday", "wednesday", "thursday", "friday"] and street_side == "right":
        print("You can't park here.")
        if is_rebel:
            print("WOW! You are a rebel!!!")
            bool_park = False
            ticket_amount += 40

    # Rule C: Permit Validations (Excluding Wednesdays)
    if permit == "no" and day != "wednesday":
        print("You can't park here without a permit.")
        if is_rebel:
            print("WOW! You are a rebel!!!")
            bool_park = False
            ticket_amount += 40

    # Rule D: Duration Ceiling Caps
    max_hours = 4
    if duration > max_hours:
        print(f"Parking is only allowed for {max_hours} hours.")
        if is_rebel:
            print("WOW! You are a rebel!!!")
            bool_park = False
            ticket_amount += 40

    # Rule E: Sunday Specific Operational Restrictions
    if day == "sunday":
        if period == "AM" and (hour >= 7 and hour <= 11):
            print("Parking is not allowed at this time.")
            if is_rebel:
                print("WOW! You are a rebel!!!")
                bool_park = False
                ticket_amount += 40
        elif period == "PM" and ((hour >= 1 and hour <= 7) or hour == 12):
            if not (hour == 7 and minutes >= 1):
                print("Parking is not allowed at this time.")
                if is_rebel:
                    print("WOW! You are a rebel!!!")
                    bool_park = False
                    ticket_amount += 40

    # Rule F: Compound Time Accumulation Infractions
    if duration % 24 == 0 and duration != 0:
        ticket_amount += overnight_rate * (duration / 24)

    # 5. Output Verdict Generation
    if ticket_amount > 0:
        print("\nYou received a ticket.")
        print(f"Your total ticket amount is ${int(ticket_amount)}. Please login to MSUParking.com to pay your fine.")
    
    if bool_park and is_rebel:
        print(f"\nSuccess: You can safely park at {time_input} on {day.capitalize()}.")

if __name__ == "__main__":
    evaluate_compliance()