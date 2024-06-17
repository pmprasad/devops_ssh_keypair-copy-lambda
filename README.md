# devops_ssh_keypair-copy-lambda.
This Lambda is used to copy each environment SSH KeyPair from target new account to Devops account bucket 'gehc-devops-accounts-keys'. 

## Use of this Lambda
  As part of the HC platform setup on new account a manual step included to create ssh Keypair for each environment and upload into secops bucket. This manual process being automated using API gateway and Lambda.
 
## Where this lambda is deployed 
  Lambda is deployed in Devops account us-east-1 region.  

## Sample Payload 

 ```bash
        curl -X POST \
             -H "x-api-key: zlYuYUnHQw7plzVySIIeu2sHxVVzilxG4NCceHWd" \
             -H "Content-Type: application/json"  \
             -d '{ "targetbucket" : "gehc-keypair-dev-eu-west-1-744356035207" }' \
             https://ob2szknzd7.execute-api.us-east-1.amazonaws.com/CopyKeyPair/service ```
