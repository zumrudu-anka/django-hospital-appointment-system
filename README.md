# gitHub-finder
🏥 📅 💻 Hospital Appointment System With Django

### Installation

- Clone this repo to your local machine using `https://github.com/zumrudu-anka/django-hospital-appointment-system.git`
- Go to the project folder
- run `python -m venv myvenv` for create virtual environment which name is myvenv
- activate virtual environment:
  
> Windows:
> myvenv/Scripts/activate.bat

> Linux:
> source myvenv/Scripts/activate

- run `pip install -r requirements.txt`
- run `python manage.py makemigrations`
- run `python manage.py migrate`
- run `python manage.py addCities`
- run `python manage.py addCounties`
- run `python manage.py createsuperuser` for create super user and enter username and password. You can pass email field

### Usage

- run `python manage.py runserver`
- Go to main page and create new patient to login the system.