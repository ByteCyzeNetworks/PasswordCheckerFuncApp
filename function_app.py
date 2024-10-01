import azure.functions as func
import json
import logging
from zxcvbn import zxcvbn

app = func.FunctionApp()

@app.route(route="password_strength", auth_level=func.AuthLevel.ANONYMOUS)
def password_strength(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Password strength check initiated.')

    try:
        # Attempt to get the JSON body
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            "Invalid JSON body.",
            status_code=400
        )

    password = req_body.get('password')

    if not password:
        return func.HttpResponse(
            "Please provide a password in the request body.",
            status_code=400
        )

    # Analyze password strength
    result = zxcvbn(password)
    score = result['score']
    feedback = result['feedback']

    response_body = {
        'strength_score': score,
        'feedback': feedback
    }

    return func.HttpResponse(
        json.dumps(response_body),
        status_code=200,
        mimetype="application/json"
    )
