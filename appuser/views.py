from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

from django.urls import reverse_lazy

from appuser.forms import UserRegisterForm, UserEditForm

# Create your views here.
def login_request(request):
    msg_login = ""

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                print("Login exitoso")
                return render(request, "appcuentas/index.html")
            
            msg_login = 'Usuario o contraseña incorrectos'

    form = AuthenticationForm()
    return render(request, "appuser/login.html", {"form": form, "msg_login": msg_login})


def register(request):
    msg_register = ""

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        print(form)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "appcuentas/index.html")
        
        msg_register = "Error al registrar usuario"
    
    form = UserRegisterForm()
    return render(request, 'appuser/registro.html', {'form':form, 'msg_register':msg_register}) 


def editar_perfil(request):
    user = request.user
    msg_editar = ""
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return render(request, "appcuentas/index.html")
        else:
            msg_editar = "Error al editar usuario"
    else:
        form = UserEditForm(instance=user)

    return render(request, 'appuser/editar_perfil.html', {'form':form, 'msg_editar':msg_editar})


""" class cambiar_password(LoginRequiredMixin, PasswordChangeView):
    template_name = 'appuser/editar_password.html'
    success_url = reverse_lazy('editarPerfil')
    msg_cambiar_password = ""
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    def form_invalid(self, form):
        self.msg_cambiar_password = "Error al cambiar contraseña"
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg_cambiar_password'] = self.msg_cambiar_password
        return context
"""