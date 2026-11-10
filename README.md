# Smart Matatu Fare Tracker

## About the Project
Smart Matatu Fare Tracker is a web-based application designed to help commuters estimate matatu fares for selected routes in Nairobi, Kenya.

The project aims to make fare information easier to access and help commuters plan their transport expenses.

## Project Objectives
- Provide estimated matatu fares for selected routes.
- Help commuters plan their transport budgets.
- Build a simple and user-friendly fare tracking system.
- Support future expansion to more routes.

## Current Features
- Fare estimation for selected routes.
- Peak-hour fare adjustment.
- Display of estimated fares in Kenyan Shillings (KES).
- Simple web interface.

## Technologies Used
- Python
- Flask
- MySQL
- HTML
- CSS
- JavaScript
- Git and GitHub

## Project Structure
```text
Smart Matatu Fare Tracker/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   └── templates/
│       └── index.html
│
├── .gitignore
├── requirements.txt
├── run.py
└── README.md
```

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/Sharly-tec1/smart-matatu-fare-tracker.git
```

2. Enter the project folder:

```bash
cd smart-matatu-fare-tracker
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Run the application:

```bash
python run.py
```

## Initial Route Coverage
The initial development includes the Thika to Nairobi CBD route, with estimated fares.

More routes will be added as development continues.

## Important Note
The displayed fares are development estimates only. Actual matatu fares may vary depending on route, time, traffic, and other operating conditions.

## Future Improvements
- Add more Nairobi routes.
- Improve fare estimation accuracy.
- Integrate additional MySQL database functionality.
- Improve the user interface.
- Expand coverage to other regions.

## Developer
Developed as a personal software development project.

**GitHub Repository:**  
https://github.com/Sharly-tec1/smart-matatu-fare-tracker

**Project Status:** Under Development