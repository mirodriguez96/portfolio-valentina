from .models import Profile


def ctx_dict(request):
    ctx = {}
    profiles = Profile.objects.all()
    for profile in profiles:
        ctx = {
            "my_name": profile.name if profile.name else "Mi nombre",
            "my_occupation": (
                profile.occupation if profile.occupation else "Mi ocupación"
            ),
            "my_avatar": profile.my_avatar,
            "my_biography": profile.biography if profile.biography else "Mi biografía",
            "my_age": profile.age if profile.age else "Mi edad",
            "my_phone": profile.phone if profile.phone else "Mi teléfono",
            "my_email": profile.email if profile.email else "Mi correo electrónico",
        }
    return ctx
