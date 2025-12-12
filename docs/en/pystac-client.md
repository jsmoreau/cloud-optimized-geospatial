# Accessing CCMEO STAC API
Examples on how to use python libraries to discover the
collections from the CCMEO datacube STAC API. 

## Using [pystac-client]

The developers of the pystac-client library provide multiple [examples](https://pystac-client.readthedocs.io/en/latest/tutorials.html) for interacting with
STAC API. Please refer to those and consult the [pystac-client documentation](https://pystac-client.readthedocs.io/en/latest/quickstart.html) for additional information.

For certificate error while accessing the STAC API, see [using custom certificate](https://pystac-client.readthedocs.io/en/stable/usage.html#using-custom-certificates) documentation.

``` sh
--8<-- "how-to-guides/pystac-client-requirements.txt:3:3"
```

### List collections

In this example you will learn how to query a STAC API with pystac-client to get the available collections.

``` py linenums="1"
--8<-- "how-to-guides/pystac-client-collections-example.py:code"
```

### List items

In this example you will learn how to:

- Query a STAC API with pystac-client with a portion of filter
- Access the data href for the specific filter

!!! info
    This specific example uses the collection **hrdem-mosaic-2m** from CCMEO's datacube

For more details on search parameters available with pystac-client, see [items search](https://pystac-client.readthedocs.io/en/stable/usage.html#itemsearch) documentation.

``` py linenums="1"
--8<-- "how-to-guides/pystac-client-items-example.py:code"
```

[pystac-client]: https://github.com/stac-utils/pystac-client

*[COG]: Cloud Optimized GeoTIFF
*[STAC]: Spatio-Temporal Asset Catalog
*[CCMEO]: Canada Center for Mapping and Earth Observation, Natural Resources Canada


