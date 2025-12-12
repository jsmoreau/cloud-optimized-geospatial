# --8<-- [start:code]
# Import the library needed
import pystac_client

# Link to ccmeo datacube stac-api
stac_root = "https://datacube.services.geo.ca/stac/api"
# Initialize the STAC client
catalog = pystac_client.Client.open(stac_root)

# Get the list of available collection id
for collection in catalog.get_collections():
    print(collection.id)
# --8<-- [end:code]