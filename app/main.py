from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from flask_mail import Message
from smtplib import SMTPException
from .forms import ContactForm
from . import mail, db
from .models import ContactMessage, Project
import os

main = Blueprint('main', __name__)


@main.route('/test-session')
def test_session():
    session['test_key'] = 'test_value'
    return f"Session set: {session.get('test_key')}"

#home route
@main.route('/')
def home():
    return render_template('home.html')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        try:
            msg = Message(
                subject='New Contact Form Submission',
                sender=os.getenv('MAIL_USERNAME'),  # Must match MAIL_USERNAME in .env
                recipients=['rahsaz.kevin@gmail.com'],  # Your personal Gmail
                reply_to=form.email.data  # Allows you to reply directly to the user's email
            )
            msg.body = f"""
            You have a new contact form submission:

            - **Name:** {form.name.data}
            - **Email:** {form.email.data}
            - **Message:** {form.message.data}
            """
            mail.send(msg)

            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('main.contact'))
        
        except SMTPException as e:
            flash(f'Failed to send email: {str(e)}', 'error')
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
    
    return render_template('contact.html', form=form)


@main.route('/projects')
def projects():
    all_projects = Project.query.all()
    return render_template('projects.html')


@main.route('/cinesteam-demo')
def cinesteam_demo():
    return render_template('cinesteam.html')
