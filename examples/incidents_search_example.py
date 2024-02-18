from __future__ import print_function
import xsoar_client.xsoar_api
from xsoar_client.xsoar_api.rest import ApiException
from pprint import pprint

api_key = None  # set to your 'YOUR_API_KEY' or set environment variable: XSOAR_API_KEY
base_url = None  # set to your 'http://XSOAR_HOST' or set environment variable: XSOAR_BASE_URL

# create an instance of the API class
api_instance = xsoar_client.configure(base_url=base_url, api_key=api_key, debug=True)
filter = xsoar_client.xsoar_api.SearchIncidentsData()

# Create incident filter object
inc_filter = xsoar_client.xsoar_api.IncidentFilter()
inc_filter.name = ['test']

filter.filter = inc_filter

try:
    # Search incidents by filter
    api_response = api_instance.search_incidents(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->search_incidents: %s\n" % e)
