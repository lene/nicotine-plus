FROM python:latest
ARG DEV=0

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
RUN export PATH="$HOME/.poetry/bin:$PATH"; poetry config virtualenvs.create false

WORKDIR /nicotine
COPY poetry.lock pyproject.toml Makefile install_data.py /nicotine/

RUN make prepare-deb

RUN mkdir -p /nicotine/src/pynicotine && mkdir -p /nicotine/src/pynicotine_plugins && touch /nicotine/src/pynicotine/__init__.py && touch /nicotine/src/pynicotine_plugins/__init__.py
RUN export PATH="$HOME/.poetry/bin:$PATH"; make install DEV=$DEV

COPY . /nicotine

ENTRYPOINT ["nicotine"]
