# base image
FROM python:3.13.11

# working directory
WORKDIR /app

# copy
COPY . /app

# run 
RUN pip install -r requirements.txt

# port expose
EXPOSE 8000

# command
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]