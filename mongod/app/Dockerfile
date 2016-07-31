FROM python:3.5

# Install the mongodb python library
RUN pip install pymongo fake-factory

# Copy the application folder
COPY ./src /app

# Enter in to the app
ENTRYPOINT python /app/app.py
