# Django Portfolio Project

This is a personal portfolio website built with Django. The project showcases my work, skills, and professional journey. It includes an about section, portfolio items, and contact information.

## Features

- **Dynamic portfolio**: Manage and display projects dynamically through the admin panel.
- **Skills section**: Highlight technical and soft skills.
- **Contact form**: Allow visitors to reach out through an email form.
- **Responsive design**: Fully functional on all device sizes.
- **Admin panel**: Manage content easily through Django's admin interface.

## Technologies Used

- **Backend**: Django 5
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Database**: SQLite (default) / PostgreSQL (optional)

## Getting Started

### Prerequisites

To run this project locally, you will need:

- Python
- Django
- SQLite (default) or PostgreSQL
- Virtualenv (optional but recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/abdelrahmanemadismail/portfolio
   cd portfolio
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations to set up the database:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser for the admin panel:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Visit the site at [http://localhost:8000](http://localhost:8000).

### Configuration

- Update the settings in `settings.py` for production (e.g., allowed hosts, database settings).
- For PostgreSQL, modify the `DATABASES` section in `settings.py` as follows:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

## Deployment

You can deploy this project using platforms like Heroku, AWS, or any other server that supports Django.

1. Set up the necessary environment variables (e.g., `DJANGO_SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`).
2. Apply static file settings using Django's `collectstatic` command.

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

---

### Contact

If you have any questions or feedback, feel free to reach out:

- **Name**: Abdelrahman Ismail
- **Email**: abdelrahman.e.ismail@gmail.com
- **LinkedIn**: [Your LinkedIn Profile](https://linkedin.com/in/abdelrahmanemadismail)