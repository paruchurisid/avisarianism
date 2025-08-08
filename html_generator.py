import json
from datetime import datetime
from typing import List, Dict, Any

class WingDealsHTMLGenerator:
    def __init__(self):
        self.html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Columbus Wing Deals - Best Chicken Wing Specials</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }

        .header {
            background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }

        .header h1 {
            font-size: 3rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .header p {
            font-size: 1.2rem;
            opacity: 0.9;
        }

        .stats-bar {
            background: #f8f9fa;
            padding: 20px;
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            border-bottom: 1px solid #e9ecef;
        }

        .stat-item {
            text-align: center;
            padding: 10px;
        }

        .stat-number {
            font-size: 2rem;
            font-weight: bold;
            color: #ff6b6b;
        }

        .stat-label {
            color: #6c757d;
            font-size: 0.9rem;
        }

        .filters {
            padding: 20px;
            background: #f8f9fa;
            border-bottom: 1px solid #e9ecef;
        }

        .filter-group {
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
            align-items: center;
        }

        .filter-btn {
            padding: 8px 16px;
            border: 2px solid #ff6b6b;
            background: white;
            color: #ff6b6b;
            border-radius: 25px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 500;
        }

        .filter-btn:hover, .filter-btn.active {
            background: #ff6b6b;
            color: white;
        }

        .deals-container {
            padding: 20px;
        }

        .deal-card {
            background: white;
            border: 1px solid #e9ecef;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 20px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .deal-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 5px;
            height: 100%;
            background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        }

        .deal-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        }

        .deal-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 15px;
        }

        .restaurant-name {
            font-size: 1.5rem;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 5px;
        }

        .confidence-badge {
            padding: 4px 12px;
            border-radius: 15px;
            font-size: 0.8rem;
            font-weight: bold;
            text-transform: uppercase;
        }

        .confidence-high {
            background: #d4edda;
            color: #155724;
        }

        .confidence-medium {
            background: #fff3cd;
            color: #856404;
        }

        .confidence-low {
            background: #f8d7da;
            color: #721c24;
        }

        .deal-text {
            font-size: 1.1rem;
            line-height: 1.6;
            color: #495057;
            margin-bottom: 15px;
        }

        .deal-meta {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.9rem;
            color: #6c757d;
        }

        .source-info {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .source-icon {
            width: 16px;
            height: 16px;
            background: #ff6b6b;
            border-radius: 50%;
        }

        .no-deals {
            text-align: center;
            padding: 60px 20px;
            color: #6c757d;
        }

        .no-deals h3 {
            font-size: 1.5rem;
            margin-bottom: 10px;
        }

        .footer {
            background: #2c3e50;
            color: white;
            text-align: center;
            padding: 30px;
            margin-top: 40px;
        }

        .footer p {
            margin-bottom: 10px;
        }

        .footer a {
            color: #ff6b6b;
            text-decoration: none;
        }

        .footer a:hover {
            text-decoration: underline;
        }

        @media (max-width: 768px) {
            .header h1 {
                font-size: 2rem;
            }
            
            .stats-bar {
                flex-direction: column;
                gap: 15px;
            }
            
            .filter-group {
                justify-content: center;
            }
            
            .deal-header {
                flex-direction: column;
                gap: 10px;
            }
            
            .deal-meta {
                flex-direction: column;
                gap: 10px;
                align-items: flex-start;
            }
        }

        .loading {
            text-align: center;
            padding: 40px;
            color: #6c757d;
        }

        .spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #ff6b6b;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 20px;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🍗 Columbus Wing Deals</h1>
            <p>Find the best chicken wing specials and deals in Columbus, Ohio</p>
        </div>

        <div class="stats-bar">
            <div class="stat-item">
                <div class="stat-number" id="total-deals">0</div>
                <div class="stat-label">Total Deals</div>
            </div>
            <div class="stat-item">
                <div class="stat-number" id="restaurants">0</div>
                <div class="stat-label">Restaurants</div>
            </div>
            <div class="stat-item">
                <div class="stat-number" id="high-confidence">0</div>
                <div class="stat-label">High Confidence</div>
            </div>
        </div>

        <div class="filters">
            <div class="filter-group">
                <button class="filter-btn active" data-filter="all">All Deals</button>
                <button class="filter-btn" data-filter="high">High Confidence</button>
                <button class="filter-btn" data-filter="medium">Medium Confidence</button>
                <button class="filter-btn" data-filter="low">Low Confidence</button>
                <button class="filter-btn" data-filter="tuesday">Tuesday Deals</button>
                <button class="filter-btn" data-filter="wednesday">Wednesday Deals</button>
                <button class="filter-btn" data-filter="thursday">Thursday Deals</button>
                <button class="filter-btn" data-filter="weekend">Weekend Deals</button>
            </div>
        </div>

        <div class="deals-container" id="deals-container">
            <div class="loading">
                <div class="spinner"></div>
                <p>Loading wing deals...</p>
            </div>
        </div>
    </div>

    <div class="footer">
        <p>🍗 Columbus Wing Deals - Your guide to the best wing specials in Columbus, Ohio</p>
        <p>Last updated: <span id="last-updated">Loading...</span></p>
        <p>Data sourced from restaurant websites and deal aggregation sites</p>
    </div>

    <script>
        // Load deals data from embedded JSON
        const dealsData = {{DEALS_DATA}};
        
        // Display deals immediately
        displayDeals(dealsData);
        updateStats(dealsData);
        document.getElementById('last-updated').textContent = new Date().toLocaleString();

        function displayDeals(deals, filter = 'all') {
            const container = document.getElementById('deals-container');
            
            if (deals.length === 0) {
                container.innerHTML = '<div class="no-deals"><h3>No Deals Found</h3><p>No wing deals found matching your criteria.</p></div>';
                return;
            }

            const filteredDeals = filterDeals(deals, filter);
            
            container.innerHTML = filteredDeals.map(deal => `
                <div class="deal-card">
                    <div class="deal-header">
                        <div>
                            <div class="restaurant-name">${deal.restaurant}</div>
                        </div>
                        <span class="confidence-badge confidence-${deal.confidence}">${deal.confidence}</span>
                    </div>
                    <div class="deal-text">${deal.deal_text}</div>
                    <div class="deal-meta">
                        <div class="source-info">
                            <div class="source-icon"></div>
                            <span>${deal.source}</span>
                        </div>
                        <span>Found: ${formatDate(deal.date_found)}</span>
                    </div>
                </div>
            `).join('');
        }

        function filterDeals(deals, filter) {
            if (filter === 'all') return deals;
            
            return deals.filter(deal => {
                const text = deal.deal_text.toLowerCase();
                const confidence = deal.confidence;
                
                switch(filter) {
                    case 'high':
                        return confidence === 'high';
                    case 'medium':
                        return confidence === 'medium';
                    case 'low':
                        return confidence === 'low';
                    case 'tuesday':
                        return text.includes('tuesday');
                    case 'wednesday':
                        return text.includes('wednesday');
                    case 'thursday':
                        return text.includes('thursday');
                    case 'weekend':
                        return text.includes('friday') || text.includes('saturday') || text.includes('sunday');
                    default:
                        return true;
                }
            });
        }

        function updateStats(deals) {
            const totalDeals = deals.length;
            const restaurants = new Set(deals.map(d => d.restaurant)).size;
            const highConfidence = deals.filter(d => d.confidence === 'high').length;
            
            document.getElementById('total-deals').textContent = totalDeals;
            document.getElementById('restaurants').textContent = restaurants;
            document.getElementById('high-confidence').textContent = highConfidence;
        }

        function formatDate(dateString) {
            const date = new Date(dateString);
            return date.toLocaleDateString() + ' ' + date.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
        }

        // Filter button functionality
        document.addEventListener('DOMContentLoaded', function() {
            const filterButtons = document.querySelectorAll('.filter-btn');
            
            filterButtons.forEach(button => {
                button.addEventListener('click', function() {
                    // Remove active class from all buttons
                    filterButtons.forEach(btn => btn.classList.remove('active'));
                    // Add active class to clicked button
                    this.classList.add('active');
                    
                    // Get the filter value
                    const filter = this.getAttribute('data-filter');
                    
                    // Apply filter to embedded data
                    displayDeals(dealsData, filter);
                });
            });
        });
    </script>
</body>
</html>
        """
    
    def generate_html(self, deals: List[Dict[str, Any]], output_file: str = 'wing_deals.html'):
        """
        Generate HTML file with embedded deals data
        This embeds the JSON data directly into the HTML so it works when opened locally
        """
        # Convert deals to JSON string for embedding
        deals_json = json.dumps(deals, indent=2)
        
        # Replace placeholder with actual data
        html_content = self.html_template.replace('{{DEALS_DATA}}', deals_json)
        
        # Write to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Generated HTML file: {output_file}")
        return output_file

def main():
    """Main function to generate HTML from JSON data"""
    try:
        # Load deals from JSON file
        with open('wing_deals.json', 'r', encoding='utf-8') as f:
            deals = json.load(f)
        
        # Generate HTML
        generator = WingDealsHTMLGenerator()
        html_file = generator.generate_html(deals)
        
        print(f"Successfully generated HTML file with {len(deals)} deals!")
        print(f"Open {html_file} in your web browser to view the deals.")
        
    except FileNotFoundError:
        print("Error: wing_deals.json not found. Please run the scraper first.")
    except Exception as e:
        print(f"Error generating HTML: {str(e)}")

if __name__ == "__main__":
    main() 