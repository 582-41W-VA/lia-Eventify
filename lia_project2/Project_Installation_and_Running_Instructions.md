# Project Installation and Running Instructions

Follow these steps to run the project.

## Prerequisites

Ensure you have the following installed:

- Python (version 3.11+) (Check by running python --version in your terminal)
- [uv](https://github.com/lyz-code/uv) (for running the Django project easily)
  To install uv, follow the steps below.

## Steps to Run the Project

### 1. Clone the Project Repository

If you haven't already, clone the repository to your local machine:

```bash
git clone https://github.com/your-repository-link.git
cd your-project-directory
```

### 2. Install `uv` if Not Installed

If `uv` is not installed, you can install it using `pip`:

```bash
pip install uv
```

### 3. Running the Project

To run the Django development server using uv run, execute the following command in the project directory:

```bash
uv run manage.py runserver
```

- This will start the Django development server, and the project should be accessible at http://127.0.0.1:8000/ in your browser.

### 4. Creating a Superuser (Optional)

If you need to create a superuser to access the Django admin panel, run the following command:

```bash
uv run manage.py createsuperuser
```

Follow the prompts to set the superuser's username, email, and password.

### 5. Accessing the Admin Panel

Once the server is running, you can access the Django admin panel at:

```bash
http://127.0.0.1:8000/admin/
```

Use the superuser credentials you created in the previous step to log in.

### 6. (Optional) Managing Database Migrations

If you've made changes to the models and need to apply database migrations, run the following commands:

```bash
uv run manage.py makemigrations
uv run manage.py migrate
```

This ensures that any database schema changes are reflected in the database.
