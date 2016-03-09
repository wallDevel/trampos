from django.contrib import admin

# Register your models here.
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# Register your models here.
from models import *

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar senha', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('email', 'telefone', 'nivel')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if self.commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password1 = ReadOnlyPasswordHashField()

    class Meta:
        model = Usuario
        fields = ('email', 'password', 'is_active', 'nivel')

    def clean_password(self):
        return self.initial['password']

class UsuarioAdmin(admin.ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'telefone', 'nivel')
    list_filter = ('nivel',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal info', {'fields': ('telefone',)}),
        ('Permissions', {'fields': ('nivel',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'telefone', 'nivel')}
        )
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Imagem)
admin.site.register(Endereco)
admin.site.register(Endereco_Beta)
admin.site.register(Comentario)
admin.site.register(Resposta)