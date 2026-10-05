from src.app import activities


def test_unregister_participant_removes_participant_from_activity(client):
    # Arrange
    activity_name = "Chess Club"
    email = "student@example.edu"
    activities[activity_name]["participants"].append(email)

    # Act
    response = client.delete(
        f"/activities/{activity_name}/participants/{email}"
    )

    # Assert
    assert response.status_code == 200
    assert email not in activities[activity_name]["participants"]


def test_unregister_missing_participant_returns_not_found(client):
    # Arrange
    activity_name = "Chess Club"
    email = "missing@example.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/participants/{email}"
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found"
