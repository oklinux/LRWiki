from api.models import Doc


def is_check_title_already_created(title):
    """
    check if title has been used
    """
    return Doc.objects.filter(title=title).exists()
