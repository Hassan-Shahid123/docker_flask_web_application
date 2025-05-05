# Use official Python image
FROM python:3.13.1

# Set working directory inside container
WORKDIR /app

# Copy project files to container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port for Flask
EXPOSE 5000

# Command to run app
CMD ["python", "app.py"]
