# Restaurant Menu Recommender - Multi-Cuisine
# 1st: Choose cuisine (Indian, Italian, Chinese, American, etc.)
# 2nd: Enter taste preferences
# 3rd: Select diet type (veg/non-veg/vegan)
# Shows top 3 matching dishes with prices

MENU = [
    # INDIAN
    {"name": "Chicken Tikka Masala", "cuisine": "Indian", "tastes": ["non-veg", "salty", "spicy"], "price": 1499},
    {"name": "Veg Biryani", "cuisine": "Indian", "tastes": ["veg", "salty", "medium cooked"], "price": 1099},
    {"name": "Paneer Tikka", "cuisine": "Indian", "tastes": ["veg", "salty", "spicy"], "price": 1250},
    {"name": "Dal Makhani", "cuisine": "Indian", "tastes": ["veg"], "price": 899},
    {"name": "Paneer Butter Masala", "cuisine": "Indian", "tastes": ["creamy", "savory", "veg"], "price": 250},
    {"name": "Hyderabadi Biryani", "cuisine": "Indian", "tastes": ["spicy", "aromatic", "non-veg"], "price": 300},
    {"name": "Masala Dosa", "cuisine": "Indian", "tastes": ["crispy", "spicy", "veg"], "price": 150},
    {"name": "Rogan Josh", "cuisine": "Indian", "tastes": ["spicy", "rich", "non-veg"], "price": 350},
    {"name": "Chole Bhature", "cuisine": "Indian", "tastes": ["spicy", "savory", "veg"], "price": 180},
    {"name": "Gulab Jamun", "cuisine": "Indian", "tastes": ["sweet", "dessert", "veg"], "price": 120},
    {"name": "Tandoori Chicken", "cuisine": "Indian", "tastes": ["spicy", "smoky", "non-veg"], "price": 280},
    {"name": "Dal Tadka", "cuisine": "Indian", "tastes": ["mild", "savory", "veg"], "price": 160},
    {"name": "Palak Paneer", "cuisine": "Indian", "tastes": ["creamy", "savory", "veg"], "price": 220},
    {"name": "Chicken Tikka Masala", "cuisine": "Indian", "tastes": ["spicy", "creamy", "non-veg"], "price": 320},
    {"name": "Rasgulla", "cuisine": "Indian", "tastes": ["sweet", "dessert", "veg"], "price": 100},
    {"name": "Aloo Paratha", "cuisine": "Indian", "tastes": ["savory", "veg"], "price": 80},
    {"name": "Fish Curry", "cuisine": "Indian", "tastes": ["spicy", "savory", "non-veg"], "price": 270},
    {"name": "Kheer", "cuisine": "Indian", "tastes": ["sweet", "dessert", "veg"], "price": 150},




    # ITALIAN
    {"name": "Margherita Pizza", "cuisine": "Italian", "tastes": ["veg", "salty"], "price": 1199},
    {"name": "Pasta Carbonara", "cuisine": "Italian", "tastes": ["non-veg", "salty", "creamy"], "price": 1399},
    {"name": "Vegan Pesto Pasta", "cuisine": "Italian", "tastes": ["vegan", "salty"], "price": 1250},
    {"name": "Spaghetti Carbonara", "cuisine": "Italian", "tastes": ["savory", "creamy", "non-veg"], "price": 650},
    {"name": "Lasagna Bolognese", "cuisine": "Italian", "tastes": ["savory", "rich", "non-veg"], "price": 700},
    {"name": "Risotto alla Milanese", "cuisine": "Italian", "tastes": ["savory", "creamy", "veg"], "price": 600},
    {"name": "Tiramisu", "cuisine": "Italian", "tastes": ["sweet", "dessert", "veg"], "price": 350},



    # CHINESE
    {"name": "Kung Pao Chicken", "cuisine": "Chinese", "tastes": ["non-veg", "spicy", "salty"], "price": 1350},
    {"name": "Veg Manchurian", "cuisine": "Chinese", "tastes": ["veg", "spicy"], "price": 1099},
    {"name": "Tofu Stir Fry", "cuisine": "Chinese", "tastes": ["vegan", "salty"], "price": 1150},
    {"name": "Sweet and Sour Pork", "cuisine": "Chinese", "tastes": ["sweet", "savory", "non-veg"], "price": 500},
    {"name": "Vegetable Chow Mein", "cuisine": "Chinese", "tastes": ["savory", "veg"], "price": 400},
    {"name": "Mapo Tofu", "cuisine": "Chinese", "tastes": ["spicy", "savory", "veg"], "price": 450},
    {"name": "Spring Rolls", "cuisine": "Chinese", "tastes": ["crispy", "savory", "veg"], "price": 300},



    # AMERICAN
    {"name": "Grilled Chicken", "cuisine": "American", "tastes": ["non-veg", "salty", "medium cooked"], "price": 1299},
    {"name": "Beef Burger", "cuisine": "American", "tastes": ["non-veg", "salty"], "price": 1350},
    {"name": "Sweet Potato Fries", "cuisine": "American", "tastes": ["vegan", "sweet"], "price": 799},
    {"name": "Cheeseburger", "cuisine": "American", "tastes": ["savory", "cheesy", "non-veg"], "price": 450},
    {"name": "Buffalo Wings", "cuisine": "American", "tastes": ["spicy", "savory", "non-veg"], "price": 500},
    {"name": "Mac and Cheese", "cuisine": "American", "tastes": ["savory", "creamy", "veg"], "price": 400},
    {"name": "BBQ Ribs", "cuisine": "American", "tastes": ["savory", "smoky", "non-veg"], "price": 650},
    {"name": "Apple Pie", "cuisine": "American", "tastes": ["sweet", "dessert", "veg"], "price": 300},


    # MEXICAN
    {"name": "Chicken Tacos", "cuisine": "Mexican", "tastes": ["non-veg", "spicy", "salty"], "price": 1299},
    {"name": "Veggie Burrito", "cuisine": "Mexican", "tastes": ["veg", "spicy"], "price": 1150},
    {"name": "Guacamole", "cuisine": "Mexican", "tastes": ["vegan"], "price": 999},
    {"name": "Tacos al Pastor", "cuisine": "Mexican", "tastes": ["spicy", "savory", "non-veg"], "price": 350},
    {"name": "Enchiladas Verdes", "cuisine": "Mexican", "tastes": ["spicy", "savory", "non-veg"], "price": 400},
    {"name": "Chiles Rellenos", "cuisine": "Mexican", "tastes": ["spicy", "savory", "veg"], "price": 380},
    {"name": "Pozole Rojo", "cuisine": "Mexican", "tastes": ["spicy", "hearty", "non-veg"], "price": 420},
    {"name": "Churros con Chocolate", "cuisine": "Mexican", "tastes": ["sweet", "dessert", "veg"], "price": 250}


]


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

