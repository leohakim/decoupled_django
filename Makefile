.ONESHELL:

djangoDev:
	bash ./run-dev.sh

billingForm:
	npm run serve --prefix ./billing/vue_spa/

blogNextJs:
	cd ./next-blog/ && npm run dev

cypressTest:
	./node_modules/.bin/cypress open

drfTest:
	export DJANGO_SETTINGS_MODULE=decoupled_dj.settings.testing
	pytest