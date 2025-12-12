# Accès aux données COG
Exemples sur l'utilisation de bibliothèques Python pour accéder et utiliser les COG. Démonstration d'un des avantages de l'optimisation pour le nuage, soit la possibilité d'accéder à une **[portion des données]** sans avoir à télécharger le fichier complet.

Voir <https://guide.cloudnativegeo.org/>

!!! Note
    Les exemples suivants commencent par une requête à l'API STAC du CCCOT via la bibliothèque pystac-client.

    Pour plus de détails sur la découverte de données via l'API STAC, consultez la section **[Interaction avec l'API STAC du CCCOT]**

## Utilisation de [rasterio]

``` sh
--8<-- "how-to-guides/rasterio-requirements.txt:2:2"
```

<!-- START: Read the header of a cog using rasterio -->
::: how-to-guides.rasterio-header-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC

``` py linenums="1" hl_lines="23-35"
--8<-- "how-to-guides/rasterio-header-example.py:code"
```
<!-- END: Read the header of a cog using rasterio -->

<!-- START: Read a portion of a cog using rasterio -->
::: how-to-guides.rasterio-window-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC

``` py linenums="1" hl_lines="27-37"
--8<-- "how-to-guides/rasterio-window-example.py:code"
```
<!-- END: Read a portion of a cog using rasterio -->

<!-- START: Read pixel with coord using rasterio -->
::: how-to-guides.rasterio-point-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC

``` py linenums="1" hl_lines="34-38"
--8<-- "how-to-guides/rasterio-point-example.py:code"
```
<!-- END: Read pixel with coord cog using rasterio -->

[rasterio installation]: https://rasterio.readthedocs.io/en/stable/installation.html
[rasterio]: https://rasterio.readthedocs.io/en/latest/quickstart.html
[Interaction avec l'API STAC du CCCOT]: pystac-client.md
[portion des données]: #how-to-guides.rasterio-window-example--read-a-portion-of-a-remote-cog

*[COG]: GeoTIFF optimisé pour le nuage
*[STAC]: Catalogue de ressources spatio-temporelles
*[CCCOT]: Centre canadien de cartographie et d'observation de la Terre, Ressources naturelles Canada

