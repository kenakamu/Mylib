import pyspark
from pyspark.sql.functions import *
from datetime import *

def addLineage(df):
    df = df.withColumn("_loadDate", lit(datetime.now()))
    df = df.withColumn("_loadDate2", lit(datetime.now()))
    return df
