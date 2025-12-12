# Bibliothèques supplémentaires

Les exemples suivants se concentrent sur le chargement de données COG dans un objet xarray soutenu par Dask pour une lecture et un traitement efficaces en mémoire.

!!! info
    [Xarray] est construit sur NumPy et Pandas, ajoutant des capacités pour les tableaux étiquetés et multidimensionnels (par exemple, données climatiques, images satellites). Il étend les tableaux NumPy en attachant des métadonnées (coordonnées, étiquettes), facilitant le travail avec les dimensions de données comme le temps, la latitude, la longitude et d'autres variables.

    Xarray peut utiliser des tableaux Dask pour une évaluation paresseuse, permettant de travailler avec de grands ensembles de données qui ne tiennent pas en mémoire. Dask optimise les flux de travail en parallélisant les tâches, en lisant les données par morceaux et en améliorant les performances et l'efficacité de la mémoire.

    Source : [Xarray: Parallel Computing with Dask] 

!!! Note
    Les exemples suivants commencent par une requête à l'API STAC du CCCOT via la bibliothèque pystac-client.

    Pour plus de détails sur la découverte de données via l'API STAC, consultez la section **[Interaction avec l'API STAC du CCCOT]**

## Utilisation de Rioxarray

``` sh
--8<-- "how-to-guides/rioxarray-requirements.txt"
```
Source :  [rioxarray installation]

::: how-to-guides.rioxarray-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC

``` py linenums="1" hl_lines="20-23"
--8<-- "how-to-guides/rioxarray-example.py:code"
```
Voir la section [utilisation-objet-xarray] ou [exemples-complets-notebooks-communautaires] pour un exemple d'utilisation d'un objet Xarray.

## De l'objet pystac item à l'objet Xarray

Consultez [pystac.Item] ou [pystac-client] pour plus d'informations.

!!! Warning
    Les bibliothèques suivantes ne font pas partie de l'écosystème [STAC utils]. Soyez conscient de l'état de maintenance de ces bibliothèques.

!!! Warning
    GetGeoTransform de GDAL et rasterio utilisent des formats différents pour les métadonnées de transformation. Lors de l'utilisation de méthodes basées sur GDAL, vous devez réorganiser la transformation.
    Voir [Réorganiser le proj:Transform STAC] pour plus de détails.
    ``` py
    --8<-- "how-to-guides/odc-stac-example.py:transform"
    ```
        
    For more information, please see [STAC documentation on proj:transform]

### Utilisation de [stackstac]

``` sh
--8<-- "how-to-guides/stackstac-requirements.txt"
```

<!-- START: Read with stackstac-stac -->
::: how-to-guides.stackstac-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC

``` py linenums="1" hl_lines="36-41"
--8<-- "how-to-guides/stackstac-example.py:code"
```

See [working-with-xarray-object] or [community-notebook-complete-examples] section for an example on using Xarray object.

### Utilisation de [odc-stac]

``` sh
--8<-- "how-to-guides/odc-stac-requirements.txt"
```

<!-- START: Read with odc-stac -->
::: how-to-guides.odc-stac-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC

``` py linenums="1" hl_lines="38-41"
--8<-- "how-to-guides/odc-stac-example.py:code"
```
See [working-with-xarray-object] or [community-notebook-complete-examples] section for an example on using Xarray object.

## Utilisation d'un objet Xarray
Consultez `Xarray.DataArray` pour les détails sur les méthodes : <https://docs.xarray.dev/en/stable/generated/xarray.DataArray.html>
``` py linenums="1"
--8<-- "how-to-guides/stackstac-example.py:example"
```
## Exemples complets de notebooks communautaires

- [Chargement de multi-collections dans un Xarray.Dataset]
- [Calcul de la direction d'écoulement en utilisant la bibliothèque libre pyflwdir et Xarray.DataArray]

[Access COG data using rioxarray]: example-cogs.md/#using-rioxarray
[Xarray]: https://docs.xarray.dev/en/stable/
[Xarray: Parallel Computing with Dask]: https://docs.xarray.dev/en/stable/user-guide/dask.html
[STAC documentation on proj:transform]:  https://github.com/stac-extensions/projection?tab=readme-ov-file#projtransform
[Re-order the STAC proj:Transform]: reorder-transform-example.md
[STAC utils]: https://github.com/stac-utils
[pystac-client]: https://pystac-client.readthedocs.io/en/stable/
[pystac.Item]: https://pystac.readthedocs.io/en/latest/api/pystac.html#item
[stackstac]: https://stackstac.readthedocs.io/en/latest/
[odc-stac]: https://odc-stac.readthedocs.io/en/latest/
[rioxarray installation]: https://corteva.github.io/rioxarray/stable/installation.html
[rioxarray]: https://corteva.github.io/rioxarray/stable/index.html
[Xarray]: https://docs.xarray.dev/en/stable/
[Xarray: Parallel Computing with Dask]: https://docs.xarray.dev/en/stable/user-guide/dask.html
[Interaction avec l'API STAC du CCCOT]: pystac-client.md
[Re-order the STAC proj:Transform]: reorder-transform-example.md
[Réorganiser le proj:Transform STAC]: reorder-transform-example.md
[utilisation-objet-xarray]: #utilisation-dun-objet-xarray
[exemples-complets-notebooks-communautaires]: #exemples-complets-de-notebooks-communautaires
<!-- TODO : Find a better way to link those jupyternotebooks... -->
[Chargement de multi-collections dans un Xarray.Dataset]: https://github.com/NRCan/cloud-optimized-geospatial/blob/ec2de7af4249ee53b9c1cdf106e8fa9b6118b5cb/how-to-guides/notebook/multi-collection-example.ipynb
[Calcul de la direction d'écoulement en utilisant la bibliothèque libre pyflwdir et Xarray.DataArray]: https://github.com/NRCan/cloud-optimized-geospatial/blob/ec2de7af4249ee53b9c1cdf106e8fa9b6118b5cb/how-to-guides/notebook/pyflwdir-example.ipynb
