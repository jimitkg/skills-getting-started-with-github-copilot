from fastapi.testclient import TestClient

from src.app import activities, app


def test_unregister_participant_removes_participant_from_activity():
    activity_name = "Chess Club"
    email = "student@example.edu"
    activities[activity_name]["participants"].append(email)

    try:
        response = TestClient(app).delete(
            f"/activities/{activity_name}/participants/{email}"
        )

        assert response.status_code == 200
        assert email not in activities[activity_name]["participants"]
    finally:
        if email in activities[activity_name]["participants"]:
            activities[activity_name]["participants"].remove(email)


def test_unregister_missing_participant_returns_not_found():
    response = TestClient(app).delete(
        "/activities/Chess Club/participants/missing@example.edu"
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found"
