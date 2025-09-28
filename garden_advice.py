# garden_advice.py

def get_user_input(prompt, valid_options):
    """
    Get user input and validate it against allowed options.

    Parameters:
        prompt (str): The input prompt for the user.
        valid_options (list): List of valid options to accept.

    Returns:
        str: Validated user input.
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        print(f"Invalid option. Please choose from: "
              f"{', '.join(valid_options)}")


def generate_advice(season, plant_type):
    """
    Generate gardening advice based on season and plant type.

    Parameters:
        season (str): Current season.
        plant_type (str): Type of plant.

    Returns:
        str: Gardening advice.
    """
    # Advice dictionary
    advice_dict = {
        "summer": {
            "flower": (
                "Water your plants regularly, provide shade, and use "
                "fertiliser to encourage blooms."
            ),
            "vegetable": (
                "Water your plants regularly and keep an eye out for pests!"
            ),
        },
        "winter": {
            "flower": (
                "Protect your plants from frost with covers and use "
                "fertiliser sparingly."
            ),
            "vegetable": (
                "Protect your plants from frost and monitor for pests indoors."
            ),
        }
    }

    # Default advice if season or plant_type not recognized
    return advice_dict.get(season, {}).get(
        plant_type, "No specific advice for this combination."
    )


def main():
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
