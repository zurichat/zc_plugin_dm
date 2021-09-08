#Build script for testing locally.
# 
#static files route set to localhost
#export BASE_URL="http://127.0.0.1:8000/static"

# change to frontend directory and build app with npm
cd frontend
yarn run build

# change to root folder and run django dev server
cd ..
python manage.py collectstatic
python manage.py runserver