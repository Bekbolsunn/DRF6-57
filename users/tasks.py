from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_otp_mail(email, code):
    print("#" * 20)
    send_mail(
        "Для подтверждения",
        f"Не сообщайте чужим людям: {code}",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    return "Ok"

@shared_task
def send_daily_report():
    print("#" * 20)
    send_mail(
        "Отчет",
        f"Не говори со мной",
        settings.EMAIL_HOST_USER,
        ["example@gmail.com"],
        fail_silently=False,
    )
    return "Ok"