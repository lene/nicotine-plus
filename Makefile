.PHONY: install lint mypy
.DEFAULT_GOAL := all

ifeq ($(PREFIX),)
    PREFIX := /usr/local
endif

SRC = nicotine pynicotine plugins
VIRTUAL_ENV = .venv

all: install lint mypy

install:
	poetry run pip install -U pip
	poetry install

install-macos:
	poetry env use 3.8.2
	brew install gtk+3 pygobject3 gobject-introspection libGeoIP
	PKG_CONFIG_PATH=/usr/local/Cellar/libffi/3.3/lib/pkgconfig make install
	# FIXME: No such file or directory: '/usr/local/var/GeoIP/GeoIP.dat'
	poetry run pip uninstall -y geoip

install-ubuntu:
	apt-get install -y python3 python3-pip python3-venv gcc \
		miniupnpc xdg-utils libgtk-3-0 libcairo2-dev libgirepository1.0-dev libgeoip-dev gobject-introspection gir1.2-gtk-3.0
	make install

lint:
	isort --recursive ${SRC}
	flake8 ${SRC} --ignore=E501,E402,W504,W503
	mypy ${SRC}

test:
	pylint ${SRC}

image:
	docker build -t nicotine -f docker/Dockerfile.python3 --network=host .