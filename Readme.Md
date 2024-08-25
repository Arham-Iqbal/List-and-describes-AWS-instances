# AWS Resource Listing with Python and Boto3

## Overview

This project provides a Python script that lists various AWS resources including EC2 instances, S3 buckets, and RDS instances using the Boto3 library. It helps you quickly access and review information about these resources in your AWS account.

## Prerequisites

Before running the script, ensure you have the following:

- **Python 3.x**: Ensure Python is installed on your machine. You can download it from [python.org](https://www.python.org/).
- **Boto3**: Install the Boto3 library, which is the Amazon Web Services (AWS) SDK for Python:
  ```bash
  pip install boto3
  ```
- **AWS CLI**: The AWS Command Line Interface (CLI) should be configured with credentials that have permissions to access EC2, S3, and RDS services. If you haven’t configured the AWS CLI, follow the [AWS CLI configuration guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).

## Features

- **List EC2 Instances**: Lists all EC2 instances in your AWS account, including their ID, state, type, and launch time.
- **List S3 Buckets**: Lists all S3 buckets, displaying the bucket name and creation date.
- **Describe RDS Instances**: Lists all RDS instances, including their identifier, class, engine, and current status.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/aws-resource-listing.git
cd aws-resource-listing
```

### 2. Install Dependencies

Install the required Python libraries using pip:

```bash
pip install boto3
```

### 3. Configure AWS Credentials

Ensure your AWS credentials are properly configured. You can do this using the AWS CLI:

```bash
aws configure
```

Alternatively, you can use a credentials file or environment variables. Refer to the [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html) for more details.

### 4. Running the Script

To list the AWS resources, simply run the `aws_resource_listing.py` script:

```bash
python aws_resource_listing.py
```

The script will output the details of EC2 instances, S3 buckets, and RDS instances in your account.

## Error Handling

The script includes basic error handling to catch and display exceptions that may occur during API calls. If an error occurs, it will be printed to the console with a relevant message.

## Customization

You can extend this project by adding the following features:
- **Filtering Results**: Add filters to the resource listing functions to narrow down the results (e.g., list only running EC2 instances).
- **Additional Services**: Extend the script to include other AWS services like Lambda, CloudFormation, or DynamoDB.
- **Output to File**: Modify the script to save the output to a file (e.g., CSV, JSON) for further analysis.



## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## Acknowledgments

- [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) for detailed information on using AWS SDK for Python.
- [AWS Documentation](https://docs.aws.amazon.com/) for understanding various AWS services and their APIs.
```

