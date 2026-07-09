def print_ec2_report(instances, instance_statuses):
    print("=" * 60)
    print("AWS EC2 Health Monitor Report")
    print("=" * 60)

    running = 0
    stopped = 0
    

    for instance in instances:
        cpu = instance["CPUUtilization"]
        print(f"Instance Name: {instance['Name']}")
        print(f"Instance ID: {instance['InstanceId']}")
        print(f"Instance Type: {instance['InstanceType']}")
        print(f"State: {instance['State']}")
        print(f"Instance Status: {instance['InstanceStatus']}")
        print(f"System Status: {instance['SystemStatus']}")
        print(f"CPU Utilization: {cpu:.2f}%" if cpu is not None else "CPU Utilization: No data available")
        print(f"Availability Zone: {instance['AvailabilityZone']}")
        print(f"Public IP: {instance['PublicIp']}")
        print(f"Private IP: {instance['PrivateIp']}")
        print("-" * 60)
        
        if instance['State'] == 'running':
            running += 1
        elif instance['State'] == 'stopped':
            stopped += 1

    print()
    print(f"Total Instances: {len(instances)}")
    print(f"Running Instances: {running}")
    print(f"Stopped Instances: {stopped}")
    print("=" * 60)
