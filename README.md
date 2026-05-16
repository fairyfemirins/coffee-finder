# Coffee Shop Finder

## Overview
A **web-based tool** for digital nomads to find the ideal coffee shop to work from in new cities.
- **Filters:** Wi-Fi, outlets, coffee quality, and vibe.
- **Map Integration:** Show nearby coffee shops with filters.
- **User Reviews:** Crowdsourced ratings and tips.

## Technical Architecture
- **Backend:** Flask + SQLite.
- **Frontend:** HTML/CSS/JS + Leaflet.js (for maps).
- **Database:** SQLite (for coffee shop data and reviews).

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/fairyfemirins/coffee-finder.git
   cd coffee-finder
   ```
2. Install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open `http://localhost:5015` in your browser.

## Usage
- Use filters to find coffee shops that match your needs.
- Click on map markers to see details.

## License
MIT License.