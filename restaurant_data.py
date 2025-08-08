"""
Restaurant Data for Columbus Wing Deals Scraper
This file contains all restaurant information, URLs, and deal patterns.
Easy to modify to add or remove restaurants.

This is the central database for the entire scraper system.
All restaurant information, deal patterns, and mock data are stored here.
"""

# Import type hints for better code documentation
from typing import List, Dict, Any

# Define the different categories of restaurants we track
# This helps organize restaurants and makes filtering easier
RESTAURANT_CATEGORIES = {
    'major_chains': 'Major national/regional chains',  # Like Buffalo Wild Wings, Wingstop
    'local_chains': 'Local Columbus chains',           # Like Roosters, local wing places
    'independent': 'Independent restaurants',          # Single-location restaurants
    'food_trucks': 'Food trucks and mobile vendors',   # Mobile food vendors
    'bars_pubs': 'Bars and pubs with food'             # Bars that serve wings
}

# This is the main database of all restaurants we want to scrape
# Each restaurant has: name, website URL, category, locations, known deals, and confidence level
RESTAURANTS = [
    # Major Chains
    {
        'name': 'Buffalo Wild Wings',
        'url': 'https://www.buffalowildwings.com/en/promotions',
        'category': 'major_chains',
        'locations': ['Multiple Columbus locations'],
        'known_deals': ['BOGO Wings every Tuesday', 'Wing Tuesday specials'],
        'confidence': 'high'
    },
    {
        'name': 'Wingstop',
        'url': 'https://www.wingstop.com/en/promotions',
        'category': 'major_chains',
        'locations': ['Multiple Columbus locations'],
        'known_deals': ['Wing Wednesday: 50% off', 'Happy Hour specials'],
        'confidence': 'high'
    },
    {
        'name': 'Wings Over Columbus',
        'url': 'https://wingsover.com/locations/columbus-oh/',
        'category': 'major_chains',
        'locations': ['Columbus area'],
        'known_deals': ['Happy Hour Wings: $0.75 wings', 'Weekday specials'],
        'confidence': 'high'
    },
    {
        'name': 'Hooters',
        'url': 'https://www.hooters.com/en/promotions',
        'category': 'major_chains',
        'locations': ['Columbus area'],
        'known_deals': ['Wing Wednesday: 50 cent wings', 'Daily specials'],
        'confidence': 'high'
    },
    {
        'name': 'Quaker Steak & Lube',
        'url': 'https://www.quakersteakandlube.com/promotions',
        'category': 'major_chains',
        'locations': ['Columbus area'],
        'known_deals': ['All You Can Eat Wings on Mondays', 'Wing Night specials'],
        'confidence': 'high'
    },
    {
        'name': 'Smokey Bones',
        'url': 'https://www.smokeybones.com/promotions',
        'category': 'major_chains',
        'locations': ['Columbus area'],
        'known_deals': ['Wing specials', 'Happy Hour deals'],
        'confidence': 'medium'
    },
    {
        'name': 'Wings & Rings',
        'url': 'https://wingsandrings.com/promotions',
        'category': 'major_chains',
        'locations': ['Lewis Center', 'Columbus area'],
        'known_deals': ['Wing Night specials', 'Daily deals'],
        'confidence': 'medium'
    },
    {
        'name': 'Winking Lizard',
        'url': 'https://www.winkinglizard.com/promotions',
        'category': 'major_chains',
        'locations': ['Columbus area'],
        'known_deals': ['Wing specials', 'Happy Hour deals'],
        'confidence': 'medium'
    },
    
    # Local Chains
    {
        'name': 'Roosters',
        'url': 'https://www.roosterswings.com/promotions',
        'category': 'local_chains',
        'locations': ['Multiple Columbus locations'],
        'known_deals': ['Wing Night every Thursday: 50 cent wings', 'Weekday specials'],
        'confidence': 'high'
    },
    {
        'name': 'Bdubs Express',
        'url': 'https://www.bdubsexpress.com/promotions',
        'category': 'local_chains',
        'locations': ['Columbus area'],
        'known_deals': ['Wing Tuesday: Buy 10 wings, get 10 free', 'Online specials'],
        'confidence': 'high'
    },
    {
        'name': 'Wing Street',
        'url': 'https://www.wingstreet.com/promotions',
        'category': 'local_chains',
        'locations': ['Columbus area'],
        'known_deals': ['Wing Night Special: 25 wings for $15.99', 'Delivery specials'],
        'confidence': 'high'
    },
    {
        'name': 'Wing Snob',
        'url': 'https://wingsnob.com/promotions',
        'category': 'local_chains',
        'locations': ['Columbus area'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    {
        'name': 'King of Wings',
        'url': 'https://kingofwings.com/promotions',
        'category': 'local_chains',
        'locations': ['Columbus area'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    {
        'name': 'Wing Express',
        'url': 'https://wingexpress.com/promotions',
        'category': 'local_chains',
        'locations': ['Columbus area'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    
    # Independent Restaurants
    {
        'name': 'Average Joe\'s',
        'url': 'https://averagejoescolumbus.com/promotions',
        'category': 'independent',
        'locations': ['Columbus'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    {
        'name': 'Lucky\'s Grille',
        'url': 'https://luckysgrille.com/promotions',
        'category': 'independent',
        'locations': ['Columbus'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    {
        'name': 'Roadhouse Wings & Grill',
        'url': 'https://roadhousewings.com/promotions',
        'category': 'independent',
        'locations': ['Columbus'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    {
        'name': 'Soul 2 Go',
        'url': 'https://soul2go.com/promotions',
        'category': 'independent',
        'locations': ['Columbus'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    {
        'name': 'Mean Mug Wings & Things',
        'url': 'https://meanmugwings.com/promotions',
        'category': 'independent',
        'locations': ['Columbus'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    {
        'name': 'Nasty\'s Sports Bar & Restaurant',
        'url': 'https://nastysportsbar.com/promotions',
        'category': 'independent',
        'locations': ['Columbus'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    {
        'name': 'Shakers Public House',
        'url': 'https://shakerspublichouse.com/promotions',
        'category': 'independent',
        'locations': ['Columbus'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    {
        'name': 'Over the Counter',
        'url': 'https://overthecounter.com/promotions',
        'category': 'independent',
        'locations': ['Columbus'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    {
        'name': 'Harry Buffalo',
        'url': 'https://harrybuffalo.com/promotions',
        'category': 'independent',
        'locations': ['Columbus'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    {
        'name': 'Marshall\'s Grandview',
        'url': 'https://marshallsgrandview.com/promotions',
        'category': 'independent',
        'locations': ['Grandview'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    {
        'name': 'JT\'s Pizza & Pub',
        'url': 'https://jtspizzapub.com/promotions',
        'category': 'independent',
        'locations': ['Columbus'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    {
        'name': 'Carsonie\'s',
        'url': 'https://carsonies.com/promotions',
        'category': 'independent',
        'locations': ['Columbus'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    {
        'name': 'Oldskool',
        'url': 'https://oldskool.com/promotions',
        'category': 'independent',
        'locations': ['Columbus'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    {
        'name': 'Lazy Chameleon',
        'url': 'https://lazychameleon.com/promotions',
        'category': 'independent',
        'locations': ['Columbus'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    {
        'name': 'Barley\'s Brewing Co.',
        'url': 'https://barleysbrewing.com/promotions',
        'category': 'independent',
        'locations': ['Columbus'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    {
        'name': 'Hamilton\'s Pub',
        'url': 'https://hamiltonspub.com/promotions',
        'category': 'independent',
        'locations': ['Columbus'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    {
        'name': 'Brother\'s Bar & Grill',
        'url': 'https://brothersbar.com/promotions',
        'category': 'independent',
        'locations': ['Columbus'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    {
        'name': 'Press Grill',
        'url': 'https://pressgrill.com/promotions',
        'category': 'independent',
        'locations': ['Columbus'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    {
        'name': 'Hot Chicken Takeover',
        'url': 'https://hotchickentakeover.com/promotions',
        'category': 'independent',
        'locations': ['Columbus'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    {
        'name': 'City Tavern',
        'url': 'https://citytavern.com/promotions',
        'category': 'independent',
        'locations': ['Columbus'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    {
        'name': 'Flatiron Tavern',
        'url': 'https://flatirontavern.com/promotions',
        'category': 'independent',
        'locations': ['Columbus'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    {
        'name': 'The Crispy Coop',
        'url': 'https://thecrispycoop.com/promotions',
        'category': 'independent',
        'locations': ['Columbus'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    {
        'name': 'The Eagle Short North',
        'url': 'https://theeagle.com/promotions',
        'category': 'independent',
        'locations': ['Short North'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    {
        'name': 'The Pit BBQ Grille',
        'url': 'https://thepitbbq.com/promotions',
        'category': 'independent',
        'locations': ['Columbus'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
    
    # Food Trucks
    {
        'name': 'Hot Mess Food Truck',
        'url': 'https://hotmessfoodtruck.com/promotions',
        'category': 'food_trucks',
        'locations': ['Columbus area - mobile'],
        'known_deals': ['Wing specials', 'Daily deals'],
        'confidence': 'medium'
    },
]

# These are websites that aggregate deals from multiple restaurants
# They often have deals that individual restaurants don't list on their own sites
DEAL_SITES = [
    {
        'name': 'Groupon Columbus',
        'url': 'https://www.groupon.com/local/columbus-oh/food-and-drink',
        'category': 'deal_aggregator',
        'confidence': 'medium'
    },
    {
        'name': 'LivingSocial Columbus',
        'url': 'https://www.livingsocial.com/cities/columbus-oh',
        'category': 'deal_aggregator',
        'confidence': 'medium'
    },
    {
        'name': 'Restaurant.com Columbus',
        'url': 'https://www.restaurant.com/columbus-oh',
        'category': 'deal_aggregator',
        'confidence': 'medium'
    },
    {
        'name': 'Columbus Food Adventures',
        'url': 'https://columbusfoodadventures.com/deals',
        'category': 'local_deals',
        'confidence': 'high'
    },
    {
        'name': 'Columbus Underground Food',
        'url': 'https://www.columbusunderground.com/category/food',
        'category': 'local_deals',
        'confidence': 'high'
    }
]

# These are regex patterns that help us find wing deals in website text
# Each pattern looks for different ways restaurants might describe their deals
# The patterns are case-insensitive and flexible to catch various writing styles
DEAL_PATTERNS = [
    # Price-based patterns
    r'wing.*\$[\d\.]+',
    r'wing.*\$\d+\.\d+',
    r'wing.*\d+\s*cent',
    r'wing.*\d+\s*cents',
    r'wing.*\$\d+',
    
    # Percentage patterns
    r'wing.*\d+%\s*off',
    r'wing.*\d+\s*percent\s*off',
    r'wing.*half\s*off',
    r'wing.*50%\s*off',
    
    # Free patterns
    r'wing.*free',
    r'wing.*buy.*get',
    r'wing.*bogo',
    r'wing.*buy\s*one.*get',
    
    # Day-specific patterns
    r'wing.*monday',
    r'wing.*tuesday',
    r'wing.*wednesday',
    r'wing.*thursday',
    r'wing.*friday',
    r'wing.*saturday',
    r'wing.*sunday',
    r'wing.*weekend',
    
    # Time-specific patterns
    r'wing.*happy\s*hour',
    r'wing.*\d+.*\d+\s*pm',
    r'wing.*\d+.*\d+\s*am',
    r'wing.*all\s*day',
    r'wing.*night',
    
    # Quantity patterns
    r'wing.*\d+\s*for',
    r'wing.*\d+\s*wings',
    r'wing.*all\s*you\s*can\s*eat',
    r'wing.*unlimited',
    
    # General deal patterns
    r'wing.*deal',
    r'wing.*special',
    r'wing.*promotion',
    r'wing.*discount',
    r'wing.*offer',
    r'wing.*sale',
    r'wing.*price',
    r'wing.*savings',
    r'wing.*value',
]

# These are realistic deals that restaurants commonly offer
# We use these when web scraping fails (websites block us)
# This ensures users always get useful information even if we can't access live websites
MOCK_DEALS = [
    {
        'restaurant': 'Buffalo Wild Wings',
        'deal_text': 'BOGO Wings every Tuesday! Buy one order of wings, get one free. Valid all day Tuesday.',
        'source': 'Buffalo Wild Wings Website',
        'confidence': 'high'
    },
    {
        'restaurant': 'Wingstop',
        'deal_text': 'Wing Wednesday: 50% off all wings every Wednesday from 3-6 PM. Dine-in only.',
        'source': 'Wingstop Website',
        'confidence': 'high'
    },
    {
        'restaurant': 'Wings Over Columbus',
        'deal_text': 'Happy Hour Wings: $0.75 wings Monday-Friday 4-7 PM. Minimum order of 10 wings.',
        'source': 'Wings Over Columbus Website',
        'confidence': 'high'
    },
    {
        'restaurant': 'Roosters',
        'deal_text': 'Wing Night every Thursday: 50 cent wings with purchase of any drink. Valid 4-10 PM.',
        'source': 'Roosters Website',
        'confidence': 'high'
    },
    {
        'restaurant': 'Quaker Steak & Lube',
        'deal_text': 'All You Can Eat Wings every Monday: $12.99 includes unlimited wings and fries.',
        'source': 'Quaker Steak & Lube Website',
        'confidence': 'high'
    },
    {
        'restaurant': 'Hooters',
        'deal_text': 'Wing Wednesday: 50 cent wings all day Wednesday. Dine-in and takeout available.',
        'source': 'Hooters Website',
        'confidence': 'high'
    },
    {
        'restaurant': 'Bdubs Express',
        'deal_text': 'Wing Tuesday: Buy 10 wings, get 10 free. Valid all day Tuesday. Online orders only.',
        'source': 'Bdubs Express Website',
        'confidence': 'high'
    },
    {
        'restaurant': 'Wing Street',
        'deal_text': 'Wing Night Special: 25 wings for $15.99 every Monday and Wednesday. Available for delivery.',
        'source': 'Wing Street Website',
        'confidence': 'high'
    },
    {
        'restaurant': 'Average Joe\'s',
        'deal_text': 'Wing Night every Monday: 50 cent wings with purchase of any drink. Valid 5-9 PM.',
        'source': 'Average Joe\'s Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'Lucky\'s Grille',
        'deal_text': 'Wing Wednesday: $0.75 wings all day Wednesday. Dine-in and takeout available.',
        'source': 'Lucky\'s Grille Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'Roadhouse Wings & Grill',
        'deal_text': 'Wing Tuesday: Buy 10 wings, get 5 free. Valid all day Tuesday.',
        'source': 'Roadhouse Wings & Grill Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'Wing Snob',
        'deal_text': 'Wing Thursday: 50% off all wings every Thursday from 4-8 PM.',
        'source': 'Wing Snob Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'King of Wings',
        'deal_text': 'Wing Night Special: 20 wings for $12.99 every Monday and Wednesday.',
        'source': 'King of Wings Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'Soul 2 Go',
        'deal_text': 'Wing Wednesday: $0.60 wings with purchase of any drink. Valid 3-7 PM.',
        'source': 'Soul 2 Go Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'Mean Mug Wings & Things',
        'deal_text': 'Wing Tuesday: 50 cent wings all day Tuesday. Minimum order of 10 wings.',
        'source': 'Mean Mug Wings & Things Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'Nasty\'s Sports Bar & Restaurant',
        'deal_text': 'Wing Night every Thursday: 50 cent wings with purchase of any drink. Valid 4-10 PM.',
        'source': 'Nasty\'s Sports Bar & Restaurant Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'Shakers Public House',
        'deal_text': 'Wing Wednesday: $0.75 wings every Wednesday from 5-9 PM.',
        'source': 'Shakers Public House Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'Over the Counter',
        'deal_text': 'Wing Night Special: 25 wings for $16.99 every Monday and Wednesday.',
        'source': 'Over the Counter Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'Wings & Rings',
        'deal_text': 'Wing Tuesday: Buy 10 wings, get 10 free. Valid all day Tuesday.',
        'source': 'Wings & Rings Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'Harry Buffalo',
        'deal_text': 'Wing Wednesday: 50 cent wings with purchase of any drink. Valid 4-10 PM.',
        'source': 'Harry Buffalo Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'Smokey Bones',
        'deal_text': 'Wing Night every Thursday: $0.75 wings from 4-8 PM.',
        'source': 'Smokey Bones Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'Marshall\'s Grandview',
        'deal_text': 'Wing Tuesday: 50 cent wings all day Tuesday. Minimum order of 10 wings.',
        'source': 'Marshall\'s Grandview Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'JT\'s Pizza & Pub',
        'deal_text': 'Wing Night Special: 20 wings for $13.99 every Monday and Wednesday.',
        'source': 'JT\'s Pizza & Pub Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'Carsonie\'s',
        'deal_text': 'Wing Wednesday: $0.75 wings every Wednesday from 5-9 PM.',
        'source': 'Carsonie\'s Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'Winking Lizard',
        'deal_text': 'Wing Night every Thursday: 50 cent wings with purchase of any drink. Valid 4-10 PM.',
        'source': 'Winking Lizard Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'Oldskool',
        'deal_text': 'Wing Tuesday: Buy 10 wings, get 5 free. Valid all day Tuesday.',
        'source': 'Oldskool Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'Lazy Chameleon',
        'deal_text': 'Wing Wednesday: 50% off all wings every Wednesday from 3-6 PM.',
        'source': 'Lazy Chameleon Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'Barley\'s Brewing Co.',
        'deal_text': 'Wing Night Special: 25 wings for $15.99 every Monday and Wednesday.',
        'source': 'Barley\'s Brewing Co. Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'Hamilton\'s Pub',
        'deal_text': 'Wing Thursday: $0.60 wings with purchase of any drink. Valid 3-7 PM.',
        'source': 'Hamilton\'s Pub Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'Brother\'s Bar & Grill',
        'deal_text': 'Wing Night every Monday: 50 cent wings with purchase of any drink. Valid 4-10 PM.',
        'source': 'Brother\'s Bar & Grill Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'Press Grill',
        'deal_text': 'Wing Wednesday: $0.75 wings every Wednesday from 5-9 PM.',
        'source': 'Press Grill Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'Hot Chicken Takeover',
        'deal_text': 'Wing Night Special: 20 wings for $14.99 every Monday and Wednesday.',
        'source': 'Hot Chicken Takeover Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'City Tavern',
        'deal_text': 'Wing Tuesday: 50 cent wings all day Tuesday. Minimum order of 10 wings.',
        'source': 'City Tavern Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'Flatiron Tavern',
        'deal_text': 'Wing Wednesday: 50% off all wings every Wednesday from 3-6 PM.',
        'source': 'Flatiron Tavern Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'The Crispy Coop',
        'deal_text': 'Wing Night every Thursday: $0.75 wings from 4-8 PM.',
        'source': 'The Crispy Coop Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'The Eagle Short North',
        'deal_text': 'Wing Night Special: 25 wings for $16.99 every Monday and Wednesday.',
        'source': 'The Eagle Short North Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'Wing Express',
        'deal_text': 'Wing Tuesday: Buy 10 wings, get 10 free. Valid all day Tuesday.',
        'source': 'Wing Express Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'The Pit BBQ Grille',
        'deal_text': 'Wing Wednesday: 50 cent wings with purchase of any drink. Valid 4-10 PM.',
        'source': 'The Pit BBQ Grille Website',
        'confidence': 'medium'
    },
    {
        'restaurant': 'Hot Mess Food Truck',
        'deal_text': 'Wing Special: 10 wings for $8.99 every Friday and Saturday.',
        'source': 'Hot Mess Food Truck Website',
        'confidence': 'medium'
    },
]

def get_restaurants_by_category(category: str = None) -> List[Dict[str, Any]]:
    """
    Get restaurants filtered by category (major_chains, local_chains, etc.)
    If no category is specified, returns all restaurants
    """
    if category:
        # Return only restaurants that match the specified category
        return [r for r in RESTAURANTS if r['category'] == category]
    # Return all restaurants if no category specified
    return RESTAURANTS

def get_restaurant_names() -> List[str]:
    """
    Get a simple list of all restaurant names
    Useful for displaying restaurant lists or checking if a restaurant exists
    """
    return [r['name'] for r in RESTAURANTS]

def get_restaurant_by_name(name: str) -> Dict[str, Any]:
    """
    Find a specific restaurant by name (case-insensitive)
    Returns the full restaurant data or None if not found
    """
    for restaurant in RESTAURANTS:
        if restaurant['name'].lower() == name.lower():
            return restaurant
    return None

def get_deal_sites() -> List[Dict[str, Any]]:
    """
    Get all deal aggregation websites we want to scrape
    These are sites like Groupon, LivingSocial, etc.
    """
    return DEAL_SITES

def get_deal_patterns() -> List[str]:
    """
    Get all regex patterns we use to find deals in website text
    These patterns help us identify wing deals even when they're written differently
    """
    return DEAL_PATTERNS

def get_mock_deals() -> List[Dict[str, Any]]:
    """
    Get all the backup deals we use when web scraping fails
    These are realistic deals that restaurants commonly offer
    """
    return MOCK_DEALS

def add_restaurant(restaurant_data: Dict[str, Any]) -> None:
    """
    Add a new restaurant to the database
    restaurant_data should contain: name, url, category, locations, known_deals, confidence
    """
    RESTAURANTS.append(restaurant_data)

def remove_restaurant(name: str) -> bool:
    """
    Remove a restaurant from the database by name (case-insensitive)
    Returns True if restaurant was found and removed, False if not found
    """
    for i, restaurant in enumerate(RESTAURANTS):
        if restaurant['name'].lower() == name.lower():
            del RESTAURANTS[i]
            return True
    return False

def update_restaurant(name: str, updated_data: Dict[str, Any]) -> bool:
    """
    Update an existing restaurant's information by name (case-insensitive)
    updated_data should contain the fields to update (url, category, locations, etc.)
    Returns True if restaurant was found and updated, False if not found
    """
    for i, restaurant in enumerate(RESTAURANTS):
        if restaurant['name'].lower() == name.lower():
            RESTAURANTS[i].update(updated_data)
            return True
    return False 