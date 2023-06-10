import time
import random
import json
import boto3


class StreamInput():

  def __init__(self,cnt):
    self.cnt=cnt
  
  def data_gen(self):
    inp={}
    num1=random.randint(1,100)
    num2=random.randint(1,100)
    inp={'First_Num':num1,'Second_Num':num2}  
    outrecords=json.dumps(inp)
    return {'Data': bytes(outrecords, 'utf-8')}

  def output(self):
    return [self.data_gen() for _ in range(self.cnt)]

  
i = 50
kinesis_stream = boto3.client('firehose')
while i > 50:
  stream=StreamInput(3)
  records=stream.output()
  # send data to kinesis
  res = kinesis_stream.put_record_batch(DeliveryStreamName="SampleNumbers",
                                                      Records=records)
  i-=1
  time.sleep(0.1)
