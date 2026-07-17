# AWS Health Monitor

AWS Health Monitor is an end-to-end cloud infrastructure monitoring project built with Python and AWS. It automates EC2 health monitoring, CPU utilization analysis, CSV report generation, and SNS-based email notifications. The project showcases Infrastructure as Code using Terraform, containerization with Docker and Docker Compose, and local Kubernetes deployment using Minikube.

## Architecture

![AWS Health Monitor Architecture](images/architecture.png)

## Features

## Features

- Provision AWS infrastructure using Terraform
- Retrieve EC2 instance inventory
- Monitor CPU utilization using Amazon CloudWatch
- Check EC2 instance and system health status
- Export reports to CSV
- Send SNS email alerts
- Configure application using `config.json`
- Containerize the application using Docker
- Run the application with Docker Compose
- Deploy the application to a local Kubernetes cluster (Minikube)

## Tech Stack

- Python
- AWS EC2
- Amazon CloudWatch
- Amazon SNS
- Terraform
- Boto3
- Docker
- Docker Compose
- Kubernetes (Minikube)

## Project Structure

```text
AWS-HEALTH-MONITOR/
│
├── images/
│   └── architecture.png
│
├── kubernetes/
│   └── pod.yaml
│
├── python/
│   ├── aws_client.py
│   ├── cloudwatch.py
│   ├── config.json
│   ├── config.py
│   ├── ec2.py
│   ├── export_csv.py
│   ├── main.py
│   ├── report.py
│   ├── requirements.txt
│   └── sns_alert.py
│
├── terraform/
│   ├── main.tf
│   ├── outputs.tf
│   ├── provider.tf
│   └── variables.tf
│
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
└── README.md
```

## Configuration

Update `python/config.json`:

```json
{
  "cpu_threshold": 80,
  "report_file": "ec2_report.csv",
  "sns_topic_arn": ""
}
```

## Run the Project

```bash
cd python
pip install -r requirements.txt
python main.py
```

## Sample Output

```text
============================================================
AWS EC2 Health Monitor Report
============================================================

Instance Name: health-monitor-server
State: running
CPU Utilization: 0.05%
Instance Status: ok
System Status: ok

Total Instances: 1
Running Instances: 1
Stopped Instances: 0
============================================================
```
## Docker

### Build the image

```bash
docker build -t aws-health-monitor:v1 .
```

### Run the container

```bash
MSYS_NO_PATHCONV=1 docker run --rm \
  -e AWS_DEFAULT_REGION=us-east-1 \
  -v /c/Users/<username>/.aws:/root/.aws:ro \
  aws-health-monitor:v1
```
## Docker Compose

Run the application using Docker Compose:

```bash
docker compose up
```

Stop the application:

```bash
docker compose down
```
## Kubernetes (Minikube)

Load the Docker image into Minikube:

```bash
minikube image load aws-health-monitor:v1
```

Create the Kubernetes Secret:

```bash
kubectl create secret generic aws-credentials \
  --from-file=config=/mnt/c/Users/<username>/.aws/config \
  --from-file=credentials=/mnt/c/Users/<username>/.aws/credentials
```

Deploy the application:

```bash
kubectl apply -f kubernetes/pod.yaml
```

View logs:

```bash
kubectl logs aws-health-monitor
```

Delete the Pod:

```bash
kubectl delete pod aws-health-monitor
```

## Author

**Jeevitha MC** 
