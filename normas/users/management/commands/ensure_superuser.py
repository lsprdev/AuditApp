import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates or updates a superuser from DJANGO_SUPERUSER_* environment variables."

    def handle(self, *args, **options):
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

        if not username or not password:
            self.stdout.write(
                "Skipping superuser setup: DJANGO_SUPERUSER_USERNAME or "
                "DJANGO_SUPERUSER_PASSWORD is not set."
            )
            return

        User = get_user_model()
        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                "email": email,
                "is_staff": True,
                "is_superuser": True,
            },
        )

        changed_fields = []
        if email and user.email != email:
            user.email = email
            changed_fields.append("email")
        if not user.is_staff:
            user.is_staff = True
            changed_fields.append("is_staff")
        if not user.is_superuser:
            user.is_superuser = True
            changed_fields.append("is_superuser")

        if created or password:
            user.set_password(password)
            changed_fields.append("password")

        if created:
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Created superuser '{username}'."))
            return

        if changed_fields:
            user.save(update_fields=sorted(set(changed_fields)))
            self.stdout.write(self.style.SUCCESS(f"Updated superuser '{username}'."))
            return

        self.stdout.write(f"Superuser '{username}' already exists.")
