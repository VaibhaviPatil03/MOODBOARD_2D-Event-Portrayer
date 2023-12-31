# -*- coding: utf-8 -*-
"""labelingimages

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11YBxkBn5pN7vlthuS5u9RkfMBBMQpNWW
"""

!pip install boto3

'''Collecting boto3
  Downloading boto3-1.26.162-py3-none-any.whl (135 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 135.9/135.9 kB 3.8 MB/s eta 0:00:00
Collecting botocore<1.30.0,>=1.29.162 (from boto3)
  Downloading botocore-1.29.162-py3-none-any.whl (11.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.0/11.0 MB 52.3 MB/s eta 0:00:00
Collecting jmespath<2.0.0,>=0.7.1 (from boto3)
  Downloading jmespath-1.0.1-py3-none-any.whl (20 kB)
Collecting s3transfer<0.7.0,>=0.6.0 (from boto3)
  Downloading s3transfer-0.6.1-py3-none-any.whl (79 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 79.8/79.8 kB 6.4 MB/s eta 0:00:00
Requirement already satisfied: python-dateutil<3.0.0,>=2.1 in /usr/local/lib/python3.10/dist-packages (from botocore<1.30.0,>=1.29.162->boto3) (2.8.2)
Requirement already satisfied: urllib3<1.27,>=1.25.4 in /usr/local/lib/python3.10/dist-packages (from botocore<1.30.0,>=1.29.162->boto3) (1.26.16)
Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil<3.0.0,>=2.1->botocore<1.30.0,>=1.29.162->boto3) (1.16.0)
Installing collected packages: jmespath, botocore, s3transfer, boto3
Successfully installed boto3-1.26.162 botocore-1.29.162 jmespath-1.0.1 s3transfer-0.6.1
'''

import boto3

session = boto3.Session(
    aws_access_key_id='AKIARYJZJG27UGMTD4DV',
    aws_secret_access_key='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',
    region_name='us-east-1'
)

rekognition_client = session.client('rekognition')

response = rekognition_client.detect_labels(
    Image={
        'S3Object': {
            'Bucket': 'testimagesofparty',
            'Name': 'birthday1.jpg'
        }
    },
    MaxLabels=10
)


labels = [label['Name'] for label in response['Labels']]
labels

image_files = ['birthday1.jpg','birthday2.png','birthday3.jpg','birthday4.jpg','birthday5.jpg','birthday6.jpg','birthday7.png','birthday8.jpg','birthday9.jpg']

all_labels = []

for image_file in image_files:
    response = rekognition_client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': 'testimagesofparty',
                'Name': image_file
            }
        },
        MaxLabels=10


    )
    labels = [label['Name'] for label in response['Labels']]
    all_labels.append(labels)


output_file = 'labels.txt'

with open(output_file, 'w') as file:
      for i, image_file in enumerate(image_files):
        file.write(f'Image: {image_file}\n')
        file.write('Labels:\n')
        for label in all_labels[i]:
            file.write(f'- {label}\n')
        file.write('\n')

image_files = ['a (1).jfif', 'a (2).jfif', 'a (3).jfif', 'a (4).jfif', 'a (5).jfif', 'a (6).jfif', 'a (7).jfif',
               'a (8).jfif', 'a (9).jfif', 'a (10).jfif', 'a (11).jfif', 'a (12).jfif', 'a (13).jfif', 'a (14).jfif',
               'a (15).jfif', 'a (16).jfif', 'a (17).jfif', 'a (18).jfif', 'a (19).jfif', 'a (20).jfif', 'a (21).jfif',
               'a (22).jfif', 'a (23).jfif', 'a (24).jfif', 'a (25).jfif', 'a (26).jfif', 'a (27).jfif', 'a (28).jfif',
               'a (29).jfif', 'a (30).jfif', 'a (31).jfif', 'a (32).jfif', 'a (33).jfif', 'a (34).jfif', 'a (35).jfif',
               'a (36).jfif', 'a (37).jfif', 'a (38).jfif', 'a (39).jfif', 'a (40).jfif', 'a (41).jfif', 'a (42).jfif',
               'a (43).jfif', 'a (44).jfif', 'a (45).jfif', 'a (46).jfif', 'a (47).jfif', 'a (48).jfif', 'a (49).jfif',
               'a (50).jfif', 'a (51).jfif', 'a (52).jfif', 'a (53).jfif', 'a (54).jpg']

all_labels = []

for image_file in image_files:
    response = rekognition_client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': 'moodboarddataset',
                'Name': image_file
            }
        },
        MaxLabels=15


    )
    labels = [label['Name'] for label in response['Labels']]
    all_labels.append(labels)


output_file = 'food.txt'

