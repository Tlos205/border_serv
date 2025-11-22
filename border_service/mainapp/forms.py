from django import forms
from django.core.mail import send_mail
from django.conf import settings
from snowpenguin.django.recaptcha3.widgets import ReCaptchaHiddenInput
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

class FeedbackForm(forms.Form):
    fio = forms.CharField(
        label="ФИО",
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Иванов Иван Иванович'})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder': 'example@mail.ru'})
    )
    phone = forms.CharField(
        required=False,
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': '+7 (999) 123-45-67'})
    )
    subject = forms.CharField(
        label="Тема",
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Кратко укажите суть обращения'})
    )
    message = forms.CharField(
        label="Текст обращения",
        widget=forms.Textarea(attrs={'rows': 8, 'placeholder': 'Подробно опишите ваш вопрос или предложение'}),
        max_length=2000
    )
    
    # Вариант 1: ReCaptcha v3 (невидимая)
    captcha = ReCaptchaField(widget=ReCaptchaHiddenInput())

    # Вариант 2: если нет рекапчи — простое поле (закомментируй строку выше и раскомментируй ниже)
    # captcha = forms.CharField(widget=forms.HiddenInput(), required=False)

    agreement = forms.BooleanField(
        required=True,
        label="Согласие на обработку персональных данных"
    )

    def send_email(self):
        data = self.cleaned_data
        subject = f"[Интернет-приёмная] {data['subject']}"
        message = f"""
Новое обращение в Интернет-приёмную

ФИО: {data['fio']}
Email: {data['email']}
Телефон: {data['phone'] or 'не указан'}

Тема: {data['subject']}

Текст обращения:
{data['message']}

Дата: {__import__('datetime').datetime.now().strftime('%d.%m.%Y %H:%M')}
        """
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['pu.karelia@fsb.ru'],  # ← сюда будет уходить письмо
            fail_silently=False,
        )