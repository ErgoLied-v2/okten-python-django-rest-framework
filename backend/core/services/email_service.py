import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from core.dataclasses.user_dataclass import User
from core.services.jwt_service import ActivateToken, JWTService, RecoveryToken


class EmailService:
    @staticmethod
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
        cls.__send_email(
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