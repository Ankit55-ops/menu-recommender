from menu_data import MENU_DATA  # ✅ IMPORTS FROM SEPARATE FILE
import random

def get_valid_food_preference():
    """Get and validate food preference input from user"""
    print("\n🥗 Choose your food preference:")
    print("- Veg")
    print("- Non-Veg") 
    print("- Vegan")
    
    while True:
        pref = input("Enter choice (Veg/Non-Veg/Vegan): ").strip().title()
        
        if pref in ["Veg"]:
            return "Veg"
        elif pref in ["Non-Veg", "Nonveg", "Non Veg"]:
            return "Non-Veg"
        elif pref == "Vegan":
            return "Vegan"
        else:
            print("❌ Invalid! Please enter Veg, Non-Veg, or Vegan")

def get_valid_cuisine():
    """Get and validate cuisine type input from user"""
    print("\n🌏 Available Cuisines:")
    print("- Indian 🇮🇳")
    print("- Nepali 🇳🇵") 
    print("- Continental 🌍")
    
    while True:
        cuisine = input("Choose cuisine: ").strip().title()
        
        if cuisine == "Indian":
            return "Indian"
        elif cuisine in ["Nepali", "Nepalese"]:
            return "Nepali"
        elif cuisine == "Continental":
            return "Continental"
        else:
            print("❌ Invalid cuisine! Choose from list above.")

def get_valid_taste(cuisine, food_pref):
    """Get available tastes and validate user selection"""
    tastes = list(MENU_DATA[cuisine][food_pref].keys())
    print(f"\n👅 Available tastes for {cuisine} {food_pref}:")
    
    for i, taste in enumerate(tastes, 1):
        print(f"  {i}. {taste}")
    
    while True:
        choice = input("Choose taste (number or name): ").strip().title()
        
        if choice.isdigit() and 1 <= int(choice) <= len(tastes):
            return tastes[int(choice)-1]
        elif choice in tastes:
            return choice
        else:
            print("❌ Invalid taste! Choose from list.")

def get_customization():
    """Get optional customization from user"""
    print("\n✨ Optional Customizations:")
    print("- extra cheese")
    print("- less oil") 
    print("- no onion")
    print("- gluten-free")
    
    custom = input("Enter customization or press Enter for none: ").strip()
    return custom if custom else "Standard preparation"

def recommend_menu_items(cuisine, food_pref, taste, customization):
    """Generate and display 2-3 personalized recommendations"""
    dishes = MENU_DATA[cuisine][food_pref][taste]
    
    num_recs = min(3, len(dishes))
    recommendations = random.sample(dishes, num_recs)
    
    print("\n" + "═"*60)
    print("🎉 YOUR PERFECT MENU RECOMMENDATIONS 🎉")
    print("═"*60)
    print(f"🥗 Type: {food_pref} | 🌏 Cuisine: {cuisine} | 👅 Taste: {taste}")
    print(f"✨ Custom: {customization}")
    print("─"*60)
    
    for i, dish in enumerate(recommendations, 1):
        print(f"{i}. 🍽️  {dish}")
        if customization != "Standard preparation":
            print(f"    ➤ Customized: {customization}")
        print()
    
    print("═"*60)
    print("Enjoy your meal! 😋")
