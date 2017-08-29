---
layout: page
title: "Pan-tilt HAT"
description: "Instructions on addint the Pan-Tilt hat to Home Assistant."
date: 2017-08-29 19:00
sidebar: true
comments: false
sharing: true
footer: true
logo: raspberry-pi.png
ha_category: DIY
ha_release: 0.53
ha_iot_class: "Local Push"
---

The `pan_tilt_phat` platform allows you to control a [Pimoroni Pan-Tilt hat](https://shop.pimoroni.com/products/pan-tilt-hat) mounted on the raspberry-pi running Home Assistant. This documentation assumes you have a [raspberry pi camera](https://home-assistant.io/components/camera.rpi_camera/) mounted on the hat, although other brands of camera could be used. This platform does not currently support control of the LED's described on the Pimorni page.

The Pan-tilt hat has two servos each with 180 degrees of motion (+/- 90 degrees) along each axis. This platform provides services for setting the angle of each servo. It also provides a service to home the servos to zero degrees on both axis. This documentation describes how to setup [input_sliders](https://home-assistant.io/components/input_slider/) on the Home Assistant front end to control the servos.

To add this platform to your installation, add the following to your `configuration.yaml` file:

```yaml
# Example configuration.yaml entry,
# which is equivalent to the default setup
sensor:
  - platform: pan_tilt_phat
```
DISCUSS THE SERVICES.

To additionally add the raspberry pi camera (in the correct orientation) and the input sliders to control the servos, also add the following to your `configuration.yaml` file:
```yaml
camera:
  - platform: rpi_camera
    vertical_flip: 1

input_slider:
  pan_control:
    name: Pan
    initial: 0
    min: -90
    max: 90
    step: 1
  tilt_control:
    name: Tilt
    initial: 0
    min: -90
    max: 90
    step: 1
```
