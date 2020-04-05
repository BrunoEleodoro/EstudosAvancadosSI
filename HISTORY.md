```
   1  git clone https://github.com/BrunoEleodoro/EstudosAvancadosSI.git
    2  cd EstudosAvancadosSI/
    3  cd ambiente_seguro/
    4  ls
    5  clear
    6  cd ..
    7  git pull origin master
    8  cd ambiente_seguro/
    9  ls
   10  clear
   11  docker-compose up -d
   12  docker logs ambiente_seguro_www_1 
   13  clear
   14  docker logs ambiente_seguro_db_1 
   15  docker logs ambiente_seguro_www_1 
   16  docker logs ambiente_seguro_www_1 
   17  docker logs ambiente_seguro_www_1 
   18  cd ..i
   19  git pull origin master
   20  docker-compose down
   21  docker-compose up -d
   22  docker-compose up -d --force-recreate --build
   23  docker logs ambiente_seguro_www_1 
   24  docker-compose downn
   25  docker-compose down
   26  docker-compose up -d --force-recreate --build
   27  docker logs ambiente_seguro_www_1 
   28  docker-compose down && git pull origin master && docker-compose up -d --force-recreate --build
   29  docker logs ambiente_seguro_www_1 
   30  docker-compose down && git pull origin master && docker-compose up -d --force-recreate --build
   31  clear
   32  docker run --rm -it -v /tmp/sqlmap:/root/.sqlmap/ paoloo/sqlmap --url www.example.com/?id=1 
   33  docker run --rm -it -v /tmp/sqlmap:/root/.sqlmap/ paoloo/sqlmap --url http://ip172-18-0-17-bq4gidroudsg00f8che0-80.direct.labs.play-with-docker.com/teste?id=1
   34  docker run --rm -it -v /tmp/sqlmap:/root/.sqlmap/ paoloo/sqlmap --url http://ip172-18-0-17-bq4gidroudsg00f8che0-80.direct.labs.play-with-docker.com/teste?id=1 --level
   35  docker run --rm -it -v /tmp/sqlmap:/root/.sqlmap/ paoloo/sqlmap --url http://ip172-18-0-17-bq4gidroudsg00f8che0-80.direct.labs.play-with-docker.com/teste?id=1 --level 3
   36  clear
   37  docker-compose downn
   38  docker-compose down
   39  clear
   40  cd ..
   41  cd ambiente_inseguro/
   42  docker-compose up
   43  clear
   44  docker-compose up -d
   45  clear
   46  docker run --rm -it -v /tmp/sqlmap:/root/.sqlmap/ paoloo/sqlmap --url http://ip172-18-0-17-bq4gidroudsg00f8che0-80.direct.labs.play-with-docker.com/teste?id=1
   47  clear
   48  docker-compose down
   49  cd ..
   50  cd ambiente_seguro/e
   51  cd ambiente_seguro/
   52  ls
   53  clear
   54  docker-compose up -d
   55  docker run --rm -it -v /tmp/sqlmap:/root/.sqlmap/ paoloo/sqlmap --url http://ip172-18-0-17-bq4gidroudsg00f8che0-80.direct.labs.play-with-docker.com/teste?id=1 --level 5
   56  rm -rf /tmp/sqlmap/
   57  docker run --rm -it -v /tmp/sqlmap:/root/.sqlmap/ paoloo/sqlmap --url http://ip172-18-0-17-bq4gidroudsg00f8che0-80.direct.labs.play-with-docker.com/teste?id=1 --level 5
   58  history
```