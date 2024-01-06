# Use a Python base image
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Copy your Python script and other necessary files
COPY . .

# Install the required Python libraries
RUN pip install -r requirements.txt

EXPOSE 8000

# Command to run your Python script
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
#uvicorn main:app --reload
