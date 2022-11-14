FROM python:3.9-buster
ENV PROJECT_ROOTDIR /app

WORKDIR ${PROJECT_ROOTDIR}

RUN apt-get update && apt-get install -y \
  curl \
  git

COPY ./api/requirements.txt ${PROJECT_ROOTDIR}/
COPY ./api ${PROJECT_ROOTDIR}/
RUN pip install -r requirements.txt
CMD ["python",  "-m" "debugpy" "--listen" "0.0.0.0:5678" "-m" "app" "--wait-for-client" "--multiprocess" "-m" "app.py"]
