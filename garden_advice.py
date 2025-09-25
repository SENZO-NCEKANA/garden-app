"""
Garden Advice Application

A Python application that provides seasonal gardening tips based on the current
month. The application loads tips from a JSON configuration file or falls back
to default tips if the configuration file is not available.

Author: Senzo Ncekana
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
    except Exception as error:
        print(f"Warning: Unexpected error: {error}. Using default tips.")
        return DEFAULT_TIPS


# Load the tips
TIPS = load_tips()


def get_season(month: int) -> str:
    """
    Determine the season based on the month.

    Args:
        month (int): Month number (1-12)

    Returns:
        str: Season name ("Spring", "Summer", "Autumn", or "Winter")

    Note:
        This function uses Southern Hemisphere seasons:
        - Spring: September, October, November
        - Summer: December, January, February
        - Autumn: March, April, May
        - Winter: June, July, August
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


def display_advice() -> None:
    """
    Display gardening advice for the current month.

    Shows the current month, season, and relevant gardening tips.
    """
    now = datetime.datetime.now()
    current_month = now.month

    # Get season and tips
    season = get_season(current_month)
    tips_list = get_garden_tips(current_month)

    # Display information
    print("Welcome to Garden Advice!")
    print(f"Current month: {current_month}")
    print(f"Season: {season}")
    print("\nGardening Tips:")

    # Show tips with proper numbering
    for index, tip in enumerate(tips_list, 1):
        print(f"{index}. {tip}")


def main() -> None:
    """
    Main function to run the garden advice application.

    This is the entry point of the application.
    """
    display_advice()


# Run main function when script is executed directly
if __name__ == "__main__":
    main()
