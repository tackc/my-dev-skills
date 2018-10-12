from django.forms import ModelForm, Form, CharField, IntegerField, PasswordInput

class LoginForm(Form):
    username = CharField(label="User Name", max_length=64)
    password = CharField(widget=PasswordInput())

# class SkillForm(Form):
#     skill = CharField(label="Skill")
#     description = CharField(label="Desc")
#     skill_level = IntegerField(label="Level Up")