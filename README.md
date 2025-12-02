# pg_recommendation
A backend service for recommending Paying Guest (PG) accommodations based on location, price, and preferences. Built using **FastAPI**, **SQLAlchemy**, and **SQLite**. 

## Table of Contents

- Features
- Technologies
- Project Structure
- Installation
- Usage
- API Endpoints
- License


## Features

- List all PGs
- Get details of a specific PG
- Create, update, and delete PG entries
- Recommend PGs based on location and price
- Load PG dataset from CSV

---

## Technologies

- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite
- Pandas (for dataset loading)

## Project Structure
[Structure](pg_recommendation_structure.jpg)


## Installation

1. Clone the repository:

```bash
git clone https://github.com/KapilTheAnalyst/pg_recommendation.git
cd pg_recommendation
```

2. Create a virtual environment (    using venv or conda):
```
python -m venv venv

or

conda create -n pg_env python=3.10
```
3. Activate the environment:
```
venv\Scripts\activate
conda activate pg_env
```
4.Install dependencies:
```
pip install -r requirements.txt
```
## Usage
1. Load dataset (CSV) into database: 
```
python backend/load_data.py
```

2. Run the FastAPI server:
```
uvicorn backend.main:app --reload
```
3. Open the API documentation in browser:
```
http://127.0.0.1:8000/docs
```
[API Endpoints](api-end-point-pg-recommendation.jpg)


# License

This project is licensed under the MIT License.

Author: Kapil Chauhan

GitHub: https://github.com/KapilTheAnalyst

Linkedin: https://www.linkedin.com/in/kapil-kumar11/ 
