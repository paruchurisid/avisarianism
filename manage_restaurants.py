#!/usr/bin/env python3
"""
Restaurant Management Script for Columbus Wing Deals Scraper
Easy way to add, remove, or update restaurant information.
"""

import sys
from restaurant_data import (
    get_restaurants_by_category, 
    get_restaurant_names, 
    get_restaurant_by_name,
    add_restaurant, 
    remove_restaurant, 
    update_restaurant,
    RESTAURANT_CATEGORIES
)

def print_restaurants():
    """Print all restaurants with their details"""
    restaurants = get_restaurants_by_category()
    
    print("\n🍗 Current Restaurants in Database:")
    print("=" * 60)
    
    for i, restaurant in enumerate(restaurants, 1):
        print(f"{i:2d}. {restaurant['name']}")
        print(f"     Category: {restaurant['category']}")
        print(f"     URL: {restaurant['url']}")
        print(f"     Locations: {', '.join(restaurant['locations'])}")
        print(f"     Confidence: {restaurant['confidence']}")
        print(f"     Known Deals: {', '.join(restaurant['known_deals'])}")
        print()

def add_new_restaurant():
    """Interactive function to add a new restaurant"""
    print("\n➕ Adding New Restaurant")
    print("=" * 30)
    
    # Get restaurant name
    name = input("Restaurant name: ").strip()
    if not name:
        print("❌ Restaurant name is required!")
        return
    
    # Check if restaurant already exists
    if get_restaurant_by_name(name):
        print(f"❌ Restaurant '{name}' already exists!")
        return
    
    # Get category
    print("\nAvailable categories:")
    for key, description in RESTAURANT_CATEGORIES.items():
        print(f"  {key}: {description}")
    
    category = input("Category: ").strip().lower()
    if category not in RESTAURANT_CATEGORIES:
        print("❌ Invalid category!")
        return
    
    # Get URL
    url = input("Website URL: ").strip()
    if not url:
        print("❌ URL is required!")
        return
    
    # Get locations
    locations_input = input("Locations (comma-separated): ").strip()
    locations = [loc.strip() for loc in locations_input.split(',') if loc.strip()]
    if not locations:
        locations = ['Columbus']
    
    # Get known deals
    deals_input = input("Known deals (comma-separated): ").strip()
    known_deals = [deal.strip() for deal in deals_input.split(',') if deal.strip()]
    if not known_deals:
        known_deals = ['Wing specials', 'Daily deals']
    
    # Get confidence
    confidence = input("Confidence (high/medium/low) [medium]: ").strip().lower()
    if not confidence:
        confidence = 'medium'
    if confidence not in ['high', 'medium', 'low']:
        confidence = 'medium'
    
    # Create restaurant data
    restaurant_data = {
        'name': name,
        'url': url,
        'category': category,
        'locations': locations,
        'known_deals': known_deals,
        'confidence': confidence
    }
    
    # Add to database
    add_restaurant(restaurant_data)
    print(f"✅ Successfully added '{name}' to the database!")

def remove_existing_restaurant():
    """Interactive function to remove a restaurant"""
    print("\n🗑️  Removing Restaurant")
    print("=" * 25)
    
    # Show current restaurants
    restaurants = get_restaurant_names()
    print("Current restaurants:")
    for i, name in enumerate(restaurants, 1):
        print(f"{i:2d}. {name}")
    
    # Get restaurant to remove
    name = input("\nRestaurant name to remove: ").strip()
    if not name:
        print("❌ Restaurant name is required!")
        return
    
    # Check if restaurant exists
    if not get_restaurant_by_name(name):
        print(f"❌ Restaurant '{name}' not found!")
        return
    
    # Confirm removal
    confirm = input(f"Are you sure you want to remove '{name}'? (y/N): ").strip().lower()
    if confirm in ['y', 'yes']:
        if remove_restaurant(name):
            print(f"✅ Successfully removed '{name}' from the database!")
        else:
            print(f"❌ Failed to remove '{name}'!")
    else:
        print("❌ Removal cancelled.")

