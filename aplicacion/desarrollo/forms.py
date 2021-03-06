from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario, Observatorio, Observacion, Inscripciones, Notificaciones
from allauth.account.forms import SignupForm
from datetimewidget.widgets import DateTimeWidget
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = Usuario
#         fields = ('nombre','tipoCocina','alergenos','precio',)

#Las dos sigueintes clases, son para que me muestre en el navegador parte /admin, que cuando quiera un nuevo usuario 
# este incluido lo que yo quiera, en este caso tipoUsuario(quen pondre por defecto aficionado y una opcion de que quiero o no ser astrofisico)

class UsuarioCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Usuario
        fields = ('tipoUsuario','solicitudAstro', )


class UsuarioChangeForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('first_name','last_name','image','solicitudAstro',)

class MiSignupForm(SignupForm):
    # Aqui lo que hago es para que me lo muestre a la hora de registrar nuevo usuario en la aplicacion
    # Como tengo en class Usuario un tipoUsuario, genero uno campo forms.MultipleChoiseField
    ATRO = 'AT'
    AFICIONADO = 'AF'

    TIPO_USUARIO = (
    (ATRO , "Atro"),
    (AFICIONADO , "Aficionado"))
    #LO QUE EH ECHO, es no me muestre la opcion de elegir usuario y por defecto ponga AFICIONADO
    # tipoUsuario= forms.MultipleChoiceField(widget=forms.Select, choices = TIPO_USUARIO )# idicio que sea forms.Select, en vez de forms.CheckboxSelectMultiple
    solicitudAstro = forms.BooleanField(widget=forms.CheckboxInput,required=False) # el require es para que si no marcas nada acepte false, si pongo a true se marca
    
    def save(self,request):
        print('-----signup------')
        user= super(MiSignupForm,self).save(request)
        print(self.cleaned_data['solicitudAstro'])
        user.solicitudAstro = self.cleaned_data['solicitudAstro']
        user.save()
        return user

class ObservacionForm(forms.ModelForm):
    class Meta:
        model = Observacion 
        fields = ('nombre','fecha_observacion','duracion_ocultacion','hora_inicio','hora_final','coordenadas','descripcion','image',) #user le indico en view.py que es el mismo registrado



class ObservatorioForm(forms.ModelForm):
    class Meta:
        model = Observatorio
        fields = ('nombre','camara','apertura','filtros','latitude','longitude','distanciaFocal','radioMovilidad',) 

class InscripcionesForm(forms.ModelForm):
    class Meta:
        model = Inscripciones
        fields = ('id_inscripcion','observaciones','observatorios','descripcion','opcionInscripcion','image',)

class NotificacionForm(forms.ModelForm):
    class Meta:
        model = Notificaciones
        fields= ('id_notificacion','user',)

class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
