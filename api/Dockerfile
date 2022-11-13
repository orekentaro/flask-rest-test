FROM python:3.9-buster
ENV PROJECT_ROOTDIR /app

WORKDIR ${PROJECT_ROOTDIR}

RUN apt-get update && apt-get install -y \
  curl \
  git

COPY ./api/requirements.txt ${PROJECT_ROOTDIR}/
COPY ./api ${PROJECT_ROOTDIR}/
RUN pip install -r requirements.txt
# CMD [ "uwsgi", "--ini", "app.ini"]
CMD [ "python", "app.py"]