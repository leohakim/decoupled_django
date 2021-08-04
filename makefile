.ONESHELL:

development:
	export DJANGO_SETTINGS_MODULE=decoupled_dj.settings.development
	uvicorn decoupled_dj.asgi:application
