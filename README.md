# Ice Cream Parlor

This is a simple Python application for managing a fictional ice cream parlor using Flask and SQLite.

## Getting Started

### Prerequisites
- Docker
- Python 3.9
- pip

### Running the Application

1. **Build and run the Docker container**
    ```
    docker build -t ice_cream_parlor .
    docker run -p 5000:5000 ice_cream_parlor
    ```

2. **Access the application**
    Open your web browser and navigate to `http://localhost:5000`

### Testing the Application

1. **Initialize the database**
    ```
    python database.py
    ```

2. **Run the Flask application**
    ```
    python app.py
    ```
### Code Documentation

- `database.py` - Contains functions to connect to the SQLite database and create the required tables.
- `models.py` - Contains classes with methods to interact with the database tables.
- `app.py` - Contains the Flask application with API endpoints to manage the ice cream parlor.
- `templates` - Contains all the html templates for the basic frontend
