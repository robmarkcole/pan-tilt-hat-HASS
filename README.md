# pan-tilt-phat-HASS
This component adds the (pimoroni)[https://shop.pimoroni.com/products/pan-tilt-hat] pan-tilt-phat to (Home-assistant)[https://home-assistant.io/]. It is complemented by an ipanel which displays the camera feed and stage controls using (this fork)[https://github.com/waveform80/pistreaming/tree/pantilthat] of a project discussed on (this thread)[http://forums.pimoroni.com/t/help-building-an-pan-tilt-webinterface-for-pimoroni-pan-tilt-hat-full-kit-with-webcam-server/3654/19]. I have found the video rate in the ipanel to be faster than the native still image display in the HASS front end.


Test you camera. Place the pan_tilt.py file in your custom components folder, i.e. <config_dir>/custom_components/sensor/pan_tilt.py
and add to your configuration file:

```
camera:
  - platform: rpi_camera
    vertical_flip: 1

sensor:
  platform: pan_tilt

group:
  default_view:
    view: yes
    icon: mdi:home
    entities:
      - camera.raspberry_pi_camera
      - sensor.pan_tilt
```

<img src="https://github.com/robmarkcole/pan-tilt-phat-HASS/blob/master/my_pan_tilt.png">
