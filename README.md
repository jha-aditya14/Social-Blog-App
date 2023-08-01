# Social-Blog-App

# Description

Social Blog App is a web application built with Django and PostgreSQL that allows users to create and share their blog posts with a community of like-minded individuals. It provides a platform for users to express their thoughts, ideas, and experiences through written content and engage in discussions with other users.

# Key Features
1. User Authentication: Secure user registration and login system powered by Django's built-in authentication framework to protect user data and ensure a personalized experience.
2. Create and Publish Blogs: Users can easily compose and publish their blogs with a user-friendly editor.
3. Read and Interact: Browse through a feed of blog posts from other users and interact by liking and commenting on their posts.
4. User Profiles: Each user has a dedicated profile page to showcase their published blogs and engagement statistics.
5. Follow Users: Follow other users to stay updated with their latest posts and activities.
6. Categories and Tags: Organize blogs into different categories and add relevant tags for easy navigation and discovery.
7. Search Functionality: Search for specific blogs or topics of interest across the platform.
8. Responsive Design: The app is designed to be responsive and accessible across various devices.
Getting Started

- To get started with the Social Blog App, follow the instructions below:

## Clone the Repository:

1. git clone https://github.com/your-username/social-blog-app.git
2. cd social-blog-app
3. Install Dependencies: Make sure you have Python and pip installed. Then, create a virtual environment and install the required dependencies:

python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt

## Configure PostgreSQL Database:

Create a PostgreSQL database and update the database settings in the settings.py file:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

## Run Migrations:

Apply the database migrations to create the necessary tables: python manage.py migrate

- Start the Development Server:

- Run the following command to start the development server: python manage.py runserver

## Access the App:

Open your web browser and visit http://localhost:8000 to access the Social Blog App.

## Technologies Used
Django - Python Web Framework
PostgreSQL - Relational Database Management System
HTML, CSS, JavaScript - Front-end
Bootstrap - Front-end Framework

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to create a pull request or open an issue in the repository.

## License
This project is licensed under the MIT License.

## External Databse using for site
$env:DATABASE_URL = "postgres://blog:tM28cTbZTWLEWXl8Y6zvvLx7vyJiHhqc@dpg-cia7btmnqql8alje2jbg-a.oregon-postgres.render.com/socialblogapp"