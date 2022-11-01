FROM python:3.10.4

ENV PYTHONUNBUFFERED=1

WORKDIR /FORM_APP
COPY requirements.txt ./
RUN  python -m pip install pip==22.2.2
RUN  pip install -r requirements.txt
COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
