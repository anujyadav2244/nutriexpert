# NutriExpert AI – Personalized Diet Expert System

## 📌 Overview

NutriExpert AI is a **terminal-based Python application** that helps users manage their nutrition by calculating calorie needs, suggesting macro targets, generating personalized recommendations, and offering safe meal suggestions based on dietary restrictions and allergies.

The system asks for the user’s details (age, weight, height, gender, activity level, goals, restrictions), then uses scientific formulas to generate a **personalized nutrition plan**.

---

## 🚀 Features

* ✅ Collects personal information (age, gender, height, weight, activity, goal).
* ✅ Calculates **BMR, TDEE, BMI, daily calories, macros (protein, carbs, fat), and water intake**.
* ✅ Gives **goal-based recommendations** (lose weight, gain weight, build muscle, maintain).
* ✅ Supports **dietary restrictions** (vegetarian, vegan, gluten-free, dairy-free) and **allergies** (nuts, eggs, dairy, shellfish).
* ✅ Suggests **safe meal options** (breakfast, lunch, dinner) using a built-in food database.
* ✅ Clean modular code split into multiple files for readability.

---

## 🏗 Project Structure

```
NutriExpert-AI/
│── main.py               # Entry point – runs the app
│── user_profile.py       # Collects user information
│── nutrition.py          # Calculates calories, macros, BMI, water
│── recommendations.py    # Generates personalized recommendations
│── food_database.py      # Food database + meal templates
│── display.py            # Displays results and meal suggestions
│── utils.py              # Helper functions for input handling
│── README.md             # Project documentation
```

---

## ⚙️ How It Works

1. Run `main.py`.
2. Enter your personal details when prompted.
3. Program calculates **nutrition needs** (calories, macros, BMI, water).
4. Program generates **recommendations** based on your BMI, goal, and restrictions.
5. Program shows **meal suggestions** that fit your restrictions and goals.

---

## 📊 Example Run

```
=== NutriExpert AI ===
Personalized Nutrition Advisor

=== Personal Information ===
Your name: Anuj
Your age (18-100): 22
Gender (male/female): male
Height in cm (120-250): 175
Weight in kg (30-300): 70

=== Activity Level ===
1. Sedentary (little/no exercise)
2. Light (exercise 1-3 days/week)
3. Moderate (exercise 3-5 days/week)
4. Active (exercise 6-7 days/week)
5. Very Active (hard exercise daily)
Enter choice (1-5): 4

=== Primary Goal ===
1. Lose weight
2. Maintain weight
3. Gain weight
4. Build muscle
Enter choice (1-4): 4

=== Results ===
User: Anuj
Age: 22
Gender: male
Activity Level: active

--- Nutritional Needs ---
calories: 2700
protein: 154 g
carbs: 320 g
fat: 75 g
water: 2.5 L
bmi: 22.9

--- Recommendations ---
- For muscle building: Consume protein every 3-4 hours and train regularly.
- Stay hydrated: Drink 2.5L of water daily.

--- Meal Suggestions ---
Breakfast Options:
- Protein oatmeal
- Tofu scramble
- Yogurt parfait
```

---

## 🛠 Installation & Usage

### 1. Clone the repo

```bash
https://github.com/anujyadav2244/nutriexpert.git
```

### 2. Run the program

```bash
python main.py
```

---

## 📖 Tech Stack

* **Language**: Python 3
* **Concepts**: OOP (Classes & Objects), Dictionaries, User Input Validation
* **Nutrition Logic**: BMR, TDEE, BMI formulas

---

## 💡 Future Improvements

* Add **GUI/Web interface** (Tkinter/Flask/React + Flask).
* Save user history to a database (SQLite/MongoDB).
* Integrate with **fitness trackers/APIs** for real-time data.
* Add **meal planning & grocery list generator**.
