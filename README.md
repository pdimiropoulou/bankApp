# API for financial institution challenge

## Introduction

This solution provides endpoints for an internal API for a fake financial institution using Python and Flask. For this challenge a postgres database with sample data has been created in https://api.elephantsql.com/.

## Run solution

Open project folder and type the following commands:

A web server will start at http://localhost:5000.


## API

## Create bank account
`POST /api/bankAccount/create`
### Request
    curl --location --request POST 'http://127.0.0.1:5000/api/bankAccount/create' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "customerId" : 3,
        "amount" : 180.86
    }'

### Response
* HTTP 200/OK: New bank account has been created
* HTTP 404/Bad request: Customer Id or amount are missing from request body
* HTTP 415/Unsupported media type: Request body is not on Json format

## Transfer
`POST /api/bankAccount/transfer`
### Request
     curl --location --request POST 'http://127.0.0.1:5000/api/bankAccount/transfer' \
    --header 'Content-Type: application/json' \
    --data-raw '{ 
        "fromAccountId" : 2,
        "toAccountId" : 3,
        "amount": 10
    }'

### Response
* HTTP 200/OK: New bank account has been created
* HTTP 404/Bad request: Targer or source acount or amount are missing from request body
* HTTP 415/Unsupported media type: Request body is not on Json format

## Account balance
`GET /api/bankAccount/balance?accountId=X`
### Request
    curl --location --request GET 'http://127.0.0.1:5000/api/bankAccount/balance?accountId=1'
### Response
* HTTP 200/OK: Will return the balance of the requested account (ex: { "balance": 2.56  })
* HTTP 404/Bad request: AccountId is missing from request query parameters

