entity_id = 'input_slider.pan_control'
slider_value = int(float(hass.states.get(entity_id).state))
logger.warning("slider_value {}".format(slider_value))
hass.services.call('pan_tilt_phat', 'pan', {"Pan":slider_value})
