FROM python:3.7

# Create and set app directory
WORKDIR /usr/src/app

COPY requirements.txt .

# install dependencies
RUN pip install -r api/requirements.txt

# Bundle app source
COPY api/main.py .

## Run application
ENTRYPOINT [ "uvicorn", "main:app", "--port", "8080" ]
