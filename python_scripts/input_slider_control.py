entity_id = 'sensor.pan_tilt_phat'
state = hass.states.get(entity_id).state   # Pan: angle
pan_angle = state.split(':')[1]           # Gets the angle
logger.warning("pan_angle {}".format(pan_angle))

hass.services.call('input_slider', 'select_value',
    {"entity_id":"input_slider.pan_control", "value": str(pan_angle)})
