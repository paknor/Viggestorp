state = hass.states.get('sensor.sn2_pir')
move = state.state

if move == '1':
    hass.services.call('light', 'turn_on', { "entity_id" : 'light.led_strip', 'rgb_color': [255, 0, 0] })
else:
   hass.services.call('light', 'turn_on', { "entity_id" : 'light.led_strip', 'rgb_color': [255, 255, 255] })