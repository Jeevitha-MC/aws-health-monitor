#What was the CPU usage of this EC2 instance?

from aws_client import get_cloudwatch_client

from datetime import datetime, timedelta, timezone

def get_cpu_utilization(instance_id):
    end_time = datetime.now(timezone.utc)
    start_time = end_time - timedelta(minutes=10)
    cloudwatch = get_cloudwatch_client()
    response = cloudwatch.get_metric_statistics(Namespace = "AWS/EC2",
        MetricName = "CPUUtilization",
        Dimensions = [
            {
                "Name": "InstanceId",
                "Value": instance_id
            }
        ],
        StartTime = start_time,
        EndTime = end_time,
        Period = 300,
        Statistics = ["Average"])
    datapoints = response["Datapoints"]
    if not datapoints:
        return None
    # Sort the datapoints by timestamp and get the latest one
    datapoints.sort(key=lambda x: x["Timestamp"])
    latest = datapoints[-1]
    return latest["Average"]