from .client import YouGileBaseClient


class ProjectsAPI(YouGileBaseClient):
    def create_project(self, title, users=None):
        data = {"title": title}
        if users:
            data["users"] = users
        return self._request("POST", "/projects", json=data)

    def get_project(self, project_id):
        return self._request("GET", f"/projects/{project_id}")

    def get_projects(self):
        return self._request("GET", "/projects")

    def update_project(self, project_id, **kwargs):
        data = {k: v for k, v in kwargs.items() if v is not None}
        return self._request("PUT", f"/projects/{project_id}", json=data)

    def delete_project(self, project_id):
        return self.update_project(project_id, deleted=True)
