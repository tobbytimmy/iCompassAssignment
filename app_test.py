from sanitized_inputs import app
from flask import json

def test_1():
    response = app.test_client().post(
        '/v1/sanitized/input/',
        data = json.dumps({"payload" : "input"}),
        content_type = "application/json",
    )

    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['result'] == "sanitized"


def test_2():
    response = app.test_client().post(
        '/v1/sanitized/input/',
        data = json.dumps({"payload" : "in\p&ut"}),
        content_type = "application/json",
    )

    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['result'] == "unsanitized"