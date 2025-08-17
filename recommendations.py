def generate_recommendations(user, nutrition):
    recommendations = []
    bmi = nutrition["bmi"]
    
    # BMI-based recommendations
    if bmi < 18.5:
        recommendations.append({
            "priority": "high",
            "message": "Your BMI indicates underweight. Focus on nutrient-dense, calorie-rich foods."
        })
    elif bmi > 25:
        recommendations.append({
            "priority": "high",
            "message": "Your BMI suggests overweight. Consider portion control and regular exercise."
        })
    
    # Goal-based recommendations
    if user.goal == "lose-weight":
        recommendations.append({
            "priority": "high",
            "message": "For weight loss: Emphasize vegetables, lean proteins, and whole grains."
        })
    elif user.goal == "build-muscle":
        recommendations.append({
            "priority": "high",
            "message": "For muscle building: Consume protein every 3-4 hours and train regularly."
        })
    
    # Dietary restrictions
    if "vegetarian" in user.dietary_restrictions:
        recommendations.append({
            "priority": "medium",
            "message": "As vegetarian: Include plant proteins like beans, lentils, and tofu."
        })
    
    if "dairy-free" in user.dietary_restrictions:
        recommendations.append({
            "priority": "medium",
            "message": "Dairy-free: Use almond milk, coconut yogurt as alternatives."
        })
    
    # General health
    recommendations.append({
        "priority": "medium",
        "message": f"Stay hydrated: Drink {nutrition['water']}L of water daily."
    })
    
    return recommendations