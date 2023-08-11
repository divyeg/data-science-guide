import os
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Read CSV").getOrCreate()


file_path = os.path.join(os.getcwd(), "Datasets/sample_dataset.csv")


class DataHandler(object):
    def __init__(self):
        pass

    def read_csv(self, file_path, sep):
        df = spark.read.csv(file_path, sep=sep, header=True, inferSchema=True)
        return df
