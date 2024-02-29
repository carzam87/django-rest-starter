import os
from pathlib import Path

import cloudinary
import cloudinary.uploader
import cloudinary.api	

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: make sure to change this in your railway variables from the default one
SECRET_KEY = os.environ["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# Edit the following line and place your railway URL, and your custom URL in the array.
CSRF_TRUSTED_ORIGINS = [
    "https://*.up.railway.app", 
    # NOTE: Place your custom url here if any
]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ["PGDATABASE"],
        "USER": os.environ["PGUSER"],
        "PASSWORD": os.environ["PGPASSWORD"],
        "HOST": os.environ["PGHOST"],
        "PORT": os.environ["PGPORT"],
    }
}


cloudinary.config( 
  	cloud_name = os.environ["CLOUDINARY_CLOUD_NAME"],
  	api_key = os.environ["CLOUDINARY_API_KEY"],
  	api_secret = os.environ["CLOUDINARY_API_SECRET"]
)