def test_tasks_get_all(client, tasks):  # Arrange
    """Test get all tasks"""
    # Act
    response = client.get("/api/v1/tasks/")
    # Assert
    assert response.status_code == 200
    data = response.json["tasks"]
    assert len(data) == 3
    for task in tasks:
        assert task.id in [item["id"] for item in data]
        assert task.name in [item["name"] for item in data]


def test_tasks_get_one(client, tasks):  # Arrange
    """Test get all tasks"""
    for task in tasks:
        # Act
        response = client.get(f"/api/v1/tasks/{task.id}")
        data = response.json
        # Assert
        assert response.status_code == 200
        assert data["name"] == task.name
        assert data["description"] == task.description
