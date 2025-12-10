from constants import MENU
def get_cuisine():
    """Choose cuisine FIRST."""
    print("\n🌍 SELECT CUISINE:")
    cuisines = ["Indian", "Italian", "Chinese", "American", "Mexican"]
    for i, cuisine in enumerate(cuisines, 1):
        print(f"{i}. {cuisine}")

    while True:
        choice = input("Enter choice (1-5): ").strip()
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(cuisines):
                return cuisines[idx]
        except:
            pass
        print("Please enter 1-5!")


def get_taste_preferences():
    """Get taste preferences SECOND."""
    print(f"\nEnter TASTE preferences for cuisine (up to 5):")
    print("e.g., salty, spicy, sweet, medium cooked, creamy")
    print("Type 'done' when finished:")

    tastes = []
    while len(tastes) < 5:
        taste = input(f"Taste {len(tastes) + 1} (or 'done'): ").lower().strip()
        if taste == 'done':
            break
        if taste and taste not in tastes:
            tastes.append(taste)

    return tastes


def get_diet_type():
    """Get diet type THIRD."""
    print("\nSelect your DIET TYPE:")
    print("1. veg")
    print("2. non-veg")
    print("3. vegan")

    while True:
        choice = input("Enter choice (1/2/3): ").strip().lower()
        if choice == '1':
            return 'veg'
        elif choice == '2':
            return 'non-veg'
        elif choice == '3':
            return 'vegan'
        else:
            print("Please enter 1, 2, or 3!")


def find_recommendations(cuisine, tastes, diet_type):
    """Find dishes matching cuisine + ALL tastes + diet type."""
    all_preferences = tastes + [diet_type]
    matches = []

    for dish in MENU:
        if (dish["cuisine"] == cuisine and
                all(pref in dish["tastes"] for pref in all_preferences)):
            matches.append(dish)

    return sorted(matches, key=lambda x: x["price"])[:3]


def display_recommendations(cuisine, recommendations):
    """Show 3 recommended options."""
    print(f"\n🍽️  {cuisine.upper()} CUISINE RECOMMENDATIONS:")
    if recommendations:
        for i, dish in enumerate(recommendations, 1):
            print(f"{i}. {dish['name']} - ${dish['price']:.2f}")
    else:
        print("No matching dishes found! Try different preferences.")


def main():
    # STEP 1: Choose cuisine first
    cuisine = get_cuisine()

    # STEP 2: Get taste preferences
    tastes = get_taste_preferences()

    # STEP 3: Get diet type
    diet_type = get_diet_type()

    # Find and display recommendations
    print(f"\nSearching {cuisine} dishes for: {', '.join(tastes)} + {diet_type}")
    recommendations = find_recommendations(cuisine, tastes, diet_type)
    display_recommendations(cuisine, recommendations)


if __name__ == "__main__":
    main()

