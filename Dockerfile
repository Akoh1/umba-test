FROM python:3.6-buster
WORKDIR /app
# COPY ./requirements.txt /app/requirements.txt
# RUN pip3 install -r /app/requirements.txt
# COPY ./scripts/seed.py /app/scripts/seed.py
# RUN python /app/scripts/seed.py
COPY . /app/
# install environment dependencies
RUN pip3 install --upgrade pip 
RUN pip3 install virtualenv

# create virtualenvironment
RUN virtualenv -p python3 .virtualenv
RUN . .virtualenv/bin/activate

RUN pip3 install -r requirements.txt
RUN python ./scripts/seed.py
EXPOSE 3000
# ENTRYPOINT [""]
# CMD ["python", "manage.py", "runserver"]
CMD ["python", "app.py"]