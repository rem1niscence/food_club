NAME='django_server'
DJANGO_DIR='/food_club/django'
NUM_WORKERS=3
DJANGO_WSGI_MODULE=config.wsgi

cd $DJANGO_DIR

# Set up Django looking for changes
./manage.py collectstatic --noinput
./manage.py migrate --noinput


# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn $DJANGO_WSGI_MODULE:application \
    --name $NAME \
    --bind 0.0.0.0:8000 \
    --workers $NUM_WORKERS \
    --log-level=info \
    --reload
    --access-logfile - 
    --error-logfile -
