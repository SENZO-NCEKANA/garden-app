"""
A simple command-line application that provides gardening advice
based on the season and type of plant.
"""

# garden_advice.py


def get_user_input(prompt: str, valid_options: list[str]) -> str:
    """
    Prompt the user for input and validate it against allowed options.

    Args:
        prompt (str): The message displayed to the user.
        valid_options (list[str]): List of valid input options.

    Returns:
        str: Validated user input.
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        print(
            f"Invalid option. Please choose from: {', '.join(valid_options)}"
        )


def generate_advice(season: str, plant_type: str) -> str:
    """
    Generate gardening advice based on the season and plant type.

    Args:
        season (str): Current season (e.g., 'summer', 'winter').
        plant_type (str): Type of plant (e.g., 'flower', 'vegetable').

    Returns:
        str: Gardening advice for the specified season and plant type.
    """
    advice_dict = {
        "summer": {
            "flower": (
                "Water your plants regularly, "
                "provide shade, and use fertilizer to encourage blooms."
            ),
            "vegetable": (
                "Water your plants regularly keep an eye out for pests!"
            ),
        },
        "winter": {
            "flower": (
                "Protect your plants from frost with covers,"
                "Also use fertilizer sparingly."
            ),
            "vegetable": (
                "Protect your plants from frost,"
                "Monitor for pests indoors."
            )
        },
    }

    return advice_dict.get(season, {}).get(
        plant_type, "No specific advice for this combination."
    )


def main() -> None:
    """
    Main function to run the Gardening Advice App.
    Prompts the user for season and plant type and displays advice.
    """
    print("🌱 Welcome to the Gardening Advice App! 🌱\n")

    seasons = ["summer", "winter"]
    plant_types = ["flower", "vegetable"]

    # Get user input
    season = get_user_input(
        "Enter the current season (summer/winter): ", seasons
    )
    plant_type = get_user_input(
        "Enter the type of plant (flower/vegetable): ", plant_types
    )

    # Generate and display advice
    advice = generate_advice(season, plant_type)
    print("\nYour Gardening Advice:")
    print(advice)


if __name__ == "__main__":
    main()
