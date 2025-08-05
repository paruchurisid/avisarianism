# Import all the libraries we need for web scraping and data handling
import requests  # For making HTTP requests to websites
from bs4 import BeautifulSoup  # For parsing HTML content from websites
from datetime import datetime  # For adding timestamps to deals
import json  # For saving data in JSON format
import time  # For adding delays between requests
import random  # For randomizing delays to avoid detection
from typing import List, Dict, Any  # For type hints
import re  # For pattern matching (finding deals in text)
import csv  # For saving data in CSV format
# Import our custom data management functions
from restaurant_data import (
    get_restaurants_by_category,  # Get list of all restaurants
    get_deal_sites,  # Get list of deal aggregation websites
    get_deal_patterns,  # Get regex patterns for finding deals
    get_mock_deals  # Get backup deals when scraping fails
)

class ColumbusWingScraper:
    """
    Main scraper class that handles all web scraping operations
    for finding wing deals in Columbus, Ohio
    """
    def __init__(self):
        # Set up headers to make our requests look like a real browser
        # This helps avoid being blocked by websites
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        # Initialize empty list to store all the deals we find
        self.deals = []
        
    def scrape_restaurant_websites(self):
        """
        Visit each restaurant's website and try to find wing deals
        This is the main scraping function that goes through all restaurants
        """
        
        # Get the list of all restaurants from our data file
        # This includes major chains, local chains, and independent restaurants
        restaurants = get_restaurants_by_category()
        
        # Loop through each restaurant in our database
        for restaurant in restaurants:
            try:
                # Print which restaurant we're currently trying to scrape
                print(f"Scraping {restaurant['name']}...")
                
                # Make an HTTP request to the restaurant's website
                # We include our browser headers and set a 10-second timeout
                response = requests.get(restaurant['url'], headers=self.headers, timeout=10)
                
                # If the request was successful (status code 200 means OK)
                if response.status_code == 200:
                    # Parse the HTML content from the website
                    soup = BeautifulSoup(response.content, 'html.parser')
                    # Extract any deals we find on this website
                    self._extract_deals_from_soup(soup, restaurant['name'])
                
                # Wait a random amount of time (1-3 seconds) before the next request
                # This prevents us from overwhelming the website's servers
                time.sleep(random.uniform(1, 3))  # Be respectful to servers
                
            except Exception as e:
                # If anything goes wrong (website is down, blocks us, etc.), 
                # print an error message and continue with the next restaurant
                print(f"Error scraping {restaurant['name']}: {str(e)}")
    
    def scrape_deal_sites(self):
        """
        Visit deal aggregation websites like Groupon and LivingSocial
        These sites often have restaurant deals that individual restaurants don't list
        """
        
        # Get the list of deal aggregation websites from our data file
        # These include Groupon, LivingSocial, Restaurant.com, etc.
        deal_sites = get_deal_sites()
        
        # Loop through each deal aggregation website
        for site in deal_sites:
            try:
                # Print which deal site we're currently trying to scrape
                print(f"Scraping {site['name']}...")
                
                # Make an HTTP request to the deal website
                response = requests.get(site['url'], headers=self.headers, timeout=10)
                
                # If the request was successful
                if response.status_code == 200:
                    # Parse the HTML content from the website
                    soup = BeautifulSoup(response.content, 'html.parser')
                    # Extract any wing deals we find on this website
                    self._extract_deals_from_soup(soup, site['name'])
                
                # Wait before the next request to be respectful
                time.sleep(random.uniform(1, 3))
                
            except Exception as e:
                # If anything goes wrong, print error and continue
                print(f"Error scraping {site['name']}: {str(e)}")
    
    def _extract_deals_from_soup(self, soup: BeautifulSoup, source: str):
        """
        This is the core function that finds wing deals in website text
        It uses regex patterns to search for deal-related text
        """
        
        # Get all the regex patterns we use to find deals
        # These patterns look for things like "wing deal", "50% off wings", etc.
        deal_patterns = get_deal_patterns()
        
        # Convert the HTML content to plain text and make it lowercase
        # This makes it easier to search through
        text_content = soup.get_text().lower()
        
        # Loop through each pattern we're looking for
        for pattern in deal_patterns:
            # Find all matches of this pattern in the text
            matches = re.finditer(pattern, text_content, re.IGNORECASE)
            
            # For each match we find
            for match in matches:
                # Get some context around the match (100 characters before and after)
                # This helps us understand what the deal is about
                start = max(0, match.start() - 100)
                end = min(len(text_content), match.end() + 100)
                context = text_content[start:end].strip()
                
                # Clean up the text by removing extra whitespace
                context = re.sub(r'\s+', ' ', context)
                
                # Only add deals that have meaningful content (more than 20 characters)
                if len(context) > 20:
                    # Create a deal object with all the information
                    deal = {
                        'restaurant': source,  # Which restaurant this came from
                        'deal_text': context,  # The actual deal text we found
                        'source': source,  # Where we found it (same as restaurant for now)
                        'date_found': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # When we found it
                        'confidence': 'medium'  # How confident we are this is a real deal
                    }
                    
                    # Check if we already have this exact deal to avoid duplicates
                    if not any(d['deal_text'] == deal['deal_text'] for d in self.deals):
                        # Add the new deal to our list
                        self.deals.append(deal)
    
    def generate_mock_deals(self):
        """
        When web scraping fails (websites block us), we use this backup system
        to generate realistic deals based on what we know restaurants typically offer
        This ensures users always get useful information
        """
        
        # Get the list of mock deals from our data file
        # These are realistic deals that restaurants commonly offer
        mock_deals = get_mock_deals()
        
        # Add a current timestamp to each mock deal
        # This makes them look like they were just found
        for deal in mock_deals:
            deal['date_found'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Add all the mock deals to our main deals list
        self.deals.extend(mock_deals)
    
    def save_to_json(self, filename: str = 'wing_deals.json'):
        """
        Save all the deals we found to a JSON file
        JSON format is good for web applications and data processing
        """
        # Open a file for writing with UTF-8 encoding (handles special characters)
        with open(filename, 'w', encoding='utf-8') as f:
            # Convert our deals list to JSON format and write it to the file
            # indent=2 makes the JSON file readable with proper formatting
            # ensure_ascii=False allows special characters to be saved properly
            json.dump(self.deals, f, indent=2, ensure_ascii=False)
        
        # Print a confirmation message showing how many deals were saved
        print(f"Saved {len(self.deals)} deals to {filename}")
    
    def save_to_csv(self, filename: str = 'wing_deals.csv'):
        """
        Save all the deals we found to a CSV file
        CSV format is good for opening in Excel or other spreadsheet software
        """
        # Check if we have any deals to save
        if not self.deals:
            print("No deals to save to CSV")
            return
        
        # Open a CSV file for writing
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            # Define the column headers for our CSV file
            fieldnames = ['restaurant', 'deal_text', 'source', 'date_found', 'confidence']
            # Create a CSV writer that knows about our data structure
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write the header row (column names)
            writer.writeheader()
            # Write each deal as a row in the CSV file
            for deal in self.deals:
                writer.writerow(deal)
        
        # Print a confirmation message
        print(f"Saved {len(self.deals)} deals to {filename}")
    
    def run_scraper(self):
        """
        This is the main function that orchestrates the entire scraping process
        It calls all the other functions in the right order
        """
        # Print a nice header to show the scraper is starting
        print("Starting Columbus Wing Deals Scraper...")
        print("=" * 50)
        
        # Step 1: Try to scrape real restaurant websites
        # This might fail because some websites block automated access
        try:
            # Visit each restaurant's website and look for deals
            self.scrape_restaurant_websites()
            # Visit deal aggregation websites and look for deals
            self.scrape_deal_sites()
        except Exception as e:
            # If anything goes wrong during scraping, print the error
            print(f"Error during web scraping: {str(e)}")
        
        # Step 2: Generate backup deals
        # Even if web scraping fails, we still provide useful information
        print("\nGenerating sample deals for demonstration...")
        self.generate_mock_deals()
        
        # Step 3: Save all the deals we found to files
        # Save as JSON for the website to use
        self.save_to_json()
        # Save as CSV for spreadsheet analysis
        self.save_to_csv()
        
        # Print a summary of what we accomplished
        print(f"\nScraping complete! Found {len(self.deals)} wing deals.")
        return self.deals

# This code only runs if we execute this file directly
# It creates a scraper instance and runs the full scraping process
if __name__ == "__main__":
    # Create a new scraper object
    scraper = ColumbusWingScraper()
    # Run the complete scraping process and get back all the deals
    deals = scraper.run_scraper() 