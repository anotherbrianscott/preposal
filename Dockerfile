FROM python:3.7

# Create and set app directory
WORKDIR /usr/src/app

COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# Bundle app source
COPY main.py .

## Run application
CMD [ "uvicorn", "main:app", "--port", "8080" ]
