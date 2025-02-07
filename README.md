# Digital Twin for Mining Simulation
This project demonstrates the concept of a Digital Twin in the mining sector using simulated data, real-time analytics, and dynamic visualizations. It showcases how mining operations such as ore extraction and transportation can be represented, monitored, and analyzed digitally using open-source tools.

## Project Features
<img width="1018" alt="Screenshot 2025-01-28 at 1 30 58 pm" src="https://github.com/user-attachments/assets/3078f80c-e598-4a80-8b57-d6476afa1a1a" />

- **Data Simulation**: Real-time generation of mining operation data (e.g., ore extracted, truck loads, machine status).
- **Database**: Storage of simulated data using SQLite.
- **Backend**: A Flask web server to serve data and provide API endpoints.
- **Frontend**: A real-time dashboard with dynamic charts powered by Plotly.
- **Analytics**: Basic calculations like average ore extraction and machine downtime alerts.

## Technology Stack
- **Programming Language**: Python
- **Web Framework**: Flask
- **Database**: SQLite
- **Visualization**: Plotly (JavaScript)
- **Operating System**: Ubuntu
- **Tools**: Python Virtual Environment

## Setup Instructions

### 1. Prerequisites
Ensure the following tools are installed on your Ubuntu system:
- Python 3.x
- SQLite
- Virtual Environment (python3-venv)
- Flask

Install them if necessary:
```
sudo apt update
sudo apt install python3 python3-pip sqlite3 git python3-venv python3-flask
```

### 2. Clone the Repository
Clone this repository to your local machine:
```
git clone https://github.com/MenakaGodakanda/digital-twin-mining.git
cd digital-twin-mining
```

### 3. Set Up a Virtual Environment
Create and activate a Python virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```
Install the required Python packages:
```
pip install flask pandas matplotlib plotly
```
### 4. Set Up the Database
Run the data generator script to create the database and populate it with initial data:
```
python app/data_generator.py
```
This script:
- Creates a table in `database/mining.db` if it doesn’t already exist.
- Simulates mining data and stores it in the database.
![Screenshot 2025-01-28 122855](https://github.com/user-attachments/assets/929bab27-9627-4b6b-9636-d9c278ce6397)

### 5. Run the Flask Application
Start the Flask web server:
```
export FLASK_APP=app
flask run
```
- The server will start at `http://127.0.0.1:5000`.
![Screenshot 2025-01-28 123132](https://github.com/user-attachments/assets/837b87e7-d130-44bb-b16c-b9487f671363)

6. Open the Dashboard
Open your web browser and navigate to:
```
http://127.0.0.1:5000
```
Here, you will see:
- A real-time chart showing ore extraction data.
- Automatic updates every 2 seconds.
- Average Ore Extraction (Green Box):
![Screenshot 2025-01-28 134126](https://github.com/user-attachments/assets/278d11ef-e337-4eeb-b8d3-21bccf4343ac)

- Downtime Alert (Red Box):
![Screenshot 2025-01-28 140408](https://github.com/user-attachments/assets/1c724cdd-c85e-4541-a138-632d2a79d4c9)

## API Endpoints
- `/`: Serves the main dashboard.
- `/api/data`: Returns the latest mining data in JSON format.

Example API Response:
![Screenshot 2025-01-28 142011](https://github.com/user-attachments/assets/008b77a7-9217-4b60-92d0-2e3652ef2f20)

## Key Features
### 1. Real-Time Data Simulation:
- Data on ore extraction, truck load, and machine status is generated every 2 seconds.

### 2. Dynamic Dashboard:
- Real-time visualization using Plotly.
- Data updates without refreshing the page.

### 3. Basic Analytics:
- Calculate the average ore extraction.
- Detect and alert on extended machine downtime.

## Screen Recording of Digital Twin for Mining Simulation
### Screen Recording 01
https://github.com/user-attachments/assets/8d40bc3f-52f5-48e0-84b2-9e3a30146620

### Screen Recording 02
https://github.com/user-attachments/assets/95108c28-b0ae-47f3-83fc-41087cc292a3

## Project Structure
```
digital-twin-mining/
├── app/
│   ├── static/          # Static files (CSS/JS)
│   ├── templates/       # HTML templates
│   ├── __init__.py      # Flask app initialization
│   ├── routes.py        # Flask routes and API endpoints
│   └── data_generator.py # Simulates mining data
├── models/              # Analytics and predictive models
│   └── prediction.py    # Model logic for analytics
├── database/            # Database files
│   └── mining.db        # SQLite database
├── scripts/             # Utility scripts (optional for extensions)
├── Dockerfile           # Optional Docker setup
└── README.md            # Documentation (this file)
```

## License

This project is licensed under the MIT License.
