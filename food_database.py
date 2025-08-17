FOOD_DATABASE = {
    # Proteins
    "chicken": {"category": "meat", "allergens": []},
    "turkey": {"category": "meat", "allergens": []},
    "salmon": {"category": "fish", "allergens": ["shellfish"]},
    "tofu": {"category": "vegetarian", "allergens": []},
    "lentils": {"category": "vegetarian", "allergens": []},
    "black_beans": {"category": "vegetarian", "allergens": []},
    "eggs": {"category": "vegetarian", "allergens": ["eggs"]},
    
    # Carbs
    "brown_rice": {"category": "grain", "allergens": []},
    "quinoa": {"category": "grain", "allergens": []},
    "sweet_potato": {"category": "vegetable", "allergens": []},
    "oats": {"category": "grain", "allergens": []},
    "whole_wheat_pasta": {"category": "grain", "allergens": ["gluten"]},
    
    # Vegetables
    "broccoli": {"category": "vegetable", "allergens": []},
    "spinach": {"category": "vegetable", "allergens": []},
    "carrots": {"category": "vegetable", "allergens": []},
    "bell_peppers": {"category": "vegetable", "allergens": []},
    "zucchini": {"category": "vegetable", "allergens": []},
    
    # Fruits
    "banana": {"category": "fruit", "allergens": []},
    "berries": {"category": "fruit", "allergens": []},
    "apple": {"category": "fruit", "allergens": []},
    "avocado": {"category": "fruit", "allergens": []},
    
    # Dairy/Dairy Alternatives
    "greek_yogurt": {"category": "dairy", "allergens": ["dairy"]},
    "almond_milk": {"category": "dairy-free", "allergens": ["nuts"]},
    "coconut_yogurt": {"category": "dairy-free", "allergens": []},
    
    # Seeds/Nuts
    "sunflower_seeds": {"category": "seeds", "allergens": []},
    "chia_seeds": {"category": "seeds", "allergens": []},
    "almonds": {"category": "nuts", "allergens": ["nuts"]}
}

MEAL_TEMPLATES = {
    "breakfast": [
        {"name": "Protein oatmeal", "components": ["oats", "almond_milk", "banana"], "tags": ["high-protein", "dairy-free"]},
        {"name": "Tofu scramble", "components": ["tofu", "bell_peppers", "spinach"], "tags": ["vegan", "high-protein"]},
        {"name": "Yogurt parfait", "components": ["greek_yogurt", "berries", "chia_seeds"], "tags": []},
        {"name": "Avocado toast", "components": ["whole_wheat_pasta", "avocado", "eggs"], "tags": []},
        {"name": "Smoothie bowl", "components": ["coconut_yogurt", "banana", "berries"], "tags": ["vegan", "dairy-free"]}
    ],
    "lunch": [
        {"name": "Grilled chicken with quinoa", "components": ["chicken", "quinoa", "broccoli"], "tags": ["high-protein"]},
        {"name": "Lentil curry", "components": ["lentils", "brown_rice", "carrots"], "tags": ["vegan", "vegetarian"]},
        {"name": "Quinoa salad", "components": ["quinoa", "black_beans", "bell_peppers"], "tags": ["vegan", "vegetarian"]},
        {"name": "Salmon bowl", "components": ["salmon", "sweet_potato", "zucchini"], "tags": []},
        {"name": "Turkey wrap", "components": ["turkey", "whole_wheat_pasta", "spinach"], "tags": []}
    ],
    "dinner": [
        {"name": "Chicken stir-fry", "components": ["chicken", "broccoli", "bell_peppers"], "tags": ["high-protein"]},
        {"name": "Vegetable curry", "components": ["tofu", "carrots", "spinach"], "tags": ["vegan", "vegetarian"]},
        {"name": "Black bean tacos", "components": ["black_beans", "avocado", "bell_peppers"], "tags": ["vegan", "vegetarian"]},
        {"name": "Baked salmon", "components": ["salmon", "sweet_potato", "zucchini"], "tags": []},
        {"name": "Pasta primavera", "components": ["whole_wheat_pasta", "zucchini", "bell_peppers"], "tags": ["vegetarian"]}
    ]
}