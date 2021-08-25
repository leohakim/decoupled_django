source venv/bin/activate
export DJANGO_SETTINGS_MODULE=decoupled_dj.settings.development
export STATIC_URL=static
echo $DJANGO_SETTINGS_MODULE
uvicorn decoupled_dj.asgi:application --reload
