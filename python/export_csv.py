import csv

def export_to_csv(instances):
    REPORT_FILE = "ec2_report.csv"
    with open(REPORT_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            "Name", "Instance ID", "Instance Type", "State", "Instance Status",
            "System Status", "CPU Utilization", "Availability Zone", "Public IP", "Private IP"
        ])
        for instance in instances:
            writer.writerow([
                instance['Name'],
                instance['InstanceId'],
                instance['InstanceType'],
                instance['State'],
                instance['InstanceStatus'],
                instance['SystemStatus'],
                f"{instance['CPUUtilization']:.2f}%" if instance['CPUUtilization'] is not None else "No data available",
                instance['AvailabilityZone'],
                instance['PublicIp'],
                instance['PrivateIp']
            ])

