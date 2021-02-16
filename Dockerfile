FROM python:3.6.1-alpine
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
ENV FLASK_APP app/main.py
CMD ["python"]
CMD ["flask", "run", "--host=0.0.0.0"]
