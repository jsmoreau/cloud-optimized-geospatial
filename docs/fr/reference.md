<!-- ---
subtitle: Rassemblement non exhaustif de ressources pertinentes.
--- -->

# Références externes

## Solutions optimisées pour le nuage
[Guide des formats géospatiaux optimisés pour le nuage] de Cloud Native Geospatial
### Références suggérées pour STAC
- [Spécification STAC]
- [Tutoriel STAC]
- Écosystème [STAC utils]
### Références suggérées pour les COG
- Format COG [introduction] et [avancé] de Cloud Native Geospatial

---
## Utilisation de Python
### Références suggérées pour l'utilisation de l'API STAC
- pystac-client

    - [Installer pystac-client]
    - [Dépôt GitHub]
    - Liens utiles du site de documentation [pystac-client] :
        - [Exemple d'utilisation de recherche d'éléments]
        - [Tutoriel de recherche d'éléments avec intersects]
        - [Référence API de recherche d'éléments]

### Références suggérées pour l'accès aux COG
- [rasterio]

    - [Démarrage rapide]
    - [Lecture d'ensemble de données]

- GDAL

    - [Options COG de GDAL]
    - [Modules CLI de GDAL]

- [rioxarray]

    - [Démarrage]
    - [Exemples]

### Bibliothèques Python supplémentaires
- [stackstac]

    - [Exemple de base]

- [xarray]
- [dask]

---
## Utilisation de QGIS
### Plugin de navigation STAC dans QGIS
- [Plugin STAC API Browser]
- QGIS [CHANGELOG] avec nouvelles fonctionnalités STAC

### Ressources pour le streaming de données depuis QGIS
- [Tutoriel] chargement d'un COG dans QGIS


[pystac-client]: https://pystac-client.readthedocs.io/en/stable/
[Exemple d'utilisation de recherche d'éléments]: https://pystac-client.readthedocs.io/en/stable/usage.html#itemsearch
[Référence API de recherche d'éléments]: <https://pystac-client.readthedocs.io/en/stable/api.html#item-search>
[Tutoriel de recherche d'éléments avec intersects]: https://pystac-client.readthedocs.io/en/stable/tutorials/item-search-intersects.html
[Dépôt GitHub]: https://github.com/stac-utils/pystac-client/tree/main/docs/tutorials
[Installer pystac-client]: https://github.com/stac-utils/pystac-client
[Spécification STAC]: https://stacspec.org/en/
[Tutoriel STAC]: https://stacspec.org/en/tutorials/
[Guide des formats géospatiaux optimisés pour le nuage]: https://guide.cloudnativegeo.org/
[introduction]: https://guide.cloudnativegeo.org/cloud-optimized-geotiffs/intro.html
[avancé]: https://guide.cloudnativegeo.org/cloud-optimized-geotiffs/cogs-details.html
[rasterio]: https://github.com/rasterio/rasterio
[Lecture d'ensemble de données]: https://rasterio.readthedocs.io/en/stable/topics/reading.html
[Démarrage rapide]: https://rasterio.readthedocs.io/en/stable/quickstart.html
[stackstac]: https://stackstac.readthedocs.io/en/latest/
[Exemple de base]: https://stackstac.readthedocs.io/en/latest/basic.html
[Options COG de GDAL]: https://gdal.org/en/stable/drivers/raster/cog.html#raster-cog
[Modules CLI de GDAL]: https://gdal.org/en/stable/programs/index.html#raster-programs
[rioxarray]: https://corteva.github.io/rioxarray/stable/
[Démarrage]: https://corteva.github.io/rioxarray/stable/getting_started/getting_started.html
[Exemples]: <https://corteva.github.io/rioxarray/stable/examples/examples.html
[xarray]: https://xarray.dev/
[dask]: https://docs.dask.org/en/stable/
[Plugin STAC API Browser]: https://stacspec.org/en/tutorials/2-intro-to-stac-api-browser-qgis-plugin/
[CHANGELOG]: https://qgis.org/project/visual-changelogs/visualchangelog340/#feature-stac-integration
[Tutoriel]: https://cogeo.org/qgis-tutorial.html
[STAC utils]: https://github.com/stac-utils

*[COG]: GeoTIFF optimisé pour le nuage
*[STAC]: Catalogue de ressources spatio-temporelles