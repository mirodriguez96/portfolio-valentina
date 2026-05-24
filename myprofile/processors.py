from .models import Profile


def ctx_dict(request):
    ctx = {}
    profiles = Profile.objects.all()
    ctx = {
        "my_name": "Mi nombre",
        "my_occupation": "Mi ocupación",
        "my_avatar": "",
        "my_biography": "Mi biografía",
        "my_age": "Mi edad",
        "my_phone": "Mi teléfono",
        "my_email": "Mi correo electrónico",
    }

    for profile in profiles:
        ctx = {
            "my_name": profile.name,
            "my_occupation": (profile.occupation),
            "my_avatar": profile.my_avatar,
            "my_biography": profile.biography,
            "my_age": profile.age,
            "my_phone": profile.phone,
            "my_email": profile.email,
        }
    return ctx
