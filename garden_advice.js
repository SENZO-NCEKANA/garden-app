// garden advice app

// get user input for season and plant type
function getUserInput() {
    // try to get from prompt, fallback to defaults
    var season = prompt("Enter season (summer, winter, spring, autumn):") || "summer";
    var plantType = prompt("Enter plant type (flower, vegetable, herb, tree):") || "flower";
    return { season: season, plantType: plantType };
}

// get user input
var userInput = getUserInput();
var season = userInput.season;
var plantType = userInput.plantType;

// variable to hold gardening advice
let advice = "";

// default tips if config file is missing
const defaultTips = {
    "Spring": [
        "Plant warm-season vegetables and flowers",
        "Prepare garden beds with organic compost",
        "Start seeds indoors for tender crops",
        "Monitor soil moisture and adjust watering"
    ],
    "Summer": [
        "Water plants deeply in early morning",
        "Harvest crops regularly to encourage growth",
        "Apply mulch to conserve soil moisture",
        "Provide shade for heat-sensitive plants"
    ],
    "Autumn": [
        "Plant cool-season vegetables and bulbs",
        "Harvest and preserve summer produce",
        "Plant trees and shrubs for next season",
        "Clean up garden debris and prepare beds"
    ],
    "Winter": [
        "Protect tender plants from cold weather",
        "Plan next year's garden layout",
        "Order seeds and supplies for spring",
        "Maintain winter crops with care"
    ]
};

// advice based on plant type
const plantAdvice = {
    "flower": "Use fertilizer to encourage blooms",
    "vegetable": "Keep an eye out for pests!",
    "herb": "Harvest regularly to promote growth",
    "tree": "Prune during dormant season"
};

// load tips from json file or use default
function loadTips() {
    // TODO: Load tips from JSON file instead of using defaultHardcodedTips
    // try to load from json file
    try {
        return defaultTips;
    } catch (error) {
        console.log("Using default tips");
        return defaultTips;
    }
}

// get season for month
function getSeason(month) {
    // southern hemisphere seasons
    if (month == 9 || month == 10 || month == 11) {
        return "Spring";
    } else if (month == 12 || month == 1 || month == 2) {
        return "Summer";
    } else if (month == 3 || month == 4 || month == 5) {
        return "Autumn";
    } else {
        return "Winter";
    }
}

// get tips for month
function getGardenTips(month) {
    // TODO: Validate month more strictly (check for non-numeric values)
    // check if month is valid
    if (month < 1 || month > 12) {
        console.log("Error: Month must be between 1 and 12");
        return ["Invalid month"];
    }

    var season = getSeason(month);
    if (season in tips) {
        return tips[season];
    } else {
        return ["No tips available"];
    }
}

// determine advice based on season
function getSeasonAdvice(season) {
    // convert season to match JSON format
    var seasonKey = season.charAt(0).toUpperCase() + season.slice(1);
    
    if (seasonKey in tips) {
        var seasonTips = tips[seasonKey];
        var advice = "";
        for (var i = 0; i < seasonTips.length; i++) {
            advice += seasonTips[i] + "\n";
        }
        return advice;
    } else {
        return "No advice for this season.\n";
    }
}

// determine advice based on plant type
function getPlantAdvice(plantType) {
    if (plantType in plantAdvice) {
        return plantAdvice[plantType];
    } else {
        return "No advice for this type of plant.";
    }
}

// show advice
function displayAdvice() {
    // get current month
    var now = new Date();
    var currentMonth = now.getMonth() + 1; // JavaScript months are 0-based

    // get season and tips
    var currentSeason = getSeason(currentMonth);
    var tipsList = getGardenTips(currentMonth);

    // display info
    console.log("Welcome to Garden Advice!");
    console.log("Current month:", currentMonth);
    console.log("Season:", currentSeason);
    console.log("\nGardening Tips:");

    // show tips
    var counter = 1;
    for (var i = 0; i < tipsList.length; i++) {
        console.log(counter + ". " + tipsList[i]);
        counter = counter + 1;
    }

    console.log("\n--- Hardcoded Advice ---");
    
    // determine advice based on hardcoded season
    advice += getSeasonAdvice(season);
    
    // determine advice based on hardcoded plant type
    advice += getPlantAdvice(plantType);
    
    // log the generated advice to console
    console.log("Hardcoded season:", season);
    console.log("Hardcoded plant type:", plantType);
    console.log("Advice:", advice);
}

// load the tips
var tips = loadTips();

// run the app when page loads
document.addEventListener('DOMContentLoaded', function() {
    displayAdvice();
});
