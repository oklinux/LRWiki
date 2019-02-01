from api.models import Doc

def create_doc(**validated_data):
    '''
    create doc by title,text,account
    :param data:
    :return Doc:
    '''
    doc = Doc.objects.create(
        **validated_data
    )
    return doc
