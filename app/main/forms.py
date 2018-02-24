from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import ValidationError, Length
from flask import flash


class AddForm(FlaskForm):		
	add_id = HiddenField('id')
	add_time = StringField('日期',
		render_kw={"placeholder":"请输入日期"},
		validators=[Length(max=20, message="超过最大20个字符")])
	add_detailed = StringField('事项', description="* 必填项",		
		render_kw={"placeholder":"请输入待办事项"},
		validators=[Length(max=50, message="超过最大50个字符")])
	add_submit = SubmitField('确定')
	
	def validate_add_detailed(self, field):
		if field.data == '':
			flash('错误：事项 不能为空')
			raise ValidationError('错误：事项 不能为空')
						
		
class EditForm(FlaskForm):		 
	edit_id = HiddenField('id')
	edit_time = StringField('日期',
		render_kw={"placeholder":"请输入日期"},
		validators=[Length(max=20, message="超过最大20个字符")])
	edit_detailed = StringField('事项', description="* 必填项",		
		render_kw={"placeholder":"请输入待办事项"},
		validators=[Length(max=50, message="超过最大50个字符")])
	edit_submit = SubmitField('确定')
	del_submit = SubmitField('删除')
	
	def validate_edit_detailed(self, field):
		if field.data == '':
			flash('错误：事项 不能为空')
			raise ValidationError('错误：事项 不能为空')



