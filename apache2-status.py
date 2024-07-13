import subprocess
import boto3

INSTANCE_ID = open('/bashcripts/instance-id').read().strip()

def check_apache2_status():
    process = subprocess.Popen(['systemctl', 'status', 'apache2'], stdout=subprocess.PIPE)
    output = process.communicate()[0]
    status = output.decode()
    if 'Active: active' in status:
        return 1
    else:
        return 0

status = check_apache2_status()

cloudwatch = boto3.client('cloudwatch', region_name='ap-south-1')
cloudwatch.put_metric_data(
    Namespace='Custom-metric-name-space',
    MetricData=[
        {
            'MetricName': 'apache2-monitor',
            'Value': status,
            'Dimensions': [
                {
                    'Name': 'InstanceId',
                    'Value': INSTANCE_ID
                }
            ]
        }
    ]
)
