FROM python:alpine3.15
WORKDIR /app
RUN apk add py3-pip
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]