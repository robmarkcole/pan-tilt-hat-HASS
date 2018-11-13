This custom component adds the [pimoroni](https://shop.pimoroni.com/products/pan-tilt-hat) pan-tilt-phat to [Home-assistant](https://home-assistant.io/).

<img src="https://github.com/robmarkcole/pan-tilt-phat-HASS/blob/master/my_pan_tilt.png" width="300">

Place the custom_components folder in your configuration directory (or add its contents to an existing custom_components folder). Add to your `configuration.yaml`:
```yaml
pan_tilt_phat:
```

The adds the services:
* `pan_tilt_phat.home` called with no data to return to home (0, 0)
* `pan_tilt_phat.pan` which can be called with e.g. `{"Pan":20}` to pan to 20 degrees
* `pan_tilt_phat.tilt` which can be called with e.g. `{"Tilt":30}` to tilt to 30 degrees


## Python scripts & automation
This repo also includes python scripts and automations to add slider control as shown in the image below. Moving the sliders triggers an automation which calls the python script to move the pan-tilt-hat. Copy the required content of the example config files to your own config files.

<img src="https://github.com/robmarkcole/pan-tilt-phat-HASS/blob/master/main_hass_pan_tilt.png" width="800">
