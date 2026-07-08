from ec2 import (get_all_instances, get_list_of_instance_ids, get_instance_status)

from report import print_ec2_report

def main():
    all_instances = get_all_instances()
    instance_ids = get_list_of_instance_ids(all_instances)
    instance_statuses = get_instance_status(instance_ids)
    print_ec2_report(all_instances, instance_statuses)
   

if __name__ == "__main__":
    main()