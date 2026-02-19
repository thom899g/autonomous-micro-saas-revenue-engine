from typing import Dict, Any
import boto3
import logging

class InfrastructureManager:
    """Manages cloud infrastructure deployment and scaling.
    
    Attributes:
        ec2_client: AWS EC2 client for managing instances.
        s3_client: AWS S3 client for managing storage.
    """
    
    def __init__(self):
        self.ec2_client = boto3.client('ec2', region_name='us-east-1')
        self.s3_client = boto3.client('s3')
        
    def deploy_infrastructure(self, app_config: Dict[str, Any]) -> None:
        """Deploys infrastructure for a micro-SaaS application.
        
        Args:
            app_config: Configuration details of the application.
        """
        logging.info(f"Deploying infrastructure for {app_config['name']}.")
        # Example: Launch an EC2 instance
        self._launch_instance(app_config)
        # Example: Create an S3 bucket
        self._create_storage_bucket(app_config)

    def _launch_instance(self, app_config: Dict[str, Any]) -> None:
        """Launches a compute instance for the application."""
        try:
            response = self.ec2_client.run_instances(
                ImageId=app_config['ami_id'],
                InstanceType=app_config['instance_type'],
                KeyName=app_config['key_name']
            )
            logging.info(f"Launched instance {response['Instances'][0]['InstanceId']}.")
        except Exception as e: