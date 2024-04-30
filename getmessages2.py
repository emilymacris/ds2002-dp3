#!/home/gitpod/.pyenv/shims/python3

import boto3
from botocore.exceptions import ClientError
import requests
import json

# Set up your SQS queue URL and boto3 client
url = "https://sqs.us-east-1.amazonaws.com/440848399208/bdf7bz"
sqs = boto3.client('sqs')
dictionary = {}
final_string = " " 
def get_message():
    try:
        # Receive message from SQS queue. Each message has two MessageAttributes: order and word
        # You want to extract these two attributes to reassemble the message
        for i in range(1,11):
            response = sqs.receive_message(
                QueueUrl=url,
                AttributeNames=[
                    'All'
                ],
                MaxNumberOfMessages=1,
                MessageAttributeNames=[
                    'All'
                ]
            )
        # Check if there is a message in the queue or not
            if "Messages" in response:
                # extract the two message attributes you want to use as variables
                # extract the handle for deletion later
                order = response['Messages'][0]['MessageAttributes']['order']['StringValue']
                word = response['Messages'][0]['MessageAttributes']['word']['StringValue']
                handle = response['Messages'][0]['ReceiptHandle']
                # dictionary[i]= [order, word, handle]

                message = {order: word}
                dictionary.update(message)
                
        # If there is no message in the queue, print a message and exit    
            else:
                print("No message in the queue")
                #exit(1)
                continue

    # Handle any errors that may occur connecting to SQS
        for x in range(0,10):        
            for key, value in dictionary.items():
                if value[0]==x:
                    final_string = final_string + " " + value[1]
        
    except ClientError as e:
        # print(e.response['Error']['Message'])
        print("ClientError")
        
    
                    # delete 
    print(dictionary)
    # SORT through the dictionary

    # sort the dict by key

    # fetch out the values (another for loop)
   # print(final_string)
   # print("hi")

get_message()

 # for i in range(0, 10):
        #     for key, value in dictionary.items():
        #         if value[1]==i:
        #             print(value[0])

                    # then use the handle to delete the message

            # Print the message attributes - this is what you want to work with to reassemble the message
            # print(f"Order: {order}")
            # print(f"Word: {word}")
