Api de reconhecimento facial KowaBulver desenvolvida por João Machado e Ezekiel Bulver

construção do container

docker build -t seunome/recfac:2.0 .

uso do container 

docker container run -d -p 5001:5001 seunome/recfac:2.0
