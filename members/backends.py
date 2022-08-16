from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


User = get_user_model()


class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(email__iexact=email) | Q(email__iexact=email))
        except User.DoesNotExist:
            User().set_password(password)
            return
        except User.MultipleObjectsReturned:
            user = User.objects.filter(Q(email__iexact=email) | Q(email__iexact=email)).order_by('id').first()

        if user.check_password(password) and self.user_can_authenticate(user):
            return user