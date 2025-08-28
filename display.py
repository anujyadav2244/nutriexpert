
from food_database import FOOD_DATABASE, MEAL_TEMPLATES

def display_meal_suggestions(user):
    safe_foods = get_safe_foods(user)
    goal = user.goal
    
    print("\nBreakfast Options:")
    suggest_meals("breakfast", safe_foods, user, goal)
    
    print("\nLunch Options:")
    suggest_meals("lunch", safe_foods, user, goal)
    
    print("\nDinner Options:")
    suggest_meals("dinner", safe_foods, user, goal)

def get_safe_foods(user):
    safe_foods = []
    for food, data in FOOD_DATABASE.items():
        if is_food_allowed(food, data, user):
            safe_foods.append(food)
    return safe_foods

def is_food_allowed(food, data, user):
    # Check dietary restrictions
    if "vegetarian" in user.dietary_restrictions and data["category"] in ["meat", "fish"]:
        return False
    if "vegan" in user.dietary_restrictions and data["category"] in ["meat", "fish", "dairy"]:
        return False
    if "dairy-free" in user.dietary_restrictions and "dairy" in data.get("allergens", []):
        return False
    if "gluten-free" in user.dietary_restrictions and "gluten" in data.get("allergens", []):
        return False
        
    # Check allergies
    if any(allergen in user.allergies for allergen in data.get("allergens", [])):
        return False
        
    return True

def suggest_meals(meal_type, safe_foods, user, goal):
    suggestions = []
    
    for meal in MEAL_TEMPLATES.get(meal_type, []):
        if all(component in safe_foods for component in meal["components"]):
            # Score based on user's goals and preferences
            score = 0
            
            # Goal-based scoring
            if goal == "build-muscle" and "high-protein" in meal["tags"]:
                score += 2
            elif goal == "lose-weight" and "vegetarian" in meal["tags"]:
                score += 1
            elif goal == "maintain":
                score += 1
            
            # Preference-based scoring
            if "vegetarian" in user.dietary_restrictions and "vegetarian" in meal["tags"]:
                score += 1
            if "vegan" in user.dietary_restrictions and "vegan" in meal["tags"]:
                score += 2
            
            suggestions.append((score, meal["name"]))
    
    if not suggestions:
        print("- No suitable meals found (please adjust restrictions)")
        print("- Try adding more foods to your database")
    else:
        # Sort by score and show top 3
        suggestions.sort(reverse=True, key=lambda x: x[0])
        for meal in suggestions[:3]:
            print(f"- {meal[1]}")

def display_results(user, nutritional_needs, recommendations):
    """
    Display the user's nutritional needs and recommendations.
    """
    print("\n=== Results ===")
    print(f"User: {user.name}")
    print(f"Age: {user.age}")
    print(f"Gender: {user.gender}")
    print(f"Activity Level: {user.activity_level}")
    
    print("\n--- Nutritional Needs ---")
    for key, value in nutritional_needs.items():
        print(f"{key.capitalize()}: {value}")

    print("\n--- Recommendations ---")
    for recommendation in recommendations:
        print(f"- {recommendation['message']}")
