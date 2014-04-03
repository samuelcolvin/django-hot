import django_tables2 as tables
from django_tables2.utils import A
import public
from django.contrib.auth.models import User, Group
import django.forms as forms

AppName = 'HotDjango'

class User(public.ModelDisplay):
    model = User
#     display = False
    exclude=['password']
    addable = False
    editable = True
    deletable = False
    attached_tables = [{'name':'Group', 'populate':'groups', 'title':'Groups'}]
    show_crums = False
    
    class DjangoTable(public.Table):
        username = public.SelfLinkColumn()
        email = tables.Column()
        first_name = tables.Column()
        last_name = tables.Column()
        class Meta(public.ModelDisplayMeta):
            pass
    
    class form(forms.ModelForm):
        class Meta:
            model = User
            fields = ('first_name', 'last_name', 'email')

class Group(public.ModelDisplay):
    model = Group
#     display = False