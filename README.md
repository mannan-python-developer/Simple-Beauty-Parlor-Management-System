# Beauty Parlor Management System

This is a simple Beauty Parlor Management System implemented using Django, designed to streamline the management and organization of beauty parlor operations. The system includes features such as appointment scheduling, customer management, and service tracking.

## Features

- **Appointment Scheduling:** Easily schedule and manage appointments for customers.
- **Customer Management:** Maintain a database of customer profiles with contact details and service history.
- **Service Tracking:** Keep track of services provided, including details like service type, duration, and cost.
- **User-Friendly Interface:** Intuitive web interface for easy navigation and use.

## Getting Started

Follow these steps to run the Beauty Parlor Management System on your local machine:

### Prerequisites

1. **Install Python:** Ensure that Python is installed on your machine. Download it from [python.org](https://www.python.org/downloads/).

2. **Install Django:** Install Django using the following command:
   ```bash
   pip install django
---

## Clone and Setup

1. **Clone the Repository:**
   Clone this repository to your local machine using the following command:
   ```bash
   git clone https://github.com/mannan258/Simple-Beauty-Parlor-Management-System.git

2. **Run Migrate and Migrations:**
  Apply database migrations to set up the database.
    ```bash
    python manage.py migrate
    ```
    ```bash
    python manage.py makemigrations
    ```

3. **Create Superuser (Optional):**
    Create an admin superuser for accessing the admin interface.
   ```bash
   python manage.py createsuperuser
   ```
---

## Run the Development Server

1. **Start the Server:**
   Launch the Django development server.
   ```bash
   python manage.py runserver
    ```
   
2. **Access the Application:**
  Open your browser and go to http://127.0.0.1:8000/ to access the Beauty Parlor Management System.

### Note!

Feel free to customize the commands and adjust settings based on your specific project requirements. Happy managing!


