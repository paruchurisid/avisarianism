# 🍗 Columbus Wing Deals Scraper

A comprehensive web scraper that finds the best chicken wing deals in Columbus, Ohio and displays them on a beautiful, modern HTML page.

## Features

- **Web Scraping**: Automatically scrapes restaurant websites and deal aggregation sites
- **Smart Pattern Matching**: Uses regex patterns to identify wing deals and specials
- **Beautiful HTML Display**: Modern, responsive web page with filtering and search
- **Multiple Data Formats**: Exports to JSON and CSV for further analysis
- **Confidence Scoring**: Rates deal reliability (high/medium/low confidence)
- **Interactive Filters**: Filter deals by day of week, confidence level, and more

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd avisarianism
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the scraper**
   ```bash
   python main.py
   ```

4. **View the results**
   - Open `wing_deals.html` in your web browser
   - Or start a local server: `python -m http.server 8000`
   - Then visit: `http://localhost:8000/wing_deals.html`

## 📁 Project Structure

```
avisarianism/
├── main.py                  # Main script to run everything
├── wing_scraper.py          # Web scraping logic
├── html_generator.py        # HTML page generator
├── restaurant_data.py       # Restaurant database and data management
├── manage_restaurants.py    # Interactive restaurant management tool
├── requirements.txt         # Python dependencies
├── README.md               # This file
├── wing_deals.html         # Generated HTML page (after running)
├── wing_deals.json         # Raw deal data (after running)
└── wing_deals.csv          # CSV format data (after running)
```

## 🔧 How It Works

### 1. Web Scraping (`wing_scraper.py`)
- Scrapes popular wing restaurant websites
- Searches deal aggregation sites (Groupon, LivingSocial)
- Uses pattern matching to identify wing deals
- Generates realistic mock deals for demonstration
- Saves data in JSON and CSV formats

### 2. HTML Generation (`html_generator.py`)
- Creates a modern, responsive HTML page
- Includes interactive filtering and search
- Displays deals with confidence ratings
- Shows statistics and metadata
- Mobile-friendly design

### 3. Restaurant Data Management (`restaurant_data.py`)
- Centralized database of all restaurant information
- Easy to add, remove, or update restaurants
- Categorized by type (major chains, local chains, independent, etc.)
- Includes deal patterns and mock data

### 4. Restaurant Management Tool (`manage_restaurants.py`)
- Interactive command-line tool for managing restaurants
- Add new restaurants with full details
- Remove or update existing restaurants
- View statistics and restaurant information

### 5. Main Script (`main.py`)
- Orchestrates the entire process
- Provides user-friendly output
- Handles errors gracefully

## 🍗 Sample Deals

The scraper finds deals like:
- **Buffalo Wild Wings**: BOGO Wings every Tuesday
- **Wingstop**: 50% off wings on Wednesdays
- **Wings Over Columbus**: $0.75 wings during happy hour
- **Roosters**: 50 cent wings on Thursdays
- **Quaker Steak & Lube**: All-you-can-eat wings on Mondays
- **Average Joe's**: 50 cent wings on Mondays
- **Lucky's Grille**: $0.75 wings on Wednesdays
- **Wing Snob**: 50% off wings on Thursdays
- **King of Wings**: 20 wings for $12.99
- **Hot Mess Food Truck**: 10 wings for $8.99 on weekends

## 🎨 HTML Features

- **Modern Design**: Beautiful gradient backgrounds and card layouts
- **Responsive**: Works on desktop, tablet, and mobile
- **Interactive Filters**: Filter by day, confidence level, restaurant
- **Statistics Dashboard**: Shows total deals, restaurants, and confidence levels
- **Real-time Updates**: Displays when data was last updated
- **Smooth Animations**: Hover effects and transitions

## 📊 Data Format

Each deal includes:
```json
{
  "restaurant": "Restaurant Name",
  "deal_text": "Description of the deal",
  "source": "Where the deal was found",
  "date_found": "2024-01-15 14:30:00",
  "confidence": "high|medium|low"
}
```

## 🔍 Filtering Options

- **All Deals**: Show everything
- **High Confidence**: Only verified deals
- **Medium/Low Confidence**: Less certain deals
- **Day-specific**: Tuesday, Wednesday, Thursday, Weekend deals

## 🛠️ Customization

### Managing Restaurants
Use the interactive management tool:
```bash
python manage_restaurants.py
```

This provides an easy menu to:
- List all restaurants
- Add new restaurants
- Remove restaurants
- Update restaurant information
- View statistics

### Adding New Restaurants Programmatically
Edit `restaurant_data.py` and add to the `RESTAURANTS` list:
```python
{
    'name': 'New Restaurant',
    'url': 'https://restaurant-website.com',
    'category': 'independent',
    'locations': ['Columbus'],
    'known_deals': ['Wing specials', 'Daily deals'],
    'confidence': 'medium'
}
```

### Modifying Deal Patterns
Update the `DEAL_PATTERNS` list in `restaurant_data.py`:
```python
DEAL_PATTERNS = [
    r'wing.*deal',
    r'wing.*special',
    # Add your patterns here
]
```

### Styling Changes
Edit the CSS in `html_generator.py` to customize the appearance.

## ⚠️ Important Notes

- **Rate Limiting**: The scraper includes delays to be respectful to websites
- **Anti-Bot Measures**: Some websites may block automated requests
- **Mock Data**: For demonstration, the scraper generates realistic sample deals
- **Legal Compliance**: Always respect websites' robots.txt and terms of service

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**: Make sure all dependencies are installed
   ```bash
   pip install -r requirements.txt
   ```

2. **No Deals Found**: The scraper will generate sample deals if web scraping fails

3. **HTML Not Loading**: Ensure `wing_deals.json` exists before running the HTML generator

4. **Permission Errors**: Make sure you have write permissions in the directory

### Getting Help

- Check that all required packages are installed
- Ensure you have internet connectivity for web scraping
- Verify Python version is 3.7 or higher

## 📈 Future Enhancements

- [ ] Add more restaurant sources
- [ ] Implement price tracking over time
- [ ] Add location-based filtering
- [ ] Create mobile app version
- [ ] Add user reviews and ratings
- [ ] Implement email notifications for new deals

## 🤝 Contributing

Feel free to contribute by:
- Adding new restaurant sources
- Improving the scraping logic
- Enhancing the HTML design
- Adding new features

## 📄 License

This project is for educational purposes. Please respect website terms of service when scraping.

---

**🍗 Happy wing hunting in Columbus, Ohio!** 🍗