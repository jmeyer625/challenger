from flask.ext.mail import Message
from flask import current_app, render_template
from app import mail, mandrill
import logging

def send_email(to, subject, template, **kwargs):
	msg = Message(current_app.config['CHALLENGER_MAIL_SUBJECT_PREFIX'] + subject, sender=current_app.config['CHALLENGER_MAIL_SENDER'], recipients=[to])
	msg.body = render_template(template + '.txt', **kwargs)
	#msg.html = render_template(template + '.html', **kwargs)
	mail.send(msg)

def send_mandrill_email(template, subject, to, **kwargs):
	print('got here')
	msg = render_template(template + '.txt', **kwargs)
	response = mandrill.send_email(
	    from_email='challengerapp@gmail.com',
	    subject=subject,
	    to=to,
	    text=msg
	)
	print(response)
		#logging.info('Sent contact email: {0}'.format(form.cleaned_data))
	# except mandrill.InvalidKeyError, e:
	# 	logging.error('Cannot send contact email: {0}'.format(form.cleaned_data))
	# 	logging.exception(e)
	# except mandrill.Error, e:
	# 	logging.error('Cannot send contact email: {0}'.format(form.cleaned_data))
	# 	logging.exception(e)