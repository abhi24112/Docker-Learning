FROM python:3.13

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY streamlit_app/ /app/

COPY src/ /app/src/

COPY models/ /app/models/

COPY data/ /app/data/

EXPOSE 8500

CMD ["streamlit", "run", "app.py"]

