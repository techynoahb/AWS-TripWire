"""AWS-TripWire Lambda handler.

Milestone 1: print every event EventBridge sends us, so we can see what arrives.
"""

import json


def lambda_handler(event, context):
    # 1. The whole event, one field per line, so it's easy to read in the logs.
    print(json.dumps(event, indent=2))

    # 2. EventBridge puts the CloudTrail record inside "detail".
    #    .get(..., {}) means a missing key gives an empty dict instead of a crash.
    detail = event.get("detail", {})
    event_name = detail.get("eventName")
    region = detail.get("awsRegion")

    print(f"Event: {event_name} in {region}")
