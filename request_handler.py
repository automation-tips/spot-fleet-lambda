# -*- coding: utf-8 -*-

# lambda func : RequestSpotInstances
# Python version 3.6 ~

import boto3

# SpotFleet、インスタンスタイプetc設定
spot_price = "0.05"
request_type = "one-time"
duration_minutes = 60
image_id = "ami-xxxxxxxxxxxxxxx"
security_groups = ["sg-xxxxxxxxxxxxx"]
incetance_type = "t3.medium"
availability_zone = "ap-northeast-1a"
subnet_id = "subnet-xxxxxxxxxxxx"

client = boto3.client('ec2')


def lambda_handler(event, context):

    # SpotFleetリクエスト
    response = client.request_spot_instances(
        SpotPrice=spot_price,
        InstanceCount=1,
        Type=request_type,
        BlockDurationMinutes=duration_minutes,
        LaunchSpecification={
            "ImageId": image_id,
            "SecurityGroupIds": security_groups,
            "InstanceType": incetance_type,
            "Placement": {
                "AvailabilityZone": availability_zone
            },
            "SubnetId": subnet_id
        }
    )
    request = {
        "requestId": response['ResponseMetadata']['RequestId']
    }

    # スポットリクエストID
    # 戻り値例：{"requestId": "sir-bbbbbbb"}
    return request


#print(lambda_handler("ddd", "aaa"))
