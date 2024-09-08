from app.accounts import  account_blueprint
from app.models import  db, Account
from flask import  render_template, request, redirect, url_for

@account_blueprint.route('', endpoint='index')
def index():
    accounts = Account.query.all()
    return render_template("accounts/index.html", accounts=accounts)

@account_blueprint.route('/create', endpoint='create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        account = Account(
            f_name=request.form['f_name'],
            l_name=request.form['l_name'],
            mail=request.form['mail'],
            password=request.form['password'],
        )
        db.session.add(account)
        db.session.commit()
        return redirect(url_for('accounts.index'))
    return render_template("accounts/create.html")

@account_blueprint.route('/<int:id>', endpoint='show', methods=['GET'])
def show(id):
    account = db.get_or_404(Account, id)
    return render_template("accounts/show.html", account=account)

@account_blueprint.route('/<int:id>/delete', endpoint='delete', methods=['POST'])
def delete(id):
    account = db.get_or_404(Account, id)
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for('accounts.index'))
