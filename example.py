from pyspark.sql import Row, SparkSession

spark = SparkSession.builder.appName("SnowparkConnectExample").getOrCreate()

df = spark.createDataFrame([
    Row(a=1, b=2.0),
    Row(a=2, b=3.0),
    Row(a=3, b=4.0)
])

df.show()
