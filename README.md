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

 pip install apache-beam[gcp]

 spark-shell  # for spark-scala :q to quit
 pyspark # for pyspark shell 
 spark-submit test-pyspart.py # direct submission to pyspark
 spark-submit test-beamrunner.py --runner=SparkRunner # submission to beam

 stop-all.sh
```

Check the link for spark details : http://localhost:8080/

TODO :
* https://towardsdatascience.com/diy-apache-spark-docker-bb4f11c10d24
* https://beam.apache.org/documentation/runners/spark/
* https://0x0ece.medium.com/a-quick-demo-of-apache-beam-with-docker-da98b99a502a