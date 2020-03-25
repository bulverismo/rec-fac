FROM        bulverismo/recfac:1.1
LABEL       maintainer="KowaBulver"
RUN         pip3 install flask
RUN         pip3 install flask_cors

WORKDIR     /app
COPY        criaDat.py /app/
RUN         chmod a+x criaDat.py
COPY        server-reconhecimento.py /app/
RUN         chmod a+x server-reconhecimento.py

ENTRYPOINT  ["./server-reconhecimento.py"]
