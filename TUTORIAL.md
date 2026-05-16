# Tutorial: Reproducible Setup for Coffee Shop Finder

## Prerequisites
- Python 3.10+
- Git

## Step-by-Step Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/fairyfemirins/coffee-finder.git
   cd coffee-finder
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install flask
   ```

4. **Run the app:**
   ```bash
   python app.py
   ```

5. **Access the app:**
   Open `http://localhost:5015` in your browser.

## Testing the App
1. Use the filters to search for coffee shops in **San Francisco** or **New York**. 
2. Click on map markers to see details.
3. Adjust filters to refine results.

## Troubleshooting
- **Port already in use:** Change the port in `app.py` (e.g., `port=5016`).
- **No results:** Ensure the city name matches the mock data (e.g., "San Francisco").