# 03_gold_pipeline.py
import dlt
from pyspark.sql.functions import *

@dlt.table(name="gold.default.goldRevenueByHour")
def gold_revenue_by_hour():
    return (
        dlt.read("silver.default.silvertripsclean")
        .withColumn("pickupHour", hour("pickupDatetime"))
        .groupBy("pickupHour")
        .agg(
            count("*").alias("totalTrips"),
            sum("totalAmount").alias("totalRevenue"),
            avg("totalAmount").alias("avgTicket"),
            (avg(col("tipAmount") / col("totalAmount")) * 100).alias("avgTipPercent")
        )
        .orderBy("pickupHour")
    )

@dlt.table(name="gold.default.goldTopZones")
def gold_top_zones():
    pu = (
        dlt.read("silver.default.silvertripsclean")
        .groupBy("puZone")
        .agg(sum("totalAmount").alias("revenue"))
        .withColumn("type", lit("pickup"))
        .orderBy(col("revenue").desc())
        .limit(10)
    )
    do = (
        dlt.read("silver.default.silvertripsclean")
        .groupBy("doZone")
        .agg(sum("totalAmount").alias("revenue"))
        .withColumn("type", lit("dropoff"))
        .orderBy(col("revenue").desc())
        .limit(10)
    )
    return pu.union(do)

@dlt.table(name="gold.default.goldTipByDayOfWeek")
def gold_tip_by_week():
    return (
        dlt.read("silver.default.silvertripsclean")
        .withColumn("dayOfWeek", date_format("pickupDatetime", "EEEE"))
        .groupBy("dayOfWeek")
        .agg(
            (avg(col("tipAmount") / col("totalAmount")) * 100).alias("avgTipPercent")
        )
        .orderBy("dayOfWeek")
    )