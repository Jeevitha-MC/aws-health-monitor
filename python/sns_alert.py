from aws_client import get_sns_client


def send_email_alert(topic_arn, subject, message):
    sns = get_sns_client()

    response = sns.publish(
        TopicArn=topic_arn,
        Subject=subject,
        Message=message
    )

    return response