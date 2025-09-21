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


def display_advice():
    """
    Show advice and get current month
    """
    now = datetime.datetime.now()
    current_month = now.month

    # get season and tips
    season = get_season(current_month)
    tips_list = get_garden_tips(current_month)

    # display info
    print("Welcome to Garden Advice!")
    print("Current month:", current_month)
    print("Season:", season)
    print("\nGardening Tips:")

    # show tips
    counter = 1
    for tip in tips_list:
        print(str(counter) + ". " + tip)
        counter = counter + 1


def main():
    """main function"""
    display_advice()


# run main function
if __name__ == "__main__":
    main()
