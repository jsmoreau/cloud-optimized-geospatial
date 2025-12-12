# Accessing COG Data
Examples on how to use python libraries to access and use COGs. Demonstrating one of the cloud
optimized advantages, being able to access a **[portion of the data]** without having to download the entire file.  

See <https://guide.cloudnativegeo.org/>

!!! Note
    The following examples starts with a request to the CCMEO STAC API via the pystac-client library.  

    For more details on how to discover data through the STAC API, see the **[Interacting with CCMEO STAC API]** section

## Using [rasterio]

The developers of the rasterio library provide additional examples of usage.
For more details on the rasterio library, see the [rasterio](https://rasterio.readthedocs.io/en/latest/quickstart.html) documentation.

``` sh
--8<-- "how-to-guides/rasterio-requirements.txt:2:2"
```

### Read the header of a remote COG

In this code you will:

- Query a STAC API with pystac-client to get link to a COG
- Read header metadata from a remote COG file

!!! info
    This specific example uses the collection **mrdem-30** from CCMEO's datacube

``` py linenums="1" hl_lines="23-35"
--8<-- "how-to-guides/rasterio-header-example.py:code"
```

### Read a portion of a remote COG - Bounding box

For this example, you will need to also install [shapely](https://shapely.readthedocs.io/en/stable/installation.html):
```bash
pip install shapely
```

In this code you will:

- Query a STAC API with pystac-client to get link to a COG
- Read a portion of a remote COG based on an AOI with the window functionality
- Write the portion locally inside a .tif file (Optional)

!!! info
    This specific example uses the collection **mrdem-30** from CCMEO's datacube

!!! Tip
    COG's file contains internal tiling that can be leveraged by iterating on
    the `src.block_windows()` while reading. If the reading window does not align with
    the internal tiling of the file, the data will be resampled.

    Example: <https://rasterio.readthedocs.io/en/stable/topics/windowed-rw.html#blocks>

    API definition: <https://rasterio.readthedocs.io/en/stable/topics/windowed-rw.html#blocks>

``` py linenums="1" hl_lines="27-37"
--8<-- "how-to-guides/rasterio-window-example.py:code"
```

### Read a portion of a remote COG - Point

For this example, you will need to also install [shapely](https://shapely.readthedocs.io/en/stable/installation.html):
```bash
pip install shapely
```

In this code you will:

- Query a STAC API with pystac-client
- Read values of remote COG based on coordinates with the [sample()](https://rasterio.readthedocs.io/en/stable/api/rasterio.io.html#rasterio.io.DatasetReader.sample) functionality

!!! info
    This specific example uses the collection **mrdem-30** from CCMEO's datacube

!!! Tip
    To perform the same request using gdal, refer to the [gdallocationinfo](https://gdal.org/en/stable/programs/gdallocationinfo.html) utility

``` py linenums="1" hl_lines="34-38"
--8<-- "how-to-guides/rasterio-point-example.py:code"
```

[rasterio installation]: https://rasterio.readthedocs.io/en/stable/installation.html
[rasterio]: https://rasterio.readthedocs.io/en/latest/quickstart.html
[Interacting with CCMEO STAC API]: pystac-client.md
[portion of the data]: #how-to-guides.rasterio-window-example--read-a-portion-of-a-remote-cog

*[COG]: Cloud Optimized GeoTIFF
*[STAC]: Spatio-Temporal Asset Catalog
*[CCMEO]: Canada Center for Mapping and Earth Observation, Natural Resources Canada
