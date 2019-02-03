from api.models import Doc


def get_doc_by_id(doc_id):
    """
    return doc by given doc id
    """
    doc = Doc.objects.filter(id=doc_id).first()
    return doc
