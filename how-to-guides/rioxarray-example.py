# --8<-- [start:code]
import pystac_client
import rioxarray

bbox=[-75.8860,45.3157,-75.5261,45.5142] 
bbox_crs = "EPSG:4326"

# Link to ccmeo datacube stac-api
stac_root = "https://datacube.services.geo.ca/stac/api"
# Initialize the STAC client
catalog = pystac_client.Client.open(stac_root)

search = catalog.search(
	collections=['mrdem-30'], 
    bbox=bbox,
	) 

# Use the rioxarray.open_rasterio() and clip it to the bbox
for page in search.pages():
    for item in page:
        band = rioxarray.open_rasterio(
            item.assets['dtm'].href, 
            chunks=512,
            ).rio.clip_box(*bbox,crs=bbox_crs)

# At this point the data is not read in the Xarray object
# See the Xarray object details
print(band)
# <xarray.DataArray (band: 1, y: 999, x: 1134)> Size: 5MB
# dask.array<getitem, shape=(1, 999, 1134), dtype=float32, chunksize=(1, 512, 512), chunktype=numpy.ndarray>
# Coordinates:
#   * band         (band) int64 8B 1
#   * x            (x) float64 9kB 1.493e+06 1.493e+06 ... 1.527e+06 1.527e+06
#   * y            (y) float64 8kB -1.557e+05 -1.558e+05 ... -1.857e+05 -1.857e+05
#     spatial_ref  int64 8B 0
# Attributes:
#     TIFFTAG_DATETIME:  2024:12:12 12:00:00
#     AREA_OR_POINT:     Area
#     scale_factor:      1.0
#     add_offset:        0.0
#     _FillValue:        -32767.0

# At this point, the metadata and array shape are set, but the data itself isn't read.
# Running .compute() allows Dask to optimize the workflow, evaluating and executing it 
# in the most efficient way, optimizing resource usage.

# Perform analysis...

# To read the data
band.compute()
# --8<-- [end:code]



