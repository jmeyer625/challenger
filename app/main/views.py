from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .. import db
from ..models import User, Permission
from ..decorators import admin_required, permission_required
from flask.ext.login import login_required

@main.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html', name = session.get('name'), known=session.get('known', False), \
			current_time = datetime.utcnow())

@main.route('/admin')
@login_required
@admin_required
def for_admins_only():
	return 'For administrators'

@main.route('/moderator')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def for_moderators_only():
	return 'For comment moderators'