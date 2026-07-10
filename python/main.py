from ec2 import (get_all_instances, get_list_of_instance_ids, get_instance_status, get_health_status)

from report import print_ec2_report
from cloudwatch import get_cpu_utilization
from sns_alert import send_email_alert
from export_csv import export_to_csv

def main():
    all_instances = get_all_instances()
    
    instance_ids = get_list_of_instance_ids(all_instances)
    
    instance_statuses = get_instance_status(instance_ids)
    health_status = get_health_status(instance_statuses)
    
    TOPIC_ARN = "arn:aws:sns:us-east-1:188149024121:aws-health-monitor-alerts"
    CPU_THRESHOLD = 80

    for instance in all_instances:
        cpu = get_cpu_utilization(instance["InstanceId"])
        instance["CPUUtilization"] = cpu

        instance_id = instance["InstanceId"]

        instance["InstanceStatus"] = health_status[instance_id]["InstanceStatus"]
        instance["SystemStatus"] = health_status[instance_id]["SystemStatus"]

        if cpu is not None and cpu >= CPU_THRESHOLD:
            send_email_alert(
                    topic_arn=TOPIC_ARN,
                    subject = "AWS Health Monitor Alert: High CPU Utilization",
                    message = (
                        f"High CPU utilization detected.\n\n"
                        f"Instance ID: {instance['InstanceId']}\n"
                        f"CPU Utilization: {cpu:.2f}%"
                    )
                    
            )
       
    print_ec2_report(all_instances, instance_statuses)
    export_to_csv(all_instances)
    print("EC2 report exported to ec2_report.csv")

if __name__ == "__main__":
    main()