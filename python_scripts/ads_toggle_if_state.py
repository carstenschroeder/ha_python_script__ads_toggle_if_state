# https://www.home-assistant.io/components/python_script/

adsvar_toggle = data.get('adsvar_toggle')
state_entity = data.get('state_entity')
state = data.get('state')

if hass.states.is_state(state_entity, state) and adsvar_toggle:
    service_data = {}
    service_data['adstype'] = 'bool'
    service_data['adsvar'] = adsvar_toggle
    service_data['value'] = 1
    hass.services.call('ads', 'write_data_by_name', service_data)