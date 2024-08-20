import os

from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.db.models import Model
from django.template.loader import get_template

from configs.celery import app

from core.dataclasses.user_dataclass import User
from core.services.jwt_service import ActivateToken, JWTService, RecoveryToken

UserModel: User | Model = get_user_model()


class EmailService:
    @staticmethod
    @app.task
    def __send_email(to: str, template_name: str, context: dict, subject: str = '') -> None:
        template = get_template(template_name)
        html_content = template.render(context)
        message = EmailMultiAlternatives(subject=subject, from_email=os.environ.get('EMAIL_HOST_USER'), to=[to])
        message.attach_alternative(html_content, 'text/html')
        message.send()

    @classmethod
    def send_test(cls):
        cls.__send_email('nakamuraritsu@gmail.com', 'test.html', {}, 'Test Email')

    @classmethod
    def registrate_email(cls, user: User):
        token = JWTService.create_token(user, ActivateToken)
        url = f'http://localhost:3000/activate/{token}'
        cls.__send_email.delay(
            user.email,
            'registration.html',
            {'name': user.profile.first_name + ' ' + user.profile.last_name, 'url': url},
            'Registration'
        )

    @classmethod
    def recovery_email(cls, user: User):
        token = JWTService.create_token(user, RecoveryToken)
        url = f'http://localhost:3000/recovery/{token}'
        cls.__send_email(
            user.email,
            'recovery.html',
            {'name': user.profile.first_name + ' ' + user.profile.last_name, 'url': url},
            'Recovery pwd'
        )

    # SEND NOTIFICATION SPAM

    @staticmethod
    @app.task
    def notification():
        for user in UserModel.objects.all():
            EmailService.__send_email(
                user.email,
                'notification.html',
                {'name': user.profile.first_name},
                'Notification'
            )
