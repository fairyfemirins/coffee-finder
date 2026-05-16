# White Paper: Coffee Shop Finder for Digital Nomads

## Problem Statement
Digital nomads struggle to find work-friendly coffee shops in new cities. Existing platforms (e.g., Yelp, Google Maps) lack filters for **Wi-Fi quality, outlet availability, and work-friendly vibes**.

## Solution
A **web-based tool** that:
- Filters coffee shops by **Wi-Fi, outlets, coffee quality, and vibe**. 
- Displays results on a **map** for easy navigation.
- Supports **crowdsourced reviews** for accuracy.

## Design Decisions
1. **Flask + SQLite:** Lightweight, easy to deploy, and scalable for small datasets.
2. **Leaflet.js:** Open-source mapping library for interactive maps.
3. **Mock Data:** Initial dataset for testing and demonstration.
4. **Responsive Frontend:** Works on mobile and desktop.

## Future Work
- **User Submissions:** Allow users to add coffee shops and reviews.
- **Real-Time Availability:** Show how busy a coffee shop is.
- **Reservations:** Integrate with booking platforms.

## Conclusion
This app fills a gap for **digital nomads** by providing a **specialized, filterable, and map-based** coffee shop finder.