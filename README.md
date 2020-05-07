# Info3180-project2: Photogram

Info3180-project2 Photogram, an instagram clone

## Setup

#### Setup virtual environment and installation of dependencies

```bash

    $ python -m venv venv
    $ source venv/bin/activate (linux/MacOS)
    $ source venv\Scripts\activate (windows)
    $ pip install -r requirements.txt

```
<br>

#### Generate local test database

```bash

    $ python generate_testdb.py

```
*Note: Well generate based on environment variables*

## Environment Variables

**Required**
BASEDIR
UPLOADS_FOLDER
DB_NAME
DB_USER
DB_PASSWORD
DB_URI

**Optional (Flask)**
FLASK_ENV
FLASK_APP
FLASK_DEBUG

## Start Flask Server

```bash

    $ flask run

```
