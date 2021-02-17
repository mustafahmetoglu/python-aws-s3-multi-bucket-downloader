import os

f = open('bucket_list.txt',"r") 
bucket_list = f.read().splitlines()

f2 = open('illegal_characters.txt' ,'r')
illegal_characters = f2.read().splitlines()
buckets_that_error_accured  = []
for bucket in bucket_list:
  bucketFileName = bucket
  for illegal in illegal_characters:
    bucketFileName = bucketFileName.replace(illegal , '')  #avoiding illegal characters on filename
  print(bucket)
  mkdir = os.system("mkdir {}".format(bucketFileName))
  if mkdir == 0:
    print('Succesfuly created directory {}'.format(bucketFileName))
    get_in_new_dir = os.system('cd {} && aws s3 sync s3://{} . '.format(bucketFileName,bucket))
    print("`new file` ran with exit code %d" % get_in_new_dir)
  else:
    print('An error accured while creating directory {} error:{}'.format(bucketFileName,mkdir))
    buckets_that_error_accured.append({"bucketName" : bucket , "errorCode" : mkdir})
if len(buckets_that_error_accured) < 1:
  print("Successfuly downloaded all '{}' listed buckets.".format(len(bucket_list)))
else:
  print('{} out of {} buckets have downloaded buckets that could not be downloaded are listed below'.format(len(bucket_list) - len(buckets_that_error_accured) , len(bucket_list)))
  print(buckets_that_error_accured)