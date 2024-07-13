# CloudWatch-Apache2-Alarm-Setup

Automated setup for monitoring Apache2 server status using AWS CloudWatch and email notifications, leveraging Python, Boto3, and AWS CLI.

## Important Terms:
- **Python**: Automation Powerhouse
- **Boto3**: AWS Service Integration
- **AWS CLI**: Command Line Interface for AWS
- **Apache2**: Web Server
- **CloudWatch**: Monitoring Service
- **SNS**: Simple Notification Service

## Introduction:

Welcome to the CloudWatch Apache2 Alarm Setup project. This initiative automates the process of monitoring the status of an Apache2 server using AWS CloudWatch and sends email notifications upon status changes. The setup leverages Python, Boto3, and the AWS CLI to ensure seamless integration and monitoring.

This project streamlines the process of configuring CloudWatch alarms to monitor the health of an Apache2 server without the need for installing an AWS agent. By following the steps outlined, users can achieve an automated monitoring system that alerts them via email whenever the Apache2 server status changes.

## Project Workflow

1. **Install Apache2**
2. **Check Python Version and Install Pip**
3. **Install AWS CLI and Configure AWS**
4. **Create Directory and Necessary Files**
5. **Create instance-id.sh Script**
6. **Create apache2-status.py Script**
7. **Set Up Crontab Jobs**
8. **Create CloudWatch Alarm and SNS Topic**

## Key Achievements:
- Automated the setup of CloudWatch metrics to monitor Apache2 server status.
- Configured email notifications via AWS SNS.
- Utilized Python and Boto3 for interaction with AWS CloudWatch.
- Ensured continuous monitoring by setting up cron jobs.

## Step-by-Step Guide

### Step 1: Install Apache2
```bash
sudo apt-get install apache2
```
```bash
sudo systemctl start apache2
```
```bash
sudo systemctl status apache2
```

### Step 2: Check Python Version and Install Pip
```bash
sudo apt-get install python3-pip
```
```bash
pip install boto3
```

### Step 3: Install AWS CLI and Configure AWS
```bash
sudo apt-get install awscli
```
```bash
aws configure
```

### Step 4: Create Directory and Necessary Files
```bash
mkdir /bashcripts
```
```bash
cd /bashcripts/
```
```bash
touch instance-id.sh instance-id apache2-status.py
```
```bash
chmod 775 *
```

### Step 5: Add this code to instance-id.sh File
```bash
#!/bin/bash
curl http://169.254.169.254/latest/meta-data/instance-id
```

### Step 6: Create apache2-status.py Script
- Use apache2-status.py File From this repository.

### Step 7: Set Up Crontab Jobs
```bash
crontab -e
```
