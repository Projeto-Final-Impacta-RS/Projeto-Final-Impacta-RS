from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import *

class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username']
        labels = {
            'username': _('Nome de usuário'),
        }
        help_texts = {
            'username': _('Obrigatório. Máximo de 150 caracteres e apenas letras ou dígitos')
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirmação de senha'

        self.fields['password1'].help_text = 'Mínimo de 8 dígitos e deve conter letras e números.'
        self.fields['password2'].help_text = 'Digite novamente a senha para verificação.'


class addQuestionform(ModelForm):
    class Meta:
        model=Questao
        fields="__all__"
        labels = {
            'descricao': _('Pergunta'),
            'alternativa1': _('Alternativa 1'),
            'alternativa2': _('Alternativa 2'),
            'alternativa3': _('Alternativa 3'),
            'alternativa4': _('Alternativa 4'),
            'resposta': _('Número da alternativa correta'),
        }
        help_texts = {
            'descricao': _(''),
        }
        error_messages = {
            'descricao': {
                'max_length': _("O tamanho limite da pergunta é de 200 caracteres."),
                'required': _("É necessário informar a pergunta."),
            },
            'alternativa1': {
                'max_length': _("O tamanho limite da alternativa 1 é de 200 caracteres."),
                'required': _("É necessário informar a alternativa 1."),
            },
            'alternativa2': {
                'max_length': _("O tamanho limite da alternativa 2 é de 200 caracteres."),
                'required': _("É necessário informar a alternativa 2."),
            },
            'alternativa3': {
                'max_length': _("O tamanho limite da alternativa 3 é de 200 caracteres."),
                'required': _("É necessário informar a alternativa 3."),
            },
            'alternativa4': {
                'max_length': _("O tamanho limite da alternativa 4 é de 200 caracteres."),
                'required': _("É necessário informar a alternativa 4."),
            },
            'resposta': {
                'max_length': _("O tamanho limite da resposta é de 200 caracteres."),
                'required': _("É necessário informar a resposta."),
            },
        }
    