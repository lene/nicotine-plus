.PHONY: install lint mypy
.DEFAULT_GOAL := all

DEV = 1

all: install lint mypy

install:
	poetry run pip install -U pip
	poetry install `if [ "${DEV}" = "0" ]; then echo "--no-dev --no-interaction --no-ansi"; fi`
	poetry run python install_data.py || sh

install-macos:
	poetry env use 3.8.2
	brew install coreutils gtk+3 pygobject3 gobject-introspection libGeoIP miniupnpc
	ln -s /usr/local/bin/ginstall .venv/bin/install
	PKG_CONFIG_PATH=/usr/local/Cellar/libffi/3.3/lib/pkgconfig make install

install-ubuntu:
	apt update; apt install -y miniupnpc xdg-utils libgtk-3-0 libcairo2-dev libgirepository1.0-dev libgeoip-dev gobject-introspection gir1.2-gtk-3.0
	make install

lint:
	isort --recursive src tests
	flake8 src tests --ignore=E501,E402,W504,W503
	mypy src tests

test:
	pytest

docker-build:
	docker-compose build nicotine

docker-up:
	docker-compose up nicotine