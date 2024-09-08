from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, IntegerField, SelectField, FileField
from wtforms.validators import DataRequired, Length
from app.models import Account, db

class PostForm(FlaskForm):
    title = StringField("Name", validators=[DataRequired(), Length(1, 40)])
    image= FileField("Image")
    description = StringField("Description", validators=[Length(1, 40)])
    account_id = SelectField("Account", validators=[DataRequired()], choices= [])
    submit = SubmitField("Save new Post")

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        # while creating object from form --> please give me the accounts
        self.account_id.choices = [(t.id, f"{t.f_name} {t.l_name}") for t in Account.query.all()]