def update_existing_restaurant():
    """Interactive function to update a restaurant"""
    print("\n✏️  Updating Restaurant")
    print("=" * 25)
    
    # Show current restaurants
    restaurants = get_restaurant_names()
    print("Current restaurants:")
    for i, name in enumerate(restaurants, 1):
        print(f"{i:2d}. {name}")
    
    # Get restaurant to update
    name = input("\nRestaurant name to update: ").strip()
    if not name:
        print("❌ Restaurant name is required!")
        return
    
    # Check if restaurant exists
    restaurant = get_restaurant_by_name(name)
    if not restaurant:
        print(f"❌ Restaurant '{name}' not found!")
        return
    
    print(f"\nCurrent data for '{name}':")
    for key, value in restaurant.items():
        print(f"  {key}: {value}")
    
    # Get updated data
    print("\nEnter new values (press Enter to keep current value):")
    
    url = input(f"URL [{restaurant['url']}]: ").strip()
    if not url:
        url = restaurant['url']
    
    print("\nAvailable categories:")
    for key, description in RESTAURANT_CATEGORIES.items():
        print(f"  {key}: {description}")
    
    category = input(f"Category [{restaurant['category']}]: ").strip().lower()
    if not category:
        category = restaurant['category']
    elif category not in RESTAURANT_CATEGORIES:
        print("❌ Invalid category! Keeping current value.")
        category = restaurant['category']
    
    locations_input = input(f"Locations [{', '.join(restaurant['locations'])}]: ").strip()
    if locations_input:
        locations = [loc.strip() for loc in locations_input.split(',') if loc.strip()]
    else:
        locations = restaurant['locations']
    
    deals_input = input(f"Known deals [{', '.join(restaurant['known_deals'])}]: ").strip()
    if deals_input:
        known_deals = [deal.strip() for deal in deals_input.split(',') if deal.strip()]
    else:
        known_deals = restaurant['known_deals']
    
    confidence = input(f"Confidence [{restaurant['confidence']}]: ").strip().lower()
    if not confidence:
        confidence = restaurant['confidence']
    elif confidence not in ['high', 'medium', 'low']:
        print("❌ Invalid confidence! Keeping current value.")
        confidence = restaurant['confidence']
    
    # Create updated data
    updated_data = {
        'url': url,
        'category': category,
        'locations': locations,
        'known_deals': known_deals,
        'confidence': confidence
    }
    
    # Update restaurant
    if update_restaurant(name, updated_data):
        print(f"✅ Successfully updated '{name}'!")
    else:
        print(f"❌ Failed to update '{name}'!")

def show_statistics():
    """Show statistics about the restaurant database"""
    restaurants = get_restaurants_by_category()
    
    print("\n📊 Restaurant Database Statistics")
    print("=" * 40)
    
    total = len(restaurants)
    print(f"Total restaurants: {total}")
    
    # Count by category
    categories = {}
    for restaurant in restaurants:
        cat = restaurant['category']
        categories[cat] = categories.get(cat, 0) + 1
    
    print("\nBy category:")
    for category, count in categories.items():
        description = RESTAURANT_CATEGORIES.get(category, category)
        print(f"  {description}: {count}")
    
    # Count by confidence
    confidence_levels = {}
    for restaurant in restaurants:
        conf = restaurant['confidence']
        confidence_levels[conf] = confidence_levels.get(conf, 0) + 1
    
    print("\nBy confidence level:")
    for confidence, count in confidence_levels.items():
        print(f"  {confidence}: {count}")

def main():
    """Main menu function"""
    while True:
        print("\n🍗 Restaurant Management Menu")
        print("=" * 30)
        print("1. List all restaurants")
        print("2. Add new restaurant")
        print("3. Remove restaurant")
        print("4. Update restaurant")
        print("5. Show statistics")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            print_restaurants()
        elif choice == '2':
            add_new_restaurant()
        elif choice == '3':
            remove_existing_restaurant()
        elif choice == '4':
            update_existing_restaurant()
        elif choice == '5':
            show_statistics()
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter 1-6.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1) 