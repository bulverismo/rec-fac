FROM        bulverismo/recfac:1.1
LABEL       maintainer="KowaBulver"

WORKDIR     /app
COPY        *.py /app/
RUN         chmod a+x *.py

COPY        requirements.txt /app/
RUN         pip3 install -r requirements.txt

CMD         ["./server-reconhecimento.py"]
