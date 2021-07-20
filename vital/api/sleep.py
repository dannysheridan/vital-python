from typing import List, Mapping, Optional

from vital.api.api import API


class Sleep(API):
    """Endpoints for getting sleep data."""

    def get(
        self,
        user_key: str,
        start_date: str,
        end_date: str,
        provider: Optional[str] = "",
    ) -> Mapping[str, List[Mapping]]:
        """
        GET Sleep data.
        """
        return self.client.get(
            f"/sleep/{user_key}",
            params={
                "start_date": start_date,
                "end_date": end_date,
                "provider": provider,
            },
        )

    def get_stream(self, sleep_id: str) -> Mapping[str, List[Mapping]]:
        """
        GET Sleep stream data.
        """
        return self.client.get(
            f"/sleep/{sleep_id}/stream/data",
        )
