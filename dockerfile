# Use the official Python image from DockerHub
FROM python:3.11-slim

# Set working directory in the container
WORKDIR /app

# Copy all files into the container
COPY . /app

# Set the default command to run your game
CMD ["python", "game.py"]
