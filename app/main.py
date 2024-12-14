from flask import Blueprint, render_template, request, flash, redirect, url_for
from .forms import ContactForm

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('home.html')


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Your message has been sent!')
        return redirect(url_for('main.home'))
    return render_template('contact.html', form=form)

@main.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')