FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5001 

RUN adduser -D user
USER user

ENTRYPOINT [ "python" ] 
CMD ["app.py"]
