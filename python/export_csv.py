import csv

def export_to_csv(instances, report_file):
    with open(report_file, mode='w', newline='') as file:
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

