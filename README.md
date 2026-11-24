# Django Study Notes

A Django project (`mysite`) with one app (`notes`): add study notes per course,
mark them revised, filter by course, and manage everything in Django's admin.

- **Run** installs Django (`pip install -r requirements.txt`), creates the SQLite
  database the first time (`python manage.py migrate`) and starts
  `python manage.py runserver`. The live preview opens at `localhost:8000`.
- Saving a file restarts the server, like runserver's reloader.
- For the admin at `/admin/`, create an account first: stop the server with
  Ctrl+C, then run `python manage.py createsuperuser`.
- After changing `notes/models.py`, run `python manage.py makemigrations`
  and `python manage.py migrate`.
- `python manage.py shell` opens Python with the project loaded.
