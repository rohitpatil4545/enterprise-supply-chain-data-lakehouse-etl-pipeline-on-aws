import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Initialize Glue Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read Raw CSV Data from S3

df = spark.read \
    .option("header", "true") \
    .csv("s3://supply-chain-raw-data-pipline-bucket/raw/supply_chain_data.csv")

# Remove Duplicate Records

df_cleaned = df.dropDuplicates()

# Filter Delayed Shipments


df_delayed = df_cleaned.filter(
    df_cleaned["delivery_status"] == "Delayed"
)

# Write Processed Data to S3 in Parquet Format

df_delayed.write \
    .mode("overwrite") \
    .parquet("s3://supply-chain-processed-data-pipline-bucket/processed/delayed_shipments/")

# Commit Glue Job

job.commit()