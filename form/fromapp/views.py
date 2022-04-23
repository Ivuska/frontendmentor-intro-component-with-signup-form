from django.core.mail import send_mail
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.conf import settings
from django.http import HttpResponseRedirect

from .forms import NameForm

# Create your views here.
class IndexView(FormView):
  # Tells django which template to use
  template_name = "index.html"
  # Tells django which formclass to use
  form_class = NameForm
  # Tells django where to redirect user when the form is validated
  success_url = 'thankyou'

  # This function is called by django when the form is valid so I cannot add any other arguments.
  def form_valid(self, form):
    # Send a thank you email to the user after confirming the form. 
    # I do not need to save the data to be able to use them in the email.
    # https://stackoverflow.com/questions/25090003/how-to-get-the-submitted-value-of-a-form-in-a-django-class-based-view
    user_name = form.cleaned_data['name']
    email_address = form.cleaned_data['email_address']
    send_mail(
      'Thank you for testing =o)',
      'Hi '+ user_name + ', thank you for your registration.',
      'frontendmentor.test@gmail.com', 
      [f'{email_address}', 'frontendmentor.test@gmail.com'], fail_silently=False)

    # Do not save user data when in production.
    if settings.DEBUG:
      form.save()
    # I call the form_valid() function from django itself. We want to provide the data to another template and show them to the user in the message 
    # and 'not only' send the form so we do not use this return.
    # return super().form_valid(form) 

    # This is not the best way how to securely share the data between two templates. But we did not store the data anywhere publicly 
    # so for testing and for practice it is OK. 
    # If we need to to it more secure we do it with some sessions solution, get the data from the dtb. Or combine the parameters in url in 
    # combination with some key or id.
    # https://stackoverflow.com/questions/44915807/how-to-pass-a-form-value-to-another-view
    # https://docs.djangoproject.com/en/4.0/topics/http/sessions/#module-django.contrib.sessions
    return HttpResponseRedirect(f'thankyou?username={user_name}&email_address={email_address}')

class ThankYouView(TemplateView):
  template_name = "thank_you.html"