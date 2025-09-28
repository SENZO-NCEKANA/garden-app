// Function to get user input with validation
function getValidInput(prompt, validOptions) {
    let userInput;
    do {
        userInput = prompt(prompt).toLowerCase().trim();
        if (!validOptions.includes(userInput)) {
            alert(`Invalid option. Please choose from: ${validOptions.join(', ')}`);
        }
    } while (!validOptions.includes(userInput));
    return userInput;
}

// Function to generate gardening advice
function generateAdvice(season, plantType) {
    const adviceDict = {
        "summer": {
            "flower": "Water your plants regularly, provide shade, and use fertiliser to encourage blooms.",
            "vegetable": "Water your plants regularly and keep an eye out for pests!"
        },
        "winter": {
            "flower": "Protect your plants from frost with covers and use fertiliser sparingly.",
            "vegetable": "Protect your plants from frost and monitor for pests indoors."
        }
    };
    
    return adviceDict[season]?.[plantType] || "No specific advice for this combination.";
}

// Main function to run the garden advice app
function runGardenAdvice() {
    console.log("🌱 Welcome to the Gardening Advice App! 🌱");
    
    const seasons = ["summer", "winter"];
    const plantTypes = ["flower", "vegetable"];
    
    // Get user input
    const season = getValidInput("Enter the current season (summer/winter):", seasons);
    const plantType = getValidInput("Enter the type of plant (flower/vegetable):", plantTypes);
    
    // Generate and display advice
    const advice = generateAdvice(season, plantType);
    console.log("\nYour Gardening Advice:");
    console.log(advice);
    
    // Display advice in the HTML interface
    displayAdvice(advice);
}

// Function to display advice in the HTML interface
function displayAdvice(advice) {
    const adviceDisplay = document.getElementById('advice-display');
    const adviceText = document.getElementById('advice-text');
    
    adviceText.textContent = advice;
    adviceDisplay.style.display = 'block';
    
    // Scroll to the advice
    adviceDisplay.scrollIntoView({ behavior: 'smooth' });
}

// Initialize the app when the page loads
document.addEventListener('DOMContentLoaded', function() {
    console.log("Garden Advice App loaded successfully!");
});

// TODO: Examples of possible features to add:
// - Add detailed comments explaining each block of code.
// - Refactor the code into functions for better readability and modularity.
// - Store advice in an object for multiple plants and seasons.
// - Suggest plants that thrive in the given season.