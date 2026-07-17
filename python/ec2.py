#Retrieve EC2 instances

from aws_client import get_ec2_client

def get_all_instances():
    ec2 = get_ec2_client()
    response = ec2.describe_instances()
    
    instances = []
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:

            name = "N/A"
            for tag in instance.get("Tags", []):
                if tag["Key"] == "Name":
                    name = tag["Value"]
                    break
            instances.append({
                "Name": name,
                "InstanceId": instance["InstanceId"],
                "InstanceType": instance["InstanceType"],
                "State": instance["State"]["Name"],
                "PublicIp": instance.get("PublicIpAddress", "N/A"),
                "PrivateIp": instance.get("PrivateIpAddress", "N/A"),
                "AvailabilityZone": instance["Placement"]["AvailabilityZone"]#Placement is a nested dictionary
            })
    return instances

def get_list_of_instance_ids(all_instances):
    instance_ids = []
    for instance in all_instances:
        instance_ids.append(instance["InstanceId"])
    return instance_ids

def get_instance_status(instance_ids):
    ec2 = get_ec2_client()
    response = ec2.describe_instance_status(InstanceIds=instance_ids, IncludeAllInstances=True)
    return response

def get_health_status(instance_statuses):
    health_status = {}
    for status in instance_statuses["InstanceStatuses"]:
        health_status[status["InstanceId"]] = {
            "SystemStatus": status["SystemStatus"]["Status"],
            "InstanceStatus": status["InstanceStatus"]["Status"]
        }
    return health_status
