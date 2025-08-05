#!/usr/bin/env python3
"""
Columbus Wing Deals Scraper
A web scraper that finds chicken wing deals in Columbus, Ohio and displays them on a beautiful HTML page.

This is the main entry point that orchestrates the entire process:
1. Scrapes websites for wing deals
2. Generates a beautiful HTML page
3. Provides user-friendly output and instructions
"""

# Import system libraries for file operations and error handling
import os
import sys
# Import our custom scraper and HTML generator classes
from wing_scraper import ColumbusWingScraper
from html_generator import WingDealsHTMLGenerator

def main():
    """
    Main function that runs the complete wing deals scraper and HTML generator
    This function orchestrates the entire process from start to finish
    """
    
    # Print a nice welcome message and explain what the scraper does
    print("🍗 Columbus Wing Deals Scraper")
    print("=" * 50)
    print("This scraper will find chicken wing deals in Columbus, Ohio")
    print("and display them on a beautiful HTML page.")
    print()
    
    # Step 1: Run the web scraper to find deals
    print("Step 1: Scraping wing deals...")
    # Create a new scraper instance
    scraper = ColumbusWingScraper()
    # Run the scraper and get back all the deals it found
    deals = scraper.run_scraper()
    
    # Check if we found any deals
    if not deals:
        print("❌ No deals found. Exiting.")
        return
    
    # Print success message with the number of deals found
    print(f"✅ Found {len(deals)} wing deals!")
    print()
    
    # Step 2: Generate the beautiful HTML webpage
    print("Step 2: Generating HTML page...")
    # Create a new HTML generator instance
    generator = WingDealsHTMLGenerator()
    # Generate the HTML file with all the deals
    html_file = generator.generate_html(deals)
    
    # Print success message
    print(f"✅ Generated HTML file: {html_file}")
    print()
    
    # Step 3: Display helpful information about what was created
    print("🎉 Scraping and HTML generation complete!")
    print()
    print("📁 Generated files:")
    print(f"   • {html_file} - Beautiful HTML page with all deals")
    print(f"   • wing_deals.json - Raw deal data in JSON format")
    print(f"   • wing_deals.csv - Deal data in CSV format")
    print()
    print("🌐 To view the deals:")
    print(f"   1. Open {html_file} in your web browser")
    print("   2. Or run: python -m http.server 8000")
    print("   3. Then visit: http://localhost:8000/wing_deals.html")
    print()
    
    # Print a summary of what we accomplished
    print("📊 Summary:")
    print(f"   • Total deals found: {len(deals)}")
    # Count unique restaurants by creating a set of restaurant names
    print(f"   • Restaurants: {len(set(d['restaurant'] for d in deals))}")
    # Count high confidence deals
    print(f"   • High confidence deals: {len([d for d in deals if d['confidence'] == 'high'])}")
    print()
    print("🍗 Happy wing hunting in Columbus!")

# This code only runs if we execute this file directly
if __name__ == "__main__":
    try:
        # Run the main function
        main()
    except KeyboardInterrupt:
        # If user presses Ctrl+C, print a nice message and exit
        print("\n\n⚠️  Scraping interrupted by user.")
        sys.exit(1)
    except Exception as e:
        # If any other error occurs, print the error and exit
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1) 