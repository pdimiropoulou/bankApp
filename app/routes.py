from flask import render_template, request, redirect
from app import app, db
from app.models import User, Customer, BankAccount, Transaction


@app.route('/api/bankAccount/create', methods=['POST'])
def add():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = request.json
            customerId = data.get('customerId','')
            amount = data.get('amount','')
            accountName = data.get('accountName','')
            if not customerId or not amount: 
                return 'Bad Request', 400
            else:
                bankAccount = BankAccount(customerId  = customerId, amount = amount, accountName = accountName)
                db.session.add(bankAccount)
                db.session.commit()
                return 'OK', 201
        else:
            return 'Unsupported media type', 415

@app.route('/api/bankAccount/transfer', methods=['POST'])
def transfer():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = request.json
            fromAccountId = data.get('fromAccountId','')
            toAccountId = data.get('toAccountId','')
            amount = data.get('amount','')
            if not fromAccountId or not toAccountId or not amount: 
                return 'Bad Request', 400
            else:
                with db.session() as post_session:
                    sourceAccount = BankAccount.query.filter(BankAccount.id == fromAccountId).first()
                    targetAccount = BankAccount.query.filter(BankAccount.id == toAccountId).first()
                    
                    # create transaction and update amount in bank accounts
                    transaction = Transaction(fromAccountId  = fromAccountId, toAccountId = toAccountId, amount = amount)
                    sourceAccount.amount -= amount
                    targetAccount.amount += amount

                    post_session.add(transaction)
                    post_session.commit()
                return 'OK', 201
        else:
            return 'Unsupported media type', 415

@app.route('/api/bankAccount/balance', methods=['GET'])
def balance():
    if request.method == 'GET':
        args = request.args
        if not args.get("accountId"):
            return 'Bad Request', 400
        else:
            accountId = args.get("accountId")
            balance = BankAccount.query.filter(BankAccount.id == accountId).first().amount
            return {'balance':balance}, 201
