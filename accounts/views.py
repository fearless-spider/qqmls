from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from qqmls.accounts.forms import RegistrationForm, User


def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleande_data['password1'],
                email=form.cleande_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = Context(request, {
        'form': form
    })
    template = get_template('registration/register.html')
    output = template.render(variables)
    return HttpResponse(output)
