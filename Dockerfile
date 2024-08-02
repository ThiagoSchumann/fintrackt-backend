# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install -r requirements.txt

# Install debugpy for debugging
RUN pip install debugpy

# Copy the rest of the application
COPY . .

# Set the environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Expose the port
EXPOSE 5000 5678

# Command to run the application with debugpy
CMD ["flask", "run", "--host=0.0.0.0"]
