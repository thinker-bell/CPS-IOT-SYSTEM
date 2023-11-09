# CPS-IOT-SYSTEM

## Introduction
The code presented in this repository provides the neccesary frameworks that are required to setup an IoT system, with a Master and Client format. The implementation is exclusively Python based. In this case the IoT system was setup to implmenet CPS security and a series of flood attacks. 

## System Requirements
The IoT system is designed to operate on two Raspberry Pi devices respectively, a Client and a Server. The Client in this case is equipped with an Arduino sensor that takes real time temperature measurements and sents it to the Server. The implementation is given via two transmission protocols, MQTT and ZeroMQ respectively. 

## MQTT Implementation

1. To run the MQTT code, respective packages need to be installed on both the Rapsberry Pi devices.
2. The Server code "BD_mqtt_server.py" is to be executed on the main Raspberry Pi, and this needs to be run concurrently first.
3. Execute the client code "BigData_sender(MQTT).py" on the Raspberry Pi equipped with an Arduino temperature sensor.

Once the server and client is up and running the temperature will be displayed via terminal on both the Client and Server side.

## ZeroMQ Implementation

1. To run the ZeroMQ code, respective packages need to be installed on both the Rapsberry Pi devices.
2. The Server code "BD_ZeroMQ_server(2).py" is to be executed on the main Raspberry Pi, and this needs to be run concurrently first.
3. Execute the client code "BigData_sender(ZeroMQ)(2).py" on the Raspberry Pi equipped with an Arduino temperature sensor.

Once the server and client is up and running the temperature will be displayed via terminal on both the Client and Server side.

## Wirehsark
Wireshark technology was utilzed to observe the Traffic data specifically on the Server, to enable the data generation for both normal and malicious data.

##DDos Attacks
Utilizing a series of tools, the Server was attacked and malicious network traffic gathered to build a classification machine learning model regarding the network traffic. 
