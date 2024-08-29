# My MiniBlog Project

![Django](https://img.shields.io/badge/Django-5+-green.svg)
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5+-orange.svg)

## Description

This is a fully functional blog application built with **Python** and **Django** for the backend, and **HTML**, **CSS**, and **Bootstrap** for the frontend. The application allows users to create, read, update, and delete blog posts. It includes features such as user authentication, commenting, and more, offering a complete blogging experience.

## Features

- **User Authentication**: Users can sign up, log in, and manage their profiles.
- **CRUD Operations**: Full support for creating, reading, updating, and deleting blog posts.
- **Commenting System**: Users can comment on posts.
- **Search Functionality**: Search for posts by title or content.
- **Pagination**: Blog posts are paginated for better navigation.
- **Responsive Design**: Fully responsive design using Bootstrap, ensuring the blog looks good on all devices.
- **Admin Panel**: Django's built-in admin panel for managing the blog content.

## Quick Start

To quickly set up the project, follow these steps. You can copy and paste everything into your terminal:

```bash
# Clone the Repository
git clone https://github.com/yourusername/your-blog-repo.git
cd your-blog-repo

# Create and Activate a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install Dependencies
pip install -r requirements.txt

# Apply Migrations
python manage.py migrate

# Create a Superuser
python manage.py createsuperuser

# Run the Development Server
python manage.py runserver

# Access the Blog in your browser
# Open http://127.0.0.1:8000/ to view the blog.
