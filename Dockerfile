# choose image from docker hub
FROM tiangolo/uwsgi-nginx-flask:python3.8

# environment variable specific to this Docker image
# defines static dir where assets such as images, CSS, and JavaScripts files
# are served from.
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static

# copy file to container and install
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /var/www/requirements.txt

# Add app
COPY ./SCRAPYMike /app
WORKDIR /app
