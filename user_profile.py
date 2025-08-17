from utils import get_number_input, get_choice_input, get_numbered_choices

class UserProfile:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = ""
        self.height = 0
        self.weight = 0
        self.activity_level = ""
        self.goal = ""
        self.dietary_restrictions = []
        self.allergies = []

    def collect_info(self):
        print("\n=== Personal Information ===")
        self.name = input("Your name: ").strip()
        self.age = get_number_input("Your age (18-100): ", 18, 100)
        self.gender = get_choice_input("Gender (male/female): ", ["male", "female"])
        self.height = get_number_input("Height in cm (120-250): ", 120, 250)
        self.weight = get_number_input("Weight in kg (30-300): ", 30, 300)
        
        print("\n=== Activity Level ===")
        print("1. Sedentary (little/no exercise)")
        print("2. Light (exercise 1-3 days/week)")
        print("3. Moderate (exercise 3-5 days/week)")
        print("4. Active (exercise 6-7 days/week)")
        print("5. Very Active (hard exercise daily)")
        self.activity_level = get_choice_input(
            "Enter choice (1-5): ",
            ["sedentary", "light", "moderate", "active", "very-active"],
            numbered=True
        )

        print("\n=== Primary Goal ===")
        print("1. Lose weight")
        print("2. Maintain weight")
        print("3. Gain weight")
        print("4. Build muscle")
        self.goal = get_choice_input(
            "Enter choice (1-4): ",
            ["lose-weight", "maintain", "gain-weight", "build-muscle"],
            numbered=True
        )

        print("\n=== Dietary Restrictions ===")
        print("1. Vegetarian")
        print("2. Vegan")
        print("3. Gluten-free")
        print("4. Dairy-free")
        print("5. None")
        self.dietary_restrictions = get_numbered_choices(
            options=["vegetarian", "vegan", "gluten-free", "dairy-free", "none"],
            prompt="Enter numbers (e.g., 1,3): "
        )

        print("\n=== Allergies ===")
        print("1. Nuts")
        print("2. Shellfish")
        print("3. Eggs")
        print("4. Dairy")
        print("5. None")
        self.allergies = get_numbered_choices(
            options=["nuts", "shellfish", "eggs", "dairy", "none"],
            prompt="Enter numbers (e.g., 2,4): "
        )