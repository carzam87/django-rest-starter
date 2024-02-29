
import os
from pathlib import Path
from dotenv import load_dotenv

import cloudinary
import cloudinary.uploader
import cloudinary.api	

load_dotenv()

# SECURITY WARNING: make sure to change this in your railway variables from the default one
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Edit the following line and place your railway URL, and your custom URL in the array.
CSRF_TRUSTED_ORIGINS = [
    "https://*.up.railway.app", 
    # NOTE: Place your custom url here if any
]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("PGDATABASE"),
        "USER": os.getenv("PGUSER"),
        "PASSWORD": os.getenv("PGPASSWORD"),
        "HOST": os.getenv("PGHOST"),
        "PORT": os.getenv("PGPORT"),
    }
}


cloudinary.config( 
  	cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME"),
  	api_key = os.getenv("CLOUDINARY_API_KEY"),
  	api_secret = os.getenv("CLOUDINARY_API_SECRET")
)