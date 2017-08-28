"""
Support for pan-tilt pHAT.

For more details about this component, please refer to the documentation at
https://home-assistant.io/components/sensor.pan_tilt_phat
"""

import logging

from homeassistant.helpers.entity import Entity

REQUIREMENTS = ['pantilthat==0.0.4']
_LOGGER = logging.getLogger(__name__)
DOMAIN = 'pan_tilt_phat'

def setup_platform(hass, config, add_devices, discovery_info=None):
    try:
        import pantilthat
    except OSError:
        _LOGGER.error("No pan-tilt pHAT was found.")
        return False

    add_devices([PanTiltPhat()], True)

class PanTiltPhat(Entity):
    """Representation of the stage."""

    ICON = 'mdi:camera-switch'

    def __init__(self):
        """Initialize the stage."""
        self._name = DOMAIN
        self._state = None       # json obj with pan and tilt

    def home(self):
        """Return the name of the sensor."""
        self._pantilt.pan(0)
        self._pantilt.tilt(0)
        return

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
        return self.ICON
