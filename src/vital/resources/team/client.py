# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.remove_none_from_dict import remove_none_from_dict
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.client_facing_physician import ClientFacingPhysician
from ...types.client_facing_team import ClientFacingTeam
from ...types.client_facing_user import ClientFacingUser
from ...types.http_validation_error import HttpValidationError

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TeamClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_link_config(self) -> typing.Dict[str, typing.Any]:
        """
        Post teams.

        ---
        from vital.client import Vital

        client = Vital(
            api_key="YOUR_API_KEY",
        )
        client.team.get_link_config()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v2/team/link/config"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Dict[str, typing.Any], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, team_id: str) -> ClientFacingTeam:
        """
        Get team.

        Parameters:
            - team_id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/team/{team_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ClientFacingTeam, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_user_by_id(self, *, query_id: typing.Optional[str] = None) -> typing.List[ClientFacingUser]:
        """
        Search team users by user_id

        Parameters:
            - query_id: typing.Optional[str].
        ---
        from vital.client import Vital

        client = Vital(
            api_key="YOUR_API_KEY",
        )
        client.team.get_user_by_id()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v2/team/users/search"),
            params=remove_none_from_dict({"query_id": query_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[ClientFacingUser], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_svix_url(self) -> typing.Dict[str, typing.Any]:
        """
        from vital.client import Vital

        client = Vital(
            api_key="YOUR_API_KEY",
        )
        client.team.get_svix_url()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v2/team/svix/url"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Dict[str, typing.Any], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_source_priorities(
        self, *, data_type: typing.Optional[str] = None
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        GET source priorities.

        Parameters:
            - data_type: typing.Optional[str].
        ---
        from vital.client import Vital

        client = Vital(
            api_key="YOUR_API_KEY",
        )
        client.team.get_source_priorities()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v2/team/source/priorities"),
            params=remove_none_from_dict({"data_type": data_type}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[typing.Dict[str, typing.Any]], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_source_priorities(self, *, team_id: str) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        Patch source priorities.

        Parameters:
            - team_id: str.
        ---
        from vital.client import Vital

        client = Vital(
            api_key="YOUR_API_KEY",
        )
        client.team.update_source_priorities(
            team_id="team-id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v2/team/source/priorities"),
            params=remove_none_from_dict({"team_id": team_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[typing.Dict[str, typing.Any]], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_physicians(self, team_id: str) -> typing.List[ClientFacingPhysician]:
        """
        Parameters:
            - team_id: str.
        ---
        from vital.client import Vital

        client = Vital(
            api_key="YOUR_API_KEY",
        )
        client.team.get_physicians(
            team_id="team-id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/team/{team_id}/physicians"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[ClientFacingPhysician], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncTeamClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_link_config(self) -> typing.Dict[str, typing.Any]:
        """
        Post teams.

        ---
        from vital.client import AsyncVital

        client = AsyncVital(
            api_key="YOUR_API_KEY",
        )
        await client.team.get_link_config()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v2/team/link/config"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Dict[str, typing.Any], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, team_id: str) -> ClientFacingTeam:
        """
        Get team.

        Parameters:
            - team_id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/team/{team_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ClientFacingTeam, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_user_by_id(self, *, query_id: typing.Optional[str] = None) -> typing.List[ClientFacingUser]:
        """
        Search team users by user_id

        Parameters:
            - query_id: typing.Optional[str].
        ---
        from vital.client import AsyncVital

        client = AsyncVital(
            api_key="YOUR_API_KEY",
        )
        await client.team.get_user_by_id()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v2/team/users/search"),
            params=remove_none_from_dict({"query_id": query_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[ClientFacingUser], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_svix_url(self) -> typing.Dict[str, typing.Any]:
        """
        from vital.client import AsyncVital

        client = AsyncVital(
            api_key="YOUR_API_KEY",
        )
        await client.team.get_svix_url()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v2/team/svix/url"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Dict[str, typing.Any], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_source_priorities(
        self, *, data_type: typing.Optional[str] = None
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        GET source priorities.

        Parameters:
            - data_type: typing.Optional[str].
        ---
        from vital.client import AsyncVital

        client = AsyncVital(
            api_key="YOUR_API_KEY",
        )
        await client.team.get_source_priorities()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v2/team/source/priorities"),
            params=remove_none_from_dict({"data_type": data_type}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[typing.Dict[str, typing.Any]], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_source_priorities(self, *, team_id: str) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        Patch source priorities.

        Parameters:
            - team_id: str.
        ---
        from vital.client import AsyncVital

        client = AsyncVital(
            api_key="YOUR_API_KEY",
        )
        await client.team.update_source_priorities(
            team_id="team-id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v2/team/source/priorities"),
            params=remove_none_from_dict({"team_id": team_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[typing.Dict[str, typing.Any]], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_physicians(self, team_id: str) -> typing.List[ClientFacingPhysician]:
        """
        Parameters:
            - team_id: str.
        ---
        from vital.client import AsyncVital

        client = AsyncVital(
            api_key="YOUR_API_KEY",
        )
        await client.team.get_physicians(
            team_id="team-id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/team/{team_id}/physicians"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[ClientFacingPhysician], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
