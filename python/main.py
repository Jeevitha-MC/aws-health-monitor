from ec2 import get_all_instances

def main():
    all_instances = get_all_instances()
    for instance in all_instances:
        print(instance)


if __name__ == "__main__":
    main()