with open(output_file, 'w') as file:
      for i, image_file in enumerate(image_files):
        file.write(f'Image: {image_file}\n')
        file.write('Labels:\n')
        for label in all_labels[i]:
            file.write(f'- {label}\n')
        file.write('\n')

image_files = ['b (1).jfif', 'b (2).jfif', 'b (3).jfif', 'b (4).jfif', 'b (5).jfif', 'b (6).jfif', 'b (7).jfif',
               'b (8).jfif', 'b (9).jfif', 'b (10).jfif', 'b (11).jfif', 'b (12).jfif', 'b (13).jfif', 'b (14).jfif',
               'b (15).jfif', 'b (16).jfif', 'b (17).jfif', 'b (18).jfif', 'b (19).jfif', 'b (20).jfif', 'b (21).jfif',
               'b (22).jfif', 'b (23).jfif', 'b (24).jfif', 'b (25).jfif', 'b (26).jfif', 'b (27).jfif', 'b (28).jfif',
               'b (29).jfif', 'b (30).jfif', 'b (31).jfif', 'b (32).jfif', 'b (33).jfif', 'b (34).jfif', 'b (35).jfif',
               'b (36).jfif', 'b (37).jfif', 'b (38).jfif', 'b (39).jfif', 'b (40).jfif', 'b (41).jfif', 'b (42).jfif',
               'b (43).jfif', 'b (1).jpg', 'b (2).jpg', 'b (3).jpg', 'b (1).png', 'b (2).png', 'b (3).png', 'b (4).png']

all_labels = []

for image_file in image_files:
    response = rekognition_client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': 'moodboarddataset',
                'Name': image_file
            }
        },
        MaxLabels=15


    )
    labels = [label['Name'] for label in response['Labels']]
    all_labels.append(labels)


output_file = 'venue.txt'

with open(output_file, 'w') as file:
      for i, image_file in enumerate(image_files):
        file.write(f'Image: {image_file}\n')
        file.write('Labels:\n')
        for label in all_labels[i]:
            file.write(f'- {label}\n')
        file.write('\n')

image_files = ['c (1).jfif', 'c (2).jfif', 'c (3).jfif', 'c (4).jfif', 'c (5).jfif', 'c (6).jfif', 'c (7).jfif',
               'c (8).jfif', 'c (9).jfif', 'c (10).jfif', 'c (11).jfif', 'c (12).jfif', 'c (13).jfif', 'c (14).jfif',
               'c (15).jfif', 'c (16).jfif', 'c (17).jfif', 'c (18).jfif', 'c (19).jfif', 'c (20).jfif', 'c (21).jfif',
               'c (22).jfif', 'c (23).jfif', 'c (24).jfif', 'c (25).jfif',
               'c (1).jpg', 'c (2).jpg', 'c (3).jpg', 'c (4).jpg', 'c (5).jpg', 'c (6).jpg', 'c (7).jpg',
               'c (8).jpg', 'c (9).jpg', 'c (10).jpg', 'c (11).jpg', 'c (12).jpg', 'c (13).jpg', 'c (14).jpg']

all_labels = []

for image_file in image_files:
    response = rekognition_client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': 'moodboarddataset',
                'Name': image_file
            }
        },
        MaxLabels=15


    )
    labels = [label['Name'] for label in response['Labels']]
    all_labels.append(labels)


output_file = 'service.txt'

with open(output_file, 'w') as file:
      for i, image_file in enumerate(image_files):
        file.write(f'Image: {image_file}\n')
        file.write('Labels:\n')
        for label in all_labels[i]:
            file.write(f'- {label}\n')
        file.write('\n')

import csv

def txt_to_csv(input_file, output_file):
    with open(input_file, 'r') as txt_file:
        lines = txt_file.readlines()

    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for line in lines:
            line = line.strip()
            if line.startswith('-'):
                line = line[1:]  # Remove the leading hyphen
            row = line.split('\t')  # Modify the delimiter if necessary
            writer.writerow(row)

# Example usage
txt_to_csv('food.txt', 'food.csv')

import csv

def txt_to_csv(input_file, output_file):
    with open(input_file, 'r') as txt_file:
        lines = txt_file.readlines()

    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for line in lines:
            line = line.strip()
            if line.startswith('-'):
                line = line[1:]  # Remove the leading hyphen
            row = line.split('\t')  # Modify the delimiter if necessary
            writer.writerow(row)

# Example usage
txt_to_csv('venue.txt', 'venue.csv')

import csv

def txt_to_csv(input_file, output_file):
    with open(input_file, 'r') as txt_file:
        lines = txt_file.readlines()

    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for line in lines:
            line = line.strip()
            if line.startswith('-'):
                line = line[1:]  # Remove the leading hyphen
            row = line.split('\t')  # Modify the delimiter if necessary
            writer.writerow(row)

# Example usage
txt_to_csv('service.txt', 'service.csv')