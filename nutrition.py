def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)

def calculate_bmr(weight_kg, height_cm, age, gender):
    if gender == "male":
        return 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        return 10 * weight_kg + 6.25 * height_cm - 5 * age - 161

def get_activity_multiplier(activity_level):
    multipliers = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very-active": 1.9
    }
    return multipliers.get(activity_level, 1.2)

def calculate_nutritional_needs(user):
    bmr = calculate_bmr(user.weight, user.height, user.age, user.gender)
    tdee = bmr * get_activity_multiplier(user.activity_level)
    
    # Adjust calories based on goal
    if user.goal == "lose-weight":
        calories = tdee - 500  # 1 lb/week weight loss
    elif user.goal == "gain-weight":
        calories = tdee + 300  # Reduced from 500 to 300 for more realistic gain
    elif user.goal == "build-muscle":
        calories = tdee + 250  # More moderate surplus
    else:  # maintain
        calories = tdee
    
    # Calculate macros
    protein_multiplier = 2.2 if user.goal == "build-muscle" else 1.6
    protein_g = user.weight * protein_multiplier
    fat_g = (calories * 0.25) / 9  # 25% of calories from fat
    carbs_g = (calories - (protein_g * 4) - (fat_g * 9)) / 4
    water_l = user.weight * 0.035  # 35ml per kg body weight
    
    return {
        "calories": max(1200, round(calories)),  # Minimum safe calories
        "protein": round(protein_g),
        "carbs": round(carbs_g),
        "fat": round(fat_g),
        "water": round(water_l, 1),
        "bmi": round(calculate_bmi(user.weight, user.height), 1)
    }