# -*- coding: utf-8 -*-
import pytest
from api.auth import AuthAPI
from api.projects import ProjectsAPI
from config import LOGIN, PASSWORD


COMPANY_ID = "f5d29675-c0c6-4cd0-abcf-ad6fd4e06c5b"


@pytest.fixture(scope="session")
def auth_token():
    auth = AuthAPI()
    key_result = auth.get_api_key(LOGIN, PASSWORD, COMPANY_ID)
    if "key" not in key_result:
        pytest.skip(f"Не удалось получить API ключ: {key_result}")
    print(" API ключ получен")
    return key_result["key"]


@pytest.fixture
def projects_api(auth_token):
    return ProjectsAPI(token=auth_token)


@pytest.fixture
def test_project_id(projects_api):
    result = projects_api.create_project("Тестовый проект")
    if "id" not in result:
        pytest.skip(f"Не удалось создать тестовый проект: {result}")
    project_id = result["id"]
    print(f" Создан тестовый проект с ID: {project_id}")
    yield project_id
    projects_api.delete_project(project_id)
    print(" Тестовый проект удалён")
