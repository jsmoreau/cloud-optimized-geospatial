# Accès à l'API STAC du CCCOT
Exemples sur l'utilisation de bibliothèques Python pour découvrir les
collections de l'API STAC du cube de données du CCCOT.

## Utilisation de [pystac-client]

Les développeurs de la bibliothèque pystac-client fournissent plusieurs [exemples](https://pystac-client.readthedocs.io/en/latest/tutorials.html) pour interagir avec
l'API STAC. Veuillez vous référer à ceux-ci et consulter la [documentation pystac-client](https://pystac-client.readthedocs.io/en/latest/quickstart.html) pour plus d'informations.

Pour les erreurs de certificat lors de l'accès à l'API STAC, consultez la documentation sur l'[utilisation de certificats personnalisés](https://pystac-client.readthedocs.io/en/stable/usage.html#using-custom-certificates).

``` sh
--8<-- "how-to-guides/pystac-client-requirements.txt:3:3"
```

### Lister les collections

Dans cet exemple, vous apprendrez comment interroger une API STAC avec pystac-client pour obtenir les collections disponibles.

``` py linenums="1"
--8<-- "how-to-guides/pystac-client-collections-example.py:code"
```

### Lister les éléments

Dans cet exemple, vous apprendrez comment :

- Interroger une API STAC avec pystac-client avec une portion de filtre
- Accéder au lien href des données pour le filtre spécifique

!!! info
    Cet exemple spécifique utilise la collection **hrdem-mosaic-2m** du cube de données du CCCOT

Pour plus de détails sur les paramètres de recherche disponibles avec pystac-client, consultez la documentation sur la [recherche d'éléments](https://pystac-client.readthedocs.io/en/stable/usage.html#itemsearch).

``` py linenums="1"
--8<-- "how-to-guides/pystac-client-items-example.py:code"
```

[pystac-client]: https://github.com/stac-utils/pystac-client

*[COG]: GeoTIFF optimisé pour le nuage
*[STAC]: Catalogue de ressources spatio-temporelles
*[CCCOT]: Centre canadien de cartographie et d'observation de la Terre, Ressources naturelles Canada




