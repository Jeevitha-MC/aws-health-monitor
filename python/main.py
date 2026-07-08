from ec2 import (get_all_instances, get_list_of_instance_ids, get_instance_status)

def main():
    all_instances = get_all_instances()
    instance_ids = get_list_of_instance_ids(all_instances)
    instance_statuses = get_instance_status(instance_ids)
    #for instance in all_instances:
        #print(instance)
    print(instance_statuses["InstanceStatuses"])


if __name__ == "__main__":
    main()