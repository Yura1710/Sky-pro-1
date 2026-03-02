from .client import YouGileBaseClient


class AuthAPI(YouGileBaseClient):
    def get_company_id(self, login, password):
        return self._request(
            "POST",
            "/auth/companies",
            json={"login": login, "password": password}
        )

    def get_api_key(self, login, password, company_id):
        return self._request(
            "POST",
            "/auth/keys",
            json={
                "login": login,
                "password": password,
                "companyId": company_id
            }
        )
