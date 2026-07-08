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

