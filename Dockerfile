FROM python:3.10.9
LABEL maintainer="ishanshrestha"
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1
WORKDIR /app

# install pipenv
RUN pip install --upgrade pip
RUN pip install pipenv


COPY Pipfile Pipfile.lock /app/


RUN pipenv install --system --dev

# copy app to image
COPY . /app/

# expose container port
EXPOSE 8000