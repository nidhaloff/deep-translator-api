FROM python:3.8  

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


COPY . /app

#EXPOSE 5000

CMD ["python", "src/main.py"]
