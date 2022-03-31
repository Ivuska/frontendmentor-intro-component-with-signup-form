from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import NameForm

# Create your views here.
class IndexView(FormView):
  #Tells django which template to use
  template_name = "index.html"
  #Tells django which formclass to use
  form_class = NameForm
  #Tells django where to redirect user when the form is validated
  success_url = 'thankyou'

  def form_valid(self, form):
    form.save()
    return super().form_valid(form)

class ThankYouView(TemplateView):
  template_name = "thank_you.html"