FROM python:3.10

WORKDIR /app
COPY /src /src
RUN pip install -r requirements.txt
EXPOSE 5100
CMD ["python", "src/app.py"]