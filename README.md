# DB-Hotel-Project
This project is a component of the database subject, wherein we utilize Django as the backend to design and implement a database application for a real-world business, specifically a hotel.

## Requirements

Requires Python 3.8 and later.  Required Python packages are listed in [requirements.txt](./requirements.txt). 

## Installation and Configuration

1. Open a command-line interface

2. Create a Virtual Environment
    ```bash
    python -m venv venv
    ```

3. Activate the Virtual Environment
- On MacOS or Linux
    ```bash
    source venv/bin/activate
    ```
- On Windows
    ```cmd
    venv\Scripts\activate
    ```

1. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```


5. Run migrations
    ```bash
    python manage.py migrate
    ```

6.  Load data from the data fixtures
    ```bash
    python manage.py loaddata data/users.json
    python manage.py loaddata data/hotel.json
    ```

7.  Run server
    ```bash
    python manage.py runserver
    ```

### How to Run

1. Activate the Virtual Environment
- On MacOS or Linux
    ```bash
    source venv/bin/activate
    ```
- On Windows
    ```cmd
    venv\Scripts\activate
    ```

2. Start the Django Development Server
    ```bash
    python manage.py runserver
    ```
    If you receive an error message indicating that the port is unavailable, try running the server on a different port (1024 thru 65535), such as
    ```bash
    python manage.py runserver 12345
    ```

3. Navigate to http://localhost:8000 in your web browser.
   
4. To stop the server, press **Ctrl-C** / **control-C** in the terminal window.

5. Exit the virtual environment by closing the window or typing
    ```bash
    deactivate
    ```
## Demo Accounts

### Demo Admin

| Username  |    Password    |
|:---------:|:--------------:|
|   admin   |     admin      |
