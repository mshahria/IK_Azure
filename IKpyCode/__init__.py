import azure.functions as func
import json
from your_main_script import get_angles  # Import your main function logic


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Parse incoming request
        req_body = req.get_json()
        px, py, pz, roll, pitch, yaw = [req_body.get(key) for key in ("px", "py", "pz", "roll", "pitch", "yaw")]

        # Call your main function
        q1, q2, q3, q4, q5, q6 = get_angles(px, py, pz, roll, pitch, yaw)

        # Return the result
        return func.HttpResponse(json.dumps({"q1": q1, "q2": q2, "q3": q3, "q4": q4, "q5": q5, "q6": q6}),
                                 status_code=200)
    except Exception as e:
        return func.HttpResponse("Error: " + str(e), status_code=500)
