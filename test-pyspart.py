from pyspark import SparkConf, SparkContext

#sc = pyspark.SparkContext() # Cannot create multiple spark context

from pyspark.sql import SparkSession
sc = SparkSession.builder.\
    master('local').\
    appName('foo').\
    getOrCreate()
#sc.sparkContext.setLogLevel('WARN')

sc = SparkContext.getOrCreate()
result = (
    sc.parallelize([1, 2, 3, 4])
    .map(lambda x: x * 2)
    .reduce(lambda x, y: x + y)
)
print(result)