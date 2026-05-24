from .models import Background


def ctx_dict(request):
    ctx = {}
    backgrounds = Background.objects.all()
    for background in backgrounds:
        ctx = {
            "home_image": background.home_image,
            "biography_image": background.biography_image,
            "portfolio_image": background.portfolio_image,
        }
    return ctx
