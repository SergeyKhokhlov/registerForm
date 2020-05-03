from flask import Flask, render_template
from flask_login import LoginManager
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired
from data import db_session, jobs, users

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    sessions = db_session.create_session()
    return sessions.query(users.User).get(user_id)


class RegisterForm(FlaskForm):
    email = StringField('Login / email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_password = PasswordField('Repeat password', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    speciality = StringField("Speciality", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    sessions = db_session.create_session()
    if form.validate_on_submit():
        if form.password.data != form.repeat_password.data:
            return render_template('register.html', form=form,
                                   message="Passwords don't match")
        if sessions.query(users.User).filter(users.User.email == form.email.data).first():
            return render_template('register.html',
                                   form=form,
                                   message="This user already exists")
        user = users.User(name=form.name.data,
                          email=form.email.data,
                          hashed_password=form.password.data,
                          surname=form.surname.data,
                          age=form.age.data,
                          position=form.position.data,
                          speciality=form.speciality.data,
                          address=form.address.data)
        user.set_password(form.password.data)
        sessions.add(user)
        sessions.commit()
    return render_template("register.html", form=form)


def main():
    db_session.global_init("db/users.db")
    app.run()


if __name__ == '__main__':
    main()
