# Test Case : Server Data Sorting
## Test Case ID : ## 001
## Description
This test shall show whether the application handle the incoming MQTT messages correctly with their corresponding database column
## Procedure
1. Publish a test MQTT messages
2. Change MQTT topics
3. Verify data in the database
## Test Data
Various MQTT topics
## Expected Result
App shall assigned the payload to the database column according to the received MQTT topic
