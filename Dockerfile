FROM python:3.12
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y python3-pip python3-cffi
RUN pip install -r requirements.txt
COPY . /app
COPY entrypoint.sh /entrypoint.sh
COPY start.sh /start.sh
RUN chmod +x /entrypoint.sh
ENV PYTHONUNBUFFERED 1
#ENTRYPOINT ["/entrypoint.sh"]
RUN python manage.py collectstatic
CMD ["gunicorn", "src.wsgi:application", "--bind", "0.0.0.0:8000"]
