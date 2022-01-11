FROM python:3.6-buster
WORKDIR /app
# RUN pip3 install -r /app/requirements.txt
# COPY ./scripts/seed.py /app/scripts/seed.py
# RUN python /app/scripts/seed.py
COPY . /app/


RUN pip3 install -r requirements.txt

RUN python ./scripts/seed.py

# ENTRYPOINT [""]
# CMD ["python", "manage.py", "runserver"]
# CMD ["python", "main.py"]
CMD ["gunicorn","--bind","0.0.0.0:5000","main:application"]
# ENTRYPOINT ["gunicorn","application:application"]
# ENTRYPOINT ["gunicorn","--bind","0.0.0.0:5000","main:application"]
# ENTRYPOINT ["gunicorn","--bind","0.0.0.0:5000","main:app"]
# ENTRYPOINT ["gunicorn main:app --bind=0.0.0.0:3000"]