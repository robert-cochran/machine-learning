FROM python:3

RUN mkdir -p /var/app
WORKDIR /var/app
COPY . /var/app

# installs sscipy, numpy and all rqrd pckgs
RUN pip install scipy numpy && \
    pip install .
