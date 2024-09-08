from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FileField
from wtforms.validators import DataRequired, Length
from app.models import Account

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(1, 40)])
    image = FileField("Image")
    description = StringField("Description", validators=[Length(1, 40)])
    account_id = SelectField("Account", validators=[DataRequired()], choices=[])
    submit = SubmitField("Save Post")

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.account_id.choices = [(account.id, f"{account.f_name} {account.l_name}") for account in Account.query.all()]
