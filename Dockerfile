FROM        bulverismo/recfac:1.1
LABEL       maintainer="KowaBulver"

RUN         pip3 install flask
RUN         pip3 install flask_cors

WORKDIR     /app
COPY        *.py /app/
RUN         chmod a+x *.py

COPY        requirements.txt /app/
RUN         pip3 install -r requirements.txt

CMD         ["./server-reconhecimento.py"]
