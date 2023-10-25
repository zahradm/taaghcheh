# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install the project dependencies
RUN pip install -r requirements.txt

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "taaghche_api.wsgi:application"]
