FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

## install dependencies 

# copy requirements.txt from local machine to docker 
COPY ./requirements.txt /requirements.txt

# install contents of docker requirements.txt in docker
RUN pip3 install -r /requirements.txt

# create a directory to store application source code
RUN mkdir /recipeapp
WORKDIR /recipeapp
COPY ./recipeapp /recipeapp/

# create a user to run application code using docker
RUN adduser -D user
# switch to the user
USER user