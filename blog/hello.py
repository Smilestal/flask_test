from flask import Flask, render_template, url_for, request, session, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config['SECRET_KEY'] = 'dsfdsfjkadfg'


# @app.errorhandler(404)
# def page_not_found():
#     return render_template('404.html'), 404
#
#
# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()

    if form.validate_on_submit():
        oldname = session.get('name')
        if oldname is not None and oldname != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))


@app.route('/user/<name>')
def hello(name):
    return render_template('user.html', name=name)


class NameForm(FlaskForm):
    name = StringField('what is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


if __name__ == '__main__':
    app.run(debug=True)
