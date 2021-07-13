# What is it?

A serverless implementation of the `internet_calendar` python package - I use it to allow iOS shortcuts to parse today's events on Forekast.

Serverless will deploy an AWS Lambda function with an associated URL, which you can call using cURL or any other tooling.

# Installation

```
npm install -g serverless
serverless deploy
```