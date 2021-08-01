import uuid


def get_generate_uuid(request):
    if 'uuid' not in request.session:
        print("Not session uuid")
        new_uuid = uuid.uuid4()
        print(str(new_uuid))
        request.session['uuid'] = str(new_uuid)
        print("session uuid now",request.session['uuid'])
    else:
        print("session is ok")
        print(request.session['uuid'])

    return request.session['uuid']