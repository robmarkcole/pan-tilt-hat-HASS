"""
Support for pan-tilt pHAT sensors.

For more details about this component, please refer to the documentation at
https://home-assistant.io/components/sensor.pantiltphat
"""

import logging

from homeassistant.helpers.entity import Entity

REQUIREMENTS = ['pantilthat==0.0.4']
_LOGGER = logging.getLogger(__name__)
DEFAULT_NAME = 'pantiltphat'

def setup_platform(hass, config, add_devices, discovery_info=None):
    try:
        # pylint: disable=import-error
        import pantilthat
    except OSError:
        _LOGGER.error("No pan-tilt pHAT was found.")
        return False

    add_devices([PanTiltStage()], True)

class PanTiltStage(Entity):
    """Representation of the stage."""

    def __init__(self):
        """Initialize the stage."""
        self._name = DEFAULT_NAME
        self._state = None       # json obj with pan and tilt

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def icon(self):
        """Icon to use in the frontend, if any."""
        return 'mdi:mdi-camera-switch'
