# The Kendalls Wedding Website

A beautiful wedding website built with Vue.js frontend and Flask backend, using SQLite database for RSVP management.

## Project Structure

```
Wedding/
├── frontend/          # Vue.js application
│   ├── src/
│   │   ├── views/    # Page components (Home, RSVP)
│   │   ├── App.vue   # Main app component
│   │   ├── main.js   # App entry point
│   │   └── style.css # Global styles
│   ├── index.html
│   ├── vite.config.js
│   └── package.json
│
└── backend/           # Flask API server
    ├── app.py        # Main Flask application
    ├── requirements.txt
    └── wedding.db    # SQLite database (created on first run)
```

## Features

- 🏠 **Home Page**: Beautiful landing page with wedding details
- 💌 **RSVP System**: Guests can submit their RSVP with dietary restrictions and messages
- 📊 **API Endpoints**: RESTful API for RSVP management
- 💾 **SQLite Database**: Persistent storage for all guest responses
- 🎨 **Elegant Design**: Modern, responsive design with custom color scheme

## Prerequisites

- Python 3.8+
- Node.js 18+
- npm or yarn

## Setup Instructions

### 1. Backend Setup

Navigate to the backend directory and install dependencies:

```bash
cd backend
pip install -r requirements.txt
```

Start the Flask server:

```bash
python app.py
```

The backend will run on `http://localhost:5000`. The database will be automatically created on first run.

### 2. Frontend Setup

In a new terminal, navigate to the frontend directory:

```bash
cd frontend
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will run on `http://localhost:5173`.

## Usage

1. Open your browser and go to `http://localhost:5173`
2. Navigate through the Home page to view wedding details
3. Click "RSVP" or navigate to the RSVP page to submit guest information
4. All RSVP data is saved to the SQLite database in the backend

## API Endpoints

- `POST /api/rsvp` - Submit a new RSVP
- `GET /api/rsvp` - Get all RSVPs
- `GET /api/rsvp/<id>` - Get a specific RSVP by ID
- `GET /api/stats` - Get RSVP statistics (total, attending, guests count)
- `GET /api/health` - Health check endpoint

## Database Schema

The RSVP table includes:
- `id` - Auto-incrementing primary key
- `name` - Guest name (required)
- `email` - Guest email (required)
- `phone` - Guest phone number (optional)
- `guests` - Number of guests (required)
- `attending` - Yes/No attendance status (required)
- `dietary` - Dietary restrictions (optional)
- `message` - Message to the couple (optional)
- `created_at` - Timestamp of RSVP submission

## Customization

### Change Wedding Details

Edit [frontend/src/views/Home.vue](frontend/src/views/Home.vue) to update:
- Wedding date
- Venue information
- Ceremony and reception times
- Couple's story

### Modify Colors

The color scheme uses a purple gradient. To change:
- Edit the gradient colors in [frontend/src/App.vue](frontend/src/App.vue) and [frontend/src/views/Home.vue](frontend/src/views/Home.vue)
- Update button and accent colors throughout the Vue components

### Database Location

By default, the SQLite database is created at `backend/wedding.db`. To change the location, modify the `DB_PATH` variable in [backend/app.py](backend/app.py).

## Development

### Frontend Development
- Built with Vue 3 and Vite
- Uses Vue Router for navigation
- Axios for API requests
- Responsive design with mobile support

### Backend Development
- Flask with Flask-CORS for cross-origin requests
- SQLite for database
- RESTful API design

## Production Deployment

For production deployment:

1. **Frontend**: Run `npm run build` in the frontend directory to create optimized production build
2. **Backend**: Use a production WSGI server like Gunicorn instead of Flask's development server
3. **Database**: Consider migrating to PostgreSQL or MySQL for production use
4. **Environment**: Set up proper environment variables and remove debug mode

## Troubleshooting

### Backend won't start
- Ensure Python 3.8+ is installed
- Check that all requirements are installed: `pip install -r requirements.txt`
- Verify port 5000 is not in use

### Frontend won't start
- Ensure Node.js 18+ is installed
- Delete `node_modules` and run `npm install` again
- Check that port 5173 is available

### RSVP submission fails
- Verify backend is running on port 5000
- Check browser console for error messages
- Ensure database file has write permissions

## License

This project is created for the Kendalls' wedding celebration.

## Contact

For questions or issues, please contact the site administrator.
