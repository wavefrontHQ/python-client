
import wavefront_api_client as wave_api

base_url = 'https://try.wavefront.com'
api_key = 'YOUR_API_KEY'

config = wave_api.Configuration()
config.host = base_url
client = wave_api.ApiClient(configuration=config, header_name='Authorization', header_value='Bearer ' + api_key)

# instantiate source API

source_api = wave_api.SourceApi(client)

sources = source_api.get_all_source()

print sources
