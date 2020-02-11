RUN apt-get update
RUN apt-get install python
RUN apt-get -y install python-pip
RUN pip install --user flask
RUN pip install --user request
ADD ./server/ /usr/src
