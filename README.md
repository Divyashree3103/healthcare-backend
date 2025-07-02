# Healthcare Backend

This is a Django + Django REST Framework backend for a healthcare system.

## Features

- JWT Authentication (Register/Login)
- Patient and Doctor Management
- Patient-Doctor Mapping APIs
- PostgreSQL database

## Tech Stack

- Django
- Django REST Framework
- PostgreSQL
- JWT Auth (SimpleJWT)

## How to Run

1. Clone the repo  
   `git clone https://github.com/Divyashree3103/healthcare-backend.git`

2. Create a virtual environment  
   `python -m venv env`

3. Activate the virtual environment  
   - On Windows: `.\env\Scripts\activate`

4. Install dependencies  
   `pip install -r requirements.txt`

5. Create a `.env` file in the root folder with:

DB_NAME=healthcare
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432

6. Run migrations  

python manage.py makemigrations
python manage.py migrate

7. Start the server  
`python manage.py runserver`

## API Endpoints

### Auth
- `POST /api/auth/register/`
- `POST /api/auth/login/`

### Patients
- `GET /api/patients/`
- `POST /api/patients/`

### Doctors
- `GET /api/doctors/`
- `POST /api/doctors/`

### Mappings
- `POST /api/mappings/`
- `GET /api/mappings/`
- `GET /api/mappings/<patient_id>/`
- `DELETE /api/mappings/<id>/`