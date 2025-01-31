# Project Installation and Running Instructions

Follow these steps to run the project.

## Prerequisites

Ensure you have the following installed:

- Python (version 3.11+)
- [uv](https://github.com/lyz-code/uv) (for running the Django project easily)

### 1. Install `uv` if Not Installed

If `uv` is not installed, you can install it using `pip`:

```bash
pip install uv
```

### 2. Running the Project

To run the Django development server using uv run, execute the following command in the project directory:

```bash
uv run manage.py runserver
```

- This will start the Django development server, and the project should be accessible at http://127.0.0.1:8000/ in your browser.

### 3. Creating a Superuser (Optional)

If you need to create a superuser to access the Django admin panel, run the following command:

```bash
uv run manage.py createsuperuser
```

Follow the prompts to set the superuser's username, email, and password.

### 4. Accessing the Admin Panel

Once the server is running, you can access the Django admin panel at:

```bash
http://127.0.0.1:8000/admin/
```

Use the superuser credentials you created in the previous step to log in.
