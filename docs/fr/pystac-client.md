# Accès à l'API STAC du CCCOT
Exemples sur l'utilisation de bibliothèques Python pour découvrir les
collections de l'API STAC du cube de données du CCCOT.

## Utilisation de [pystac-client]

``` sh
--8<-- "how-to-guides/pystac-client-requirements.txt:3:3"
```

<!-- START: Get a list of collections using pystac-client -->
::: how-to-guides.pystac-client-collections-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC


``` py linenums="1"
--8<-- "how-to-guides/pystac-client-collections-example.py:code"
```
<!-- END: Get a list of collections using pystac-client -->

<!-- START: Get a list of items using pystac-client -->
::: how-to-guides.pystac-client-items-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC


``` py linenums="1"
--8<-- "how-to-guides/pystac-client-items-example.py:code"
```
<!-- END: Get a list of items using pystac-client -->

[pystac-client]: https://github.com/stac-utils/pystac-client

*[COG]: GeoTIFF optimisé pour le nuage
*[STAC]: Catalogue de ressources spatio-temporelles
*[CCCOT]: Centre canadien de cartographie et d'observation de la Terre, Ressources naturelles Canada




