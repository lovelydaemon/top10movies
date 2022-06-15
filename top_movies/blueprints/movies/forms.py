from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length, NumberRange


class EditForm(FlaskForm):
    rating = FloatField(label='Your Rating Out of 5 e.g. 3.5', validators=[DataRequired(), NumberRange(min=1, max=5)])
    review = StringField(
        label='Your Review',
        validators=[DataRequired(), Length(max=250)]
        )

    submit = SubmitField('Done')


class AddForm(FlaskForm):
    title = StringField(
        label='Movie Title',
        validators=[DataRequired()]
        )

    submit = SubmitField('Add Movie')
