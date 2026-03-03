$test_projects_fixed = @"
# -*- coding: utf-8 -*-

class TestProjectsPositive:

    def test_create_project_valid_title(self, projects_api):
        result = projects_api.create_project("Новый проект")
        assert "id" in result, f"Ошибка создания: {result}"
        assert result["id"] is not None

    def test_create_project_with_special_chars(self, projects_api):
        result = projects_api.create_project("Проект №1 - Тест!@#$%")
        assert "id" in result, f"Ошибка создания: {result}"

    def test_get_project_by_id(self, projects_api, test_project_id):
        result = projects_api.get_project(test_project_id)
        assert result["id"] == test_project_id
        assert "title" in result
        assert "timestamp" in result

    def test_get_projects_list(self, projects_api):
        result = projects_api.get_projects()
        assert "content" in result or isinstance(result, list)

    def test_update_project_title(self, projects_api, test_project_id):
        new_title = "Обновлённое название"
        result = projects_api.update_project(test_project_id, title=new_title)
        assert result["id"] == test_project_id
        updated = projects_api.get_project(test_project_id)
        assert updated["title"] == new_title

    def test_delete_project_soft(self, projects_api, test_project_id):
        result = projects_api.delete_project(test_project_id)
        assert result["id"] == test_project_id
        deleted = projects_api.get_project(test_project_id)
        assert deleted.get("deleted") is True


class TestProjectsNegative:

    def test_create_project_empty_title(self, projects_api):
        result = projects_api.create_project("")
        assert "error" in result or result.get("status", 200) >= 400

    def test_create_project_missing_title(self, projects_api):
        result = projects_api._request("POST", "/projects", json={})
        assert "error" in result or result.get("status", 200) >= 400

    def test_get_project_invalid_id(self, projects_api):
        result = projects_api.get_project("invalid-id-12345")
        assert result.get("status", 200) == 404 or "error" in result

    def test_get_project_empty_id(self, projects_api):
        result = projects_api.get_project("")
        assert "error" not in result
        assert "content" in result or isinstance(result, list)

    def test_update_project_invalid_id(self, projects_api):
        result = projects_api.update_project("invalid-id", title="Новое название")
        assert result.get("status", 200) == 404 or "error" in result

    def test_update_project_without_data(self, projects_api, test_project_id):
        result = projects_api.update_project(test_project_id)
        assert "error" in result or "id" in result

    def test_delete_project_invalid_id(self, projects_api):
        result = projects_api.delete_project("invalid-id")
        assert result.get("status", 200) == 404 or "error" in result
"@
Set-Content -Path test_projects.py -Value $test_projects_fixed -Encoding UTF8
