items = [
    {"name": "Train to Busan", "category": "movie","genre": "thriller", "rating": 9},
    {"name": "Demon Slayer: Infinity Castle", "category": "movie", "genre": "anime", "rating": 10},
    {"name": "Zootopia", "category": "movie","genre":"anime","rating":8},
    {"name": "Avatar: The Way of Water", "category": "movie","genre": "adventure","rating":8},
    {"name": "Parasite", "category": "movie","genre": "thriller", "rating": 9},
    {"name": "Jumanji", "category": "movie", "genre": "comedy", "rating": 8},
    {"name": "Home Alone", "category": "movie","genre": "comedy", "rating": 8},
    {"name": "Jurassic Park", "category": "movie","genre":"adventure","rating": 8},
    {"name": "Harry Potter and the Prisoner of Azkaban", "category": "movie","genre":"fantasy", "rating": 8},
    {"name": "Atomic Habits", "category": "book", "genre": "self-help", "rating": 9},
    {"name": "The Alchemist", "category": "book", "genre": "fiction", "rating": 8},
    {"name": "The Hunger Games","category": "book", "genre": "adventure", "rating": 9},
    {"name": "The Women in the Window", "category": "book", "genre": "thriller", "rating": 9},
    {"name": "Wireless Headphones", "category": "product", "genre": "electronics", "rating": 8},
    {"name": "Gaming Mouse", "category": "product", "genre": "electronics", "rating": 9},
    {"name": "Bluetooth Speaker", "category":"product", "genre":"electronics", "rating": 8},
    {"name": "Mechanical keyboard", "category":"product", "genre":"electronics", "rating": 7},
]
def recommend():
    print("Welcome! I can recommend movies, books, or products for you ")
    category = input("What are you looking for? (movie/book/product): ").lower().strip()
    item_type = input("Enter preferred type (e.g., anime, thriller, comedy, adventure, fiction, electronics): ").lower().strip()
    rating_input = input("Minimum rating you prefer? (1-10): ").strip()
    if rating_input.isdigit():
        min_rating = int(rating_input)
    else:
        print("Invalid rating. Using default rating 5.")
        min_rating = 5
    print("\nHere are some recommendations for you:\n")
    found = False
    for item in items:
        if (item["category"] == category and
            item["genre"] == item_type and
            item["rating"] >= min_rating):
            print(f"• {item['name']} (Rating: {item['rating']}/10)")
            found = True
    if not found:
        print("Sorry, no items matched your preferences.")
recommend()
