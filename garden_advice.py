"""
Garden advice app
Gives gardening tips based on month and season
"""

import datetime
import json

# default tips if config file is missing
default_tips = {
    "Spring": [
        "Start seeds indoors for warm-season crops",
        "Prepare garden beds by adding compost",
        "Plant cool-season vegetables like lettuce and peas"
    ],
    "Summer": [
        "Water plants deeply in the morning",
        "Harvest vegetables regularly to encourage production",
        "Mulch around plants to retain moisture"
    ],
    "Autumn": [
        "Plant bulbs for spring flowers",
        "Harvest and store root vegetables",
        "Clean up garden debris to prevent disease"
    ],
    "Winter": [
        "Protect tender plants from frost",
        "Plan your garden layout for next year",
        "Order seeds and bulbs for spring planting"
    ]
}


def load_tips():
    """load tips from file"""
    # add better error handling for file loading
    try:
        f = open('tips_config.json', 'r', encoding='utf-8')
        data = json.load(f)
        f.close()
        return data
    except FileNotFoundError:
        print("Warning: tips_config.json not found. Using default tips.")
        return default_tips
    except json.JSONDecodeError as e:
        print(f"Warning: Error parsing JSON file: {e}. Using default tips.")
        return default_tips
    except OSError as e:
        print(f"Warning: Error loading file: {e}. Using default tips.")
        return default_tips
    except PermissionError as e:
        print(f"Warning: Permission error: {e}. Using default tips.")
        return default_tips
    except Exception as e:
        print(f"Warning: Unexpected error: {e}. Using default tips.")
        return default_tips


# load the tips
tips = load_tips()


def get_season(month):
    """
    Get season for month
    """
    if month == 9 or month == 10 or month == 11:
        return "Spring"
    elif month == 12 or month == 1 or month == 2:
        return "Summer"
    elif month == 3 or month == 4 or month == 5:
        return "Autumn"
    else:
        return "Winter"


def get_garden_tips(month):
    """
    Get tips for month
    check if month is valid
    """
    # add input validation for non-integer values
    if not isinstance(month, int):
        print("Error: Month must be an integer")
        return ["Invalid month"]
    if month < 1 or month > 12:
        print("Error: Month must be between 1 and 12")
        return ["Invalid month"]

    season = get_season(month)
    if season in tips:
        return tips[season]
    else:
        return ["No tips available"]


def get_user_input() -> int:
    """
    Get month input from user with validation.
    
    Returns:
        int: Valid month number (1-12)
    """
    while True:
        try:
            user_input = input("\nEnter a month (1-12) or press Enter for current month: ").strip()
            
            # If user presses Enter, use current month
            if not user_input:
                return datetime.datetime.now().month
            
            month = int(user_input)
            
            if 1 <= month <= 12:
                return month
            else:
                print("❌ Error: Month must be between 1 and 12. Please try again.")
                
        except ValueError:
            print("❌ Error: Please enter a valid number between 1 and 12.")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Happy gardening!")
            exit(0)
        except Exception as e:
            print(f"❌ Unexpected error: {e}. Please try again.")


def display_advice():
    """
    Show advice and get current month with enhanced user experience
    """
    print("🌱 Welcome to Garden Advice! 🌱")
    print("=" * 50)
    
    # Get month input from user
    current_month = get_user_input()
    
    # Get season and tips
    season = get_season(current_month)
    tips_list = get_garden_tips(current_month)

    # Display information with better formatting
    print(f"\n📅 Current month: {current_month}")
    print(f"🍂 Season: {season}")
    print(f"\n💡 Gardening Tips for {season}:")
    print("-" * 30)

    # Show tips with better formatting
    if tips_list and tips_list[0] != "Invalid month" and tips_list[0] != "No tips available":
        for index, tip in enumerate(tips_list, 1):
            print(f"  {index}. {tip}")
    else:
        print("  No tips available for this month.")
    
    print("\n" + "=" * 50)
    print("Happy gardening! 🌿")


def show_multiple_months():
    """
    Allow user to get tips for multiple months.
    """
    print("\n📅 Multiple Month Tips")
    print("-" * 30)
    
    months_to_show = []
    while True:
        try:
            month_input = input("Enter a month (1-12) or 'done' to finish: ").strip().lower()
            
            if month_input == 'done':
                break
                
            month = int(month_input)
            if 1 <= month <= 12:
                months_to_show.append(month)
                print(f"✅ Added month {month}")
            else:
                print("❌ Month must be between 1 and 12.")
                
        except ValueError:
            print("❌ Please enter a valid number or 'done'.")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Happy gardening!")
            exit(0)
    
    if months_to_show:
        print(f"\n🌱 Tips for months: {', '.join(map(str, months_to_show))}")
        print("=" * 50)
        
        for month in months_to_show:
            season = get_season(month)
            tips_list = get_garden_tips(month)
            
            print(f"\n📅 Month {month} ({season}):")
            print("-" * 20)
            
            if tips_list and tips_list[0] not in ["Invalid month", "No tips available"]:
                for index, tip in enumerate(tips_list, 1):
                    print(f"  {index}. {tip}")
            else:
                print("  No tips available.")


def main():
    """
    Main function with enhanced user experience and menu options.
    """
    while True:
        try:
            print("\n🌱 Garden Advice Menu 🌱")
            print("=" * 30)
            print("1. Get tips for current month")
            print("2. Get tips for specific month")
            print("3. Get tips for multiple months")
            print("4. Exit")
            print("-" * 30)
            
            choice = input("Choose an option (1-4): ").strip()
            
            if choice == '1':
                current_month = datetime.datetime.now().month
                season = get_season(current_month)
                tips_list = get_garden_tips(current_month)
                
                print(f"\n📅 Current month: {current_month}")
                print(f"🍂 Season: {season}")
                print(f"\n💡 Gardening Tips for {season}:")
                print("-" * 30)
                
                if tips_list and tips_list[0] not in ["Invalid month", "No tips available"]:
                    for index, tip in enumerate(tips_list, 1):
                        print(f"  {index}. {tip}")
                else:
                    print("  No tips available for this month.")
                    
            elif choice == '2':
                display_advice()
            elif choice == '3':
                show_multiple_months()
            elif choice == '4':
                print("\n👋 Thank you for using Garden Advice! Happy gardening! 🌿")
                break
            else:
                print("❌ Invalid choice. Please select 1, 2, 3, or 4.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Happy gardening!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}. Please try again.")


# Run main function when script is executed directly
if __name__ == "__main__":
    main()
