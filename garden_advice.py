"""
Garden Advice Application

A Python application that provides seasonal gardening tips based on the current
month. The application loads tips from a JSON configuration file or falls back
to default tips if the configuration file is not available.

Author: Nelson
Version: 1.0.0
"""

import datetime
import json
from typing import Dict, List

# Default tips if config file is missing
DEFAULT_TIPS: Dict[str, List[str]] = {
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


def load_tips() -> Dict[str, List[str]]:
    """
    Load gardening tips from configuration file.

    Attempts to load tips from 'tips_config.json'. If the file is not found,
    contains invalid JSON, or encounters any other error, falls back to default
    tips.

    Returns:
        Dict[str, List[str]]: Dictionary containing seasonal tips

    Raises:
        No exceptions are raised; all errors are handled gracefully
    """
    try:
        with open('tips_config.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Warning: tips_config.json not found. Using default tips.")
        return DEFAULT_TIPS
    except json.JSONDecodeError as error:
        print(f"Warning: Error parsing JSON file: {error}. "
              f"Using default tips.")
        return DEFAULT_TIPS
    except PermissionError as error:
        print(f"Warning: Permission error: {error}. Using default tips.")
        return DEFAULT_TIPS
    except OSError as error:
        print(f"Warning: Error loading file: {error}. Using default tips.")
        return DEFAULT_TIPS
    except (ValueError, TypeError, AttributeError) as error:
        print(f"Warning: Unexpected error: {error}. Using default tips.")
        return DEFAULT_TIPS


# Load the tips
TIPS = load_tips()


def get_season(month: int) -> str:
    """
    Get season for month.

    Args:
        month (int): Month number (1-12)

    Returns:
        str: Season name ("Spring", "Summer", "Autumn", or "Winter")
    """
    if month in [9, 10, 11]:
        return "Spring"
    elif month in [12, 1, 2]:
        return "Summer"
    elif month in [3, 4, 5]:
        return "Autumn"
    else:
        return "Winter"


def get_garden_tips(month: int) -> List[str]:
    """
    Get gardening tips for a specific month.

    Args:
        month (int): Month number (1-12)

    Returns:
        List[str]: List of gardening tips for the month's season

    Note:
        Returns error messages if month is invalid
    """
    # Input validation for non-integer values
    if not isinstance(month, int):
        print("Error: Month must be an integer")
        return ["Invalid month"]
    if month < 1 or month > 12:
        print("Error: Month must be between 1 and 12")
        return ["Invalid month"]

    season = get_season(month)
    if season in TIPS:
        return TIPS[season]
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
            user_input = input(
                "\nEnter a month (1-12) or press Enter for current month: "
            ).strip()

            # If user presses Enter, use current month
            if not user_input:
                return datetime.datetime.now().month

            month = int(user_input)

            if 1 <= month <= 12:
                return month
            else:
                print("❌ Error: Month must be between 1 and 12. "
                      "Please try again.")
                continue

        except ValueError:
            print("❌ Error: Please enter a valid number between 1 and 12.")
            continue
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Happy gardening!")
            exit(0)
        except (TypeError, AttributeError) as e:
            print(f"❌ Unexpected error: {e}. Please try again.")


def display_advice() -> None:
    """
    Show advice and get current month with enhanced user experience.
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
    if (tips_list and tips_list[0] not in
            ["Invalid month", "No tips available"]):
        for index, tip in enumerate(tips_list, 1):
            print(f"  {index}. {tip}")
    else:
        print("  No tips available for this month.")

    print("\n" + "=" * 50)
    print("Happy gardening! 🌿")


def show_multiple_months() -> None:
    """
    Allow user to get tips for multiple months.
    """
    print("\n📅 Multiple Month Tips")
    print("-" * 30)

    months_to_show = []
    while True:
        try:
            month_input = input(
                "Enter a month (1-12) or 'done' to finish: "
            ).strip().lower()

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

            if (tips_list and tips_list[0] not in
                    ["Invalid month", "No tips available"]):
                for index, tip in enumerate(tips_list, 1):
                    print(f"  {index}. {tip}")
            else:
                print("  No tips available.")


def main() -> None:
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

                if (tips_list and tips_list[0] not in
                        ["Invalid month", "No tips available"]):
                    for index, tip in enumerate(tips_list, 1):
                        print(f"  {index}. {tip}")
                else:
                    print("  No tips available for this month.")

            elif choice == '2':
                display_advice()
            elif choice == '3':
                show_multiple_months()
            elif choice == '4':
                print("\n👋 Thank you for using Garden Advice! "
                      "Happy gardening! 🌿")
                break
            else:
                print("❌ Invalid choice. Please select 1, 2, 3, or 4.")

        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Happy gardening!")
            break
        except (ValueError, TypeError, AttributeError) as e:
            print(f"❌ An error occurred: {e}. Please try again.")


# Run main function when script is executed directly
if __name__ == "__main__":
    main()
