# spark-setup-run

Install the cluster on linux as described (here)[https://phoenixnap.com/kb/install-spark-on-ubuntu]
```
 sudo apt install default-jdk scala git -y
 java -version; javac -version; scala -version; git --version

 wget https://archive.apache.org/dist/spark/spark-3.0.3/spark-3.0.3-bin-hadoop2.7.tgz
 tar xvf spark-3.0.3-bin-hadoop2.7.tgz
 sudo mv spark-3.0.3-bin-hadoop2.7/ /opt/spark
 sudo nano ~/.profile
 source ~/.profile
 start-master.sh
 start-slave.sh -c 1 -m 256M spark://6730b:7077

 stop-all.sh
```