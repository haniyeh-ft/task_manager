

# Task Manager

This is a prioritized list of tasks that need to be completed for the Task Manager project. Use this list to keep track of your progress and ensure that all tasks are completed.

- User Authentication: Secure user authentication and authorization.
   - login by phone number and password
   - session based
- Task Management: Create, update, delete, and view tasks.
- Task Assignments: Assign tasks to multiple users.
   - Only allow the assigned user to modify or delete a task.
- Filtering: Filter tasks by title, creation date, priority, and status.
- API Endpoints: RESTful API endpoints for interacting with:
   - Tasks
   - Users


## Build and Run

SetUp venv:
   ```bash
   python3 -m venv venv_taskmanager
   source venv_taskmanager/bin/activate
   ```

Get the project:

   ```bash
   git clone https://github.com/haniyeh-ft/task_manager.git
   ```

Install dependencies:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

Run database:
   ```bash
   docker-compose up -d
   ```

Apply database migrations:

   ```bash
   //go to the scr directory//
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py createsuperuser
   ```

Start the development server:

   ```bash
   python3 manage.py runserver
   ```

Access the application in your web browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).


## API Documentation

The API documentation is available at [http://127.0.0.1:8000/api/schema/swagger/](http://127.0.0.1:8000/api/schema/swagger/) when the server is running.

## Testing

To run tests, use the following command:

```bash
python3 manage.py test
```
