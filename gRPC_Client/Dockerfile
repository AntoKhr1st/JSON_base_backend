FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
# тестовый запрос с помощью библиотеки клиента к серверу на сохранение тестовых данных.
# данные можно скоррективароть в файле upload_test.py
#CMD ["python", "upload_test.py"]
