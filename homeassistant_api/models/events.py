"""Event Model File"""

from typing import TYPE_CHECKING, Dict, cast

from pydantic import BaseModel

if TYPE_CHECKING:
    from homeassistant_api import Client


class Event(BaseModel):
    """
    Event class for Homeassistant Event Triggers

    For attribute information see the Data Science docs on Event models
    https://data.home-assistant.io/docs/events
    """

    event_type: str
    listener_count: int
    client: "Client"

    def fire(self, **event_data) -> str:
        """Fires the corresponding event in Home Assistant."""
        data = self.client.fire_event(self.event_type, **event_data)
        return cast(Dict[str, str], data).get("message", "No message provided")
