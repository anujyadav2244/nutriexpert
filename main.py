from user_profile import UserProfile
from nutrition import calculate_nutritional_needs
from recommendations import generate_recommendations
from display import display_results  # This now matches the function name

def main():
    print("\n=== NutriExpert AI ===")
    print("Personalized Nutrition Advisor\n")
    
    # Create and collect user profile
    user = UserProfile()
    user.collect_info()
    
    # Calculate nutritional needs
    nutritional_needs = calculate_nutritional_needs(user)
    
    # Generate recommendations
    recommendations = generate_recommendations(user, nutritional_needs)
    
    # Display results
    display_results(user, nutritional_needs, recommendations)

if __name__ == "__main__":
    main()