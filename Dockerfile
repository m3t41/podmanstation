FROM python:3.12 
# Or any preferred Python version.
USER root
RUN apt-get update
RUN apt-get -y install podman
ADD start.py .
ADD requirements.txt .
RUN pip install -r requirements.txt

CMD ["python3", "./start.py"] 
# Or enter the name of your unique directory and parameter set.
