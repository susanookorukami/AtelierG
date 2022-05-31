
# Slim version of Python
FROM python:3.8.12-slim

#Work directory
WORKDIR /AtelierG

# Copy the csv file data
COPY pizza.csv pizza.csv

# Download Package Information
RUN apt-get update -y

# Install Tkinter
RUN apt-get install tk -y

# Commands to run Tkinter application
CMD ["/AtelierG/pizza.py"]
ENTRYPOINT ["python3"]