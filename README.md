# Flask_App

### Creating virtual environment for new project.
    
   Activate Python env:
   ```
   ./env/scripts/activate
   ```

### Install the following packages into local env:

   ```
   pip install flask
   
   pip install flask-sqlalchemy
   ```

### Create the database db_name in Postgres we need here for our application

### Create configurations and edit app.py
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/db_name'
    
### In the local enviroment run:
    $ python
    >>> from app import db
    >>> db.create_all()

### Run the app
   ```
   python app.py
   ```
   
