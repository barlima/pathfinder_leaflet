# Pathfinder Leaflet

Prepared as a training before creating a proper application.

## Running the application

### Prerequisites

Make sure you have installed **Python 3.6**, **pip3** and **django**. In case you haven't, run the below commands.

**For Ubuntu Linux:**
```
apt-get install python3
apt-get install python3-pip
pip3 install django
```

Go to the directory where you would like to download the projects.
```
git clone git@github.com:barlima/pathfinder_leaflet.git
```

### Setup static folder location

Add full path of static folder location to **django_leaflet/settings.py**.

```
cd pathfinder_leaflet/static
pwd
```
Copy the result and paste it to **settings.py**
```
STATICFILES_DIRS = [
    '/home/bartek/MyProjects/Leaflet_tutorial/django_leaflet/static',
    [PATH_TO_STATIC_DIR]
]
```

### Run the server

Go to **pathfinder_leaflet** dir and run:
```
python3 manage.py runserver
```

To check if the application is working properly go to [127.0.0.1:8000/map](htto://127.0.0.1:8000/map).
Please make sure that the server is running on port 8000.
