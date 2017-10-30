# Pathfinder Leaflet

Prepared as a training before creating a proper application.


## Running the application

### Prerequisites

Make sure you have installed **Python 3.6**, **pip3**, **django**, **nodejs** and **npm**. In case you haven't, run the commands below.

**For Ubuntu Linux:**
```
apt-get install python3 python3-pip nodejs npm
pip3 install django
```

Go to the directory where you would like to download the projects.
```
git clone git@github.com:barlima/pathfinder_leaflet.git
```


### Required repositories

Clone the [OSRM](https://github.com/Project-OSRM/osrm-backend) repository to your working directory and [build it from source](https://github.com/Project-OSRM/osrm-backend#building-from-source).

Make sure that **NodeJS** and **npm** have been installed successfully.
Install [Leaflet Routing Machine](https://github.com/Project-OSRM/osrm-backend#building-from-source) package and connect it with the **pathfinder_leaflet** application.

At the end you should have a directory structure looking like this:
```
Working directory:
- pathfinder_leaflet/static/node_modules/leaflet_routing_machine
- osrm-backend
```


### Setup static folder location

Add full path of static folder location to **django_leaflet/settings.py**.

```shell
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


## Run the server

Go to **pathfinder_leaflet** dir and run:
```shell
python3 manage.py runserver
```

To check if the application is working properly go to [127.0.0.1:8000/map](htto://127.0.0.1:8000/map).
Please make sure that the server is running on port 8000.
