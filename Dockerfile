FROM        bulverismo/recfac:1.1
LABEL       maintainer="KowaBulver"

WORKDIR     /app
COPY        criaDat.py /app/
RUN         chmod a+x criaDat.py
COPY        server-reconhecimento.py /app/
RUN         chmod a+x server-reconhecimento.py

ENTRYPOINT  ["./server-reconhecimento.py"]
