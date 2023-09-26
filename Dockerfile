FROM python:3.8-alpine

# Copy the requirements file into the image
COPY ./app/requirements.txt /app/requirements.txt

WORKDIR /app

# Install the dependencies specified in the requirements file
RUN pip install -r requirements.txt

# Copy app contents to the image
COPY app/ /app

EXPOSE 5000

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
