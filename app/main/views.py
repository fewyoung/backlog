from . import main
from .forms import AddForm, EditForm
from flask import render_template, session, flash, request, redirect, url_for
from ..models import db, User, Detail
		
					
@main.route('/', methods=['GET', 'POST'])
def index():
	add_form = AddForm()
	edit_form = EditForm()
	edit_forms = []	
	get_ip = request.remote_addr
	
	search_user = User.query.filter_by(userip=get_ip).first()
	if search_user is None:
		new_user = User(userip=get_ip)
		db.session.add(new_user)
		db.session.commit()
	
	if add_form.add_submit.data and add_form.validate_on_submit():
		new_detail = Detail(detailtime = add_form.add_time.data,
				  detailed = add_form.add_detailed.data,
				  user = search_user)
		for field in add_form:
			field.data = None
		db.session.add(new_detail)
		db.session.commit()
		flash('完成：添加事项')
		return redirect(url_for('.index'))
		
	if edit_form.edit_submit.data and edit_form.validate_on_submit():
		edit_detail = Detail.query.filter(
			Detail.id == edit_form.edit_id.data).first()
		edit_detail.detailtime = edit_form.edit_time.data
		edit_detail.detailed = edit_form.edit_detailed.data
		db.session.commit()	
		flash('完成：修改事项')
		return redirect(url_for('.index'))
	
	if edit_form.del_submit.data and edit_form.validate_on_submit():
		del_detail = Detail.query.filter(
			Detail.id == edit_form.edit_id.data).first()
		db.session.delete(del_detail)
		db.session.commit()	
		flash('完成：删除事项')	
		return redirect(url_for('.index'))
	
	details = Detail.query.filter_by(
		user=search_user).order_by(Detail.id.desc())
	for detail in details:
		edit_form = EditForm()
		edit_form.edit_id.data = detail.id
		edit_form.edit_time.data = detail.detailtime
		edit_form.edit_detailed.data = detail.detailed
		edit_forms.append(edit_form)	

	return render_template('main.html', 
		add_form=add_form,
		edit_forms=edit_forms)




