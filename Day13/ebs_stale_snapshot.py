import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    try:
        # Get all EBS snapshots with pagination
        snapshots = []
        paginator = ec2.get_paginator('describe_snapshots')
        for page in paginator.paginate(OwnerIds=['self']):
            snapshots.extend(page['Snapshots'])

        print(f"Found {len(snapshots)} snapshots.")

        # Get all active EC2 instance IDs
        instances_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
        active_instance_ids = set()
        for reservation in instances_response['Reservations']:
            for instance in reservation['Instances']:
                active_instance_ids.add(instance['InstanceId'])

        print(f"Active instances: {active_instance_ids}")

        # Iterate through each snapshot and delete if it's not attached to any volume or the volume is not attached to a running instance
        for snapshot in snapshots:
            snapshot_id = snapshot['SnapshotId']
            volume_id = snapshot.get('VolumeId')

            if not volume_id:
                # Delete the snapshot if it's not attached to any volume
                ec2.delete_snapshot(SnapshotId=snapshot_id)
                print(f"Deleted EBS snapshot {snapshot_id} as it was not attached to any volume.")
            else:
                # Check if the volume still exists
                try:
                    volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
                    if not volume_response['Volumes'][0]['Attachments']:
                        ec2.delete_snapshot(SnapshotId=snapshot_id)
                        print(f"Deleted EBS snapshot {snapshot_id} as it was taken from a volume not attached to any running instance.")
                except ec2.exceptions.ClientError as e:
                    if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                        # The volume associated with the snapshot is not found (it might have been deleted)
                        ec2.delete_snapshot(SnapshotId=snapshot_id)
                        print(f"Deleted EBS snapshot {snapshot_id} as its associated volume was not found.")
                    else:
                        # Handle other potential errors
                        print(f"Error describing volume for snapshot {snapshot_id}: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")
