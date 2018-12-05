# Pull base image
FROM python:3.6

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code
ADD requirements.txt /code/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /code/Pipfile
RUN pipenv install -r requirements.txt
RUN pipenv install --system --skip-lock

# Copy project
COPY . /code/