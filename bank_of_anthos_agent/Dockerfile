# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code to the working directory
COPY . .

# Expose port 8080 to the outside world
EXPOSE 8080

# Command to run the FastAPI application
# The --host 0.0.0.0 flag is crucial to accept connections from outside the container
# The --port 8080 flag matches the EXPOSE instruction and Vertex AI's requirement
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
