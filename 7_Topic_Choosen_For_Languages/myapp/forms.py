from django.forms import ModelForm
from myapp.models import Project

class ProjectReg(ModelForm):
    required_css_class="required"
    class Meta:
        model=Project
        fields=['studentname','ptopic','planguages','pduration